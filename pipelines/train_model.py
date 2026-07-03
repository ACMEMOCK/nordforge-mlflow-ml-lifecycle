from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from nordforge_ml.baseline import load_sample_rows, run_baseline, write_json
from nordforge_ml.portfolio import load_portfolio, model_by_id


def log_with_mlflow(model: dict, result: dict, tracking_uri: str) -> bool:
    try:
        import mlflow
    except ImportError:
        return False

    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(f"/NordForge/IndustrialML/{model['model_id']}")
    with mlflow.start_run(run_name=f"baseline-{model['model_id']}"):
        mlflow.log_param("model_id", model["model_id"])
        mlflow.log_param("task_type", model["task_type"])
        mlflow.log_param("owner_team", model["owner_team"])
        mlflow.log_param("upstream_packages", ",".join(model.get("upstream_packages", [])))
        for metric, value in result["metrics"].items():
            mlflow.log_metric(metric, value)
        card_path = REPO_ROOT / "mlflow" / "model_cards" / f"{model['model_id']}.md"
        if card_path.exists():
            mlflow.log_artifact(str(card_path), artifact_path="model_card")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a NordForge baseline model experiment.")
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--portfolio", default="config/model_portfolio.json")
    parser.add_argument("--sample-data", default="data/samples/model_training_samples.csv")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    portfolio = load_portfolio(REPO_ROOT / args.portfolio)
    model = model_by_id(portfolio, args.model_id)
    if model["status"] == "data_gap":
        print(f"{args.model_id} is a data-gap model and cannot train yet")
        return 1

    rows = load_sample_rows(REPO_ROOT / args.sample_data, args.model_id)
    result = run_baseline(model, rows)
    result["generated_at"] = datetime.now(timezone.utc).isoformat()
    result["dry_run"] = bool(args.dry_run)
    result["tracking_uri"] = os.environ.get("MLFLOW_TRACKING_URI", "http://localhost:5000")

    logged = False
    if not args.dry_run:
        logged = log_with_mlflow(model, result, result["tracking_uri"])
    result["logged_to_mlflow"] = logged

    output_path = REPO_ROOT / "mlflow" / "runs" / f"latest_{args.model_id}_run.json"
    write_json(output_path, result)
    print(f"Baseline experiment complete for {args.model_id}")
    print(f"Metrics: {result['metrics']}")
    print(f"Run artifact: {output_path}")
    if not logged and not args.dry_run:
        print("MLflow package not available; wrote dry-run artifact instead")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
