from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from nordforge_ml.baseline import write_json
from nordforge_ml.portfolio import load_portfolio, model_by_id


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a dry-run model registration plan.")
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--portfolio", default="config/model_portfolio.json")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    portfolio = load_portfolio(REPO_ROOT / args.portfolio)
    model = model_by_id(portfolio, args.model_id)
    run_artifact = REPO_ROOT / "mlflow" / "runs" / f"latest_{args.model_id}_run.json"
    metrics = {}
    if run_artifact.exists():
        metrics = json.loads(run_artifact.read_text(encoding="utf-8")).get("metrics", {})

    plan = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "execute": args.execute,
        "model_id": model["model_id"],
        "registered_model_name": model["registered_model_name"],
        "requested_alias": "candidate",
        "owner_team": model["owner_team"],
        "metric_gates": model["metric_gates"],
        "observed_metrics": metrics,
        "approval_required_from": [model["owner_team"], "Data Science", "Data Governance"],
        "notes": "Execute mode intentionally left as a controlled production operation.",
    }
    output_path = REPO_ROOT / "mlflow" / "registry" / f"{args.model_id}_registration_request.json"
    write_json(output_path, plan)
    print(f"Registration plan written to {output_path}")
    if args.execute:
        print("Execute mode is documented but not enabled in this starter repository.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
