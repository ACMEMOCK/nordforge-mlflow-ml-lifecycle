from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = REPO_ROOT / "config"
MLFLOW_DIR = REPO_ROOT / "mlflow"
MODEL_CARDS_DIR = MLFLOW_DIR / "model_cards"
SAMPLE_DATA_PATH = REPO_ROOT / "data" / "samples" / "model_training_samples.csv"


MODEL_SPECS: list[dict[str, Any]] = [
    {
        "model_id": "nf_late_delivery_risk",
        "name": "Late Delivery Risk",
        "registered_model_name": "NordForgeLateDeliveryRisk",
        "task_type": "binary_classification",
        "status": "candidate",
        "criticality": "high",
        "owner_team": "Logistics Analytics",
        "business_purpose": "Predict order and shipment lines likely to miss promised delivery windows.",
        "target": "late_delivery_flag",
        "primary_entity": "shipment_or_order_line",
        "upstream_packages": ["accu1932_order_fulfillment", "acda7982_logistics_analytics", "acsa2637_freight_transportation"],
        "downstream_dashboards": ["Logistics OTIF Control Tower", "Executive Operations Scorecard"],
        "feature_groups": ["order_promise", "freight_lane", "carrier_performance", "warehouse_capacity"],
        "metric_gates": {"roc_auc": 0.78, "f1_score": 0.62, "precision": 0.64},
    },
    {
        "model_id": "nf_customer_promise_risk",
        "name": "Customer Promise Risk",
        "registered_model_name": "NordForgeCustomerPromiseRisk",
        "task_type": "binary_classification",
        "status": "candidate",
        "criticality": "high",
        "owner_team": "Customer Availability Desk",
        "business_purpose": "Prioritize customer orders and ATP positions that need service intervention.",
        "target": "promise_risk_flag",
        "primary_entity": "warehouse_sku_lot_segment",
        "upstream_packages": ["accu1533_customer_availability", "accu1932_order_fulfillment"],
        "downstream_dashboards": ["Customer Promise Daily", "Service Escalation Workbench"],
        "feature_groups": ["atp_position", "blocked_stock", "allocation_segment", "service_history"],
        "metric_gates": {"roc_auc": 0.80, "f1_score": 0.66, "precision": 0.68},
    },
    {
        "model_id": "nf_inventory_aging_risk",
        "name": "Inventory Aging Risk",
        "registered_model_name": "NordForgeInventoryAgingRisk",
        "task_type": "binary_classification",
        "status": "candidate",
        "criticality": "medium",
        "owner_team": "Industrial Inventory Control",
        "business_purpose": "Identify lots likely to age into excess, blocked, or slow-moving inventory.",
        "target": "aging_risk_flag",
        "primary_entity": "warehouse_sku_lot",
        "upstream_packages": ["acda4413_inventory_movements", "accu1533_customer_availability"],
        "downstream_dashboards": ["Inventory Health Daily", "Working Capital Review"],
        "feature_groups": ["stock_age", "movement_velocity", "warehouse_zone", "material_family"],
        "metric_gates": {"roc_auc": 0.76, "f1_score": 0.60, "precision": 0.62},
    },
    {
        "model_id": "nf_scrap_loss_propensity",
        "name": "Scrap Loss Propensity",
        "registered_model_name": "NordForgeScrapLossPropensity",
        "task_type": "binary_classification",
        "status": "candidate",
        "criticality": "medium",
        "owner_team": "Industrial Inventory Control",
        "business_purpose": "Predict production movements and lots that are likely to become scrap or loss events.",
        "target": "scrap_loss_flag",
        "primary_entity": "production_movement",
        "upstream_packages": ["acda4413_inventory_movements"],
        "downstream_dashboards": ["Production Loss Review", "Inventory Health Daily"],
        "feature_groups": ["movement_type", "material_type", "stock_age", "reference_document"],
        "metric_gates": {"roc_auc": 0.74, "f1_score": 0.58, "precision": 0.60},
    },
    {
        "model_id": "nf_demand_forecast_segment",
        "name": "Demand Forecast By Segment",
        "registered_model_name": "NordForgeDemandForecastSegment",
        "task_type": "forecasting",
        "status": "candidate",
        "criticality": "medium",
        "owner_team": "Commercial Operations",
        "business_purpose": "Forecast near-term demand by customer segment, SKU family, and allocation segment.",
        "target": "next_14_day_order_qty",
        "primary_entity": "segment_sku_family_day",
        "upstream_packages": ["accu1932_order_fulfillment", "acsa2026_contract_customer", "accu1533_customer_availability"],
        "downstream_dashboards": ["Executive Revenue Outlook", "Customer Promise Daily"],
        "feature_groups": ["order_history", "pricing_terms", "allocation_segment", "service_atp"],
        "metric_gates": {"wmape": 0.18, "bias": 0.04},
    },
    {
        "model_id": "nf_freight_cost_variance_detector",
        "name": "Freight Cost Variance Detector",
        "registered_model_name": "NordForgeFreightCostVarianceDetector",
        "task_type": "anomaly_detection",
        "status": "candidate",
        "criticality": "medium",
        "owner_team": "Freight Audit and Transportation",
        "business_purpose": "Detect freight invoices and lanes with abnormal cost variance before accrual close.",
        "target": "freight_cost_variance_alert",
        "primary_entity": "freight_invoice_line",
        "upstream_packages": ["acsa2637_freight_transportation", "acda7982_logistics_analytics"],
        "downstream_dashboards": ["Freight Cost and Audit", "Route Cost Scorecard"],
        "feature_groups": ["carrier", "lane_family", "weight_distance", "rate_card", "fuel_surcharge"],
        "metric_gates": {"precision": 0.70, "f1_score": 0.61, "roc_auc": 0.77},
    },
    {
        "model_id": "nf_supplier_risk_score",
        "name": "Supplier Risk Score",
        "registered_model_name": "NordForgeSupplierRiskScore",
        "task_type": "risk_scoring",
        "status": "data_gap",
        "criticality": "medium",
        "owner_team": "Procurement Analytics",
        "business_purpose": "Score suppliers for late deliveries, quality defects, and capacity risk.",
        "target": "supplier_risk_score",
        "primary_entity": "supplier_material_month",
        "upstream_packages": [],
        "upstream_data_gaps": ["supplier delivery history", "quality defect claims", "purchase order schedule lines"],
        "downstream_dashboards": ["Supplier Performance Review"],
        "feature_groups": ["supplier_otd", "quality_ppm", "material_criticality", "region_risk"],
        "metric_gates": {"spearman_corr": 0.45, "calibration_error": 0.08},
    },
    {
        "model_id": "nf_energy_anomaly_detection",
        "name": "Energy Anomaly Detection",
        "registered_model_name": "NordForgeEnergyAnomalyDetection",
        "task_type": "anomaly_detection",
        "status": "data_gap",
        "criticality": "medium",
        "owner_team": "Sustainability Analytics",
        "business_purpose": "Detect abnormal plant energy consumption relative to production and weather context.",
        "target": "energy_anomaly_flag",
        "primary_entity": "plant_line_hour",
        "upstream_packages": [],
        "upstream_data_gaps": ["plant energy meter telemetry", "production line schedules", "weather-normalization feed"],
        "downstream_dashboards": ["Sustainability Energy Review"],
        "feature_groups": ["meter_readings", "line_runtime", "production_volume", "weather"],
        "metric_gates": {"precision": 0.68, "recall": 0.55},
    },
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any] | list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def package_index(contracts: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {package["package_id"]: package for package in contracts["packages"]}


def model_card(model: dict[str, Any], packages: dict[str, dict[str, Any]]) -> str:
    source_lines = []
    for package_id in model.get("upstream_packages", []):
        package = packages[package_id]
        source_lines.append(f"- `{package_id}`: {package['business_purpose']}")
    if model.get("upstream_data_gaps"):
        source_lines.extend(f"- Data gap: {gap}" for gap in model["upstream_data_gaps"])

    gates = "\n".join(f"- `{metric}`: {value}" for metric, value in model["metric_gates"].items())
    sources = "\n".join(source_lines) if source_lines else "- No approved source packages yet."
    dashboards = "\n".join(f"- {dashboard}" for dashboard in model.get("downstream_dashboards", []))

    return f"""# {model['name']}

Model ID: `{model['model_id']}`

Registered model name: `{model['registered_model_name']}`

Status: `{model['status']}`

Owner team: {model['owner_team']}

## Business Purpose

{model['business_purpose']}

## Target

`{model['target']}` at grain `{model['primary_entity']}`.

## Source Data

{sources}

## Feature Groups

{chr(10).join(f"- {feature}" for feature in model['feature_groups'])}

## Metric Gates

{gates}

## Downstream Consumers

{dashboards}

## Approval Notes

Candidate models require data-quality validation, model card approval, registry review, and monitoring readiness before production use.
"""


def sample_rows(models: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for model in models:
        if model["status"] == "data_gap":
            continue
        for index in range(1, 13):
            rows.append(
                {
                    "model_id": model["model_id"],
                    "entity_id": f"{model['model_id']}-sample-{index:03d}",
                    "snapshot_date": f"2026-06-{10 + index:02d}",
                    "feature_group_count": len(model["feature_groups"]),
                    "upstream_package_count": len(model.get("upstream_packages", [])),
                    "synthetic_signal": round((index * 7 % 19) / 18, 4),
                    "target_value": 1 if index % 4 == 0 else 0,
                }
            )
    return rows


def write_sample_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "model_id",
        "entity_id",
        "snapshot_date",
        "feature_group_count",
        "upstream_package_count",
        "synthetic_signal",
        "target_value",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    contracts = load_json(CONFIG_DIR / "airflow_dataset_contracts.json")
    bi_catalog = load_json(CONFIG_DIR / "superset_bi_catalog.json")
    quality_manifest = load_json(CONFIG_DIR / "great_expectations_quality_manifest.json")
    packages = package_index(contracts)

    for folder in [MODEL_CARDS_DIR, MLFLOW_DIR / "experiments", MLFLOW_DIR / "registry"]:
        folder.mkdir(parents=True, exist_ok=True)
        for path in folder.glob("*.json"):
            path.unlink()
        for path in folder.glob("*.md"):
            path.unlink()

    generated_at = datetime.now(timezone.utc).isoformat()
    experiments = []
    registry_plan = []
    for model in MODEL_SPECS:
        experiment_name = f"/NordForge/IndustrialML/{model['model_id']}"
        experiments.append(
            {
                "experiment_name": experiment_name,
                "model_id": model["model_id"],
                "owner_team": model["owner_team"],
                "artifact_location": f"mlflow-artifacts:/nordforge/{model['model_id']}",
                "tags": {
                    "nordforge.domain": ",".join(model.get("upstream_packages", []) or model.get("upstream_data_gaps", [])),
                    "nordforge.status": model["status"],
                    "nordforge.criticality": model["criticality"],
                },
            }
        )
        registry_plan.append(
            {
                "registered_model_name": model["registered_model_name"],
                "model_id": model["model_id"],
                "initial_alias": "candidate" if model["status"] == "candidate" else "data-gap",
                "approval_required_from": [model["owner_team"], "Data Science", "Data Governance"],
                "promotion_gates": model["metric_gates"],
                "monitoring_required": model["status"] == "candidate",
            }
        )
        (MODEL_CARDS_DIR / f"{model['model_id']}.md").write_text(model_card(model, packages), encoding="utf-8")

    portfolio = {
        "portfolio_version": "2026.07.03",
        "generated_at": generated_at,
        "company": contracts["company"],
        "repository": "nordforge-mlflow-ml-lifecycle",
        "upstream_repositories": [
            "nordforge-airflow-orchestration",
            "nordforge-great-expectations-quality",
            "nordforge-openmetadata-governance",
            "nordforge-superset-bi",
        ],
        "source_contract_summary": {
            "packages": len(contracts["packages"]),
            "quality_suites": quality_manifest["summary"]["expectation_suites"],
            "bi_datasets": len(bi_catalog.get("datasets", [])),
        },
        "models": MODEL_SPECS,
    }

    write_json(CONFIG_DIR / "model_portfolio.json", portfolio)
    write_json(MLFLOW_DIR / "experiments" / "experiments_manifest.json", experiments)
    write_json(MLFLOW_DIR / "registry" / "model_registry_plan.json", registry_plan)
    write_sample_csv(SAMPLE_DATA_PATH, sample_rows(MODEL_SPECS))

    print(f"Generated {len(MODEL_SPECS)} model specs")
    print(f"Generated {len(experiments)} experiment definitions")
    print(f"Generated {len(registry_plan)} registry plan entries")
    print(f"Generated sample rows: {sum(1 for model in MODEL_SPECS if model['status'] != 'data_gap') * 12}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
