from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO_PATH = REPO_ROOT / "config" / "model_portfolio.json"


class MlLifecycleAssetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            [sys.executable, "scripts/generate_ml_assets.py"],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        cls.portfolio = json.loads(PORTFOLIO_PATH.read_text(encoding="utf-8"))

    def test_portfolio_has_expected_shape(self) -> None:
        models = self.portfolio["models"]
        self.assertEqual(len(models), 8)
        self.assertEqual(sum(1 for model in models if model["status"] == "candidate"), 6)
        self.assertEqual(sum(1 for model in models if model["status"] == "data_gap"), 2)

    def test_late_delivery_model_uses_existing_nordforge_packages(self) -> None:
        model = next(model for model in self.portfolio["models"] if model["model_id"] == "nf_late_delivery_risk")
        self.assertIn("accu1932_order_fulfillment", model["upstream_packages"])
        self.assertIn("acda7982_logistics_analytics", model["upstream_packages"])
        self.assertIn("acsa2637_freight_transportation", model["upstream_packages"])
        self.assertGreaterEqual(model["metric_gates"]["roc_auc"], 0.78)

    def test_data_gap_models_are_explicit(self) -> None:
        gap_models = [model for model in self.portfolio["models"] if model["status"] == "data_gap"]
        gap_ids = {model["model_id"] for model in gap_models}
        self.assertEqual(gap_ids, {"nf_supplier_risk_score", "nf_energy_anomaly_detection"})
        for model in gap_models:
            self.assertTrue(model["upstream_data_gaps"])

    def test_dry_run_training_writes_artifact(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "pipelines/train_model.py",
                "--model-id",
                "nf_late_delivery_risk",
                "--dry-run",
            ],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((REPO_ROOT / "mlflow" / "runs" / "latest_nf_late_delivery_risk_run.json").exists())


if __name__ == "__main__":
    unittest.main()
