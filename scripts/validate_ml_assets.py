from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = REPO_ROOT / "config"
MODEL_CARDS_DIR = REPO_ROOT / "mlflow" / "model_cards"
EXPERIMENTS_PATH = REPO_ROOT / "mlflow" / "experiments" / "experiments_manifest.json"
REGISTRY_PLAN_PATH = REPO_ROOT / "mlflow" / "registry" / "model_registry_plan.json"
SAMPLE_DATA_PATH = REPO_ROOT / "data" / "samples" / "model_training_samples.csv"

ALLOWED_STATUSES = {"candidate", "staging", "production", "retired", "data_gap"}
ALLOWED_TASK_TYPES = {"binary_classification", "forecasting", "anomaly_detection", "risk_scoring"}


def load_json(path: Path) -> dict[str, Any] | list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate() -> list[str]:
    issues: list[str] = []
    contracts = load_json(CONFIG_DIR / "airflow_dataset_contracts.json")
    portfolio = load_json(CONFIG_DIR / "model_portfolio.json")
    experiments = load_json(EXPERIMENTS_PATH)
    registry_plan = load_json(REGISTRY_PLAN_PATH)

    packages = {package["package_id"] for package in contracts["packages"]}
    models = portfolio.get("models", [])
    model_ids = [model["model_id"] for model in models]

    if len(model_ids) != len(set(model_ids)):
        issues.append("Model IDs must be unique")
    if len(models) < 8:
        issues.append("Portfolio should contain at least 8 model specs")

    experiment_model_ids = {experiment["model_id"] for experiment in experiments}
    registry_model_ids = {entry["model_id"] for entry in registry_plan}

    for model in models:
        model_id = model["model_id"]
        if model["status"] not in ALLOWED_STATUSES:
            issues.append(f"{model_id} has unsupported status {model['status']}")
        if model["task_type"] not in ALLOWED_TASK_TYPES:
            issues.append(f"{model_id} has unsupported task type {model['task_type']}")
        if model_id not in experiment_model_ids:
            issues.append(f"{model_id} is missing an experiment definition")
        if model_id not in registry_model_ids:
            issues.append(f"{model_id} is missing a registry plan")
        if not model.get("metric_gates"):
            issues.append(f"{model_id} has no metric gates")
        if not (MODEL_CARDS_DIR / f"{model_id}.md").exists():
            issues.append(f"{model_id} is missing a model card")
        if model["status"] == "data_gap":
            if model.get("upstream_packages"):
                issues.append(f"{model_id} data_gap model should not claim approved source packages")
            if not model.get("upstream_data_gaps"):
                issues.append(f"{model_id} needs upstream_data_gaps")
        else:
            for package_id in model.get("upstream_packages", []):
                if package_id not in packages:
                    issues.append(f"{model_id} references unknown package {package_id}")

    candidate_count = sum(1 for model in models if model["status"] == "candidate")
    data_gap_count = sum(1 for model in models if model["status"] == "data_gap")
    if candidate_count < 6:
        issues.append("Portfolio should include at least 6 candidate models")
    if data_gap_count < 2:
        issues.append("Portfolio should preserve supplier and energy data-gap models")
    if not SAMPLE_DATA_PATH.exists():
        issues.append("Sample training data is missing")

    return issues


def main() -> int:
    issues = validate()
    if issues:
        print("ML asset validation failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    portfolio = load_json(CONFIG_DIR / "model_portfolio.json")
    print(
        "ML asset validation passed: "
        f"{len(portfolio['models'])} models, "
        f"{len(load_json(EXPERIMENTS_PATH))} experiments, "
        f"{len(load_json(REGISTRY_PLAN_PATH))} registry entries"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
