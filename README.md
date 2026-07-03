# NordForge MLflow ML Lifecycle

MLflow lifecycle repository for NordForge Industrial Group.

This repository complements the NordForge data platform:

- `nordforge-airflow-orchestration`: schedules ERP and operations data flows.
- `nordforge-great-expectations-quality`: validates source packages and BI marts.
- `nordforge-openmetadata-governance`: catalogs ownership, lineage, policy, and certification.
- `nordforge-superset-bi`: publishes operational and executive dashboards.
- `nordforge-mlflow-ml-lifecycle`: tracks experiments, model candidates, model cards, registry plans, and deployment readiness.

## What This Repository Provides

- Local MLflow tracking-server scaffold
- Generated model portfolio aligned to existing NordForge data products
- Baseline experiment runner with dry-run fallback
- Model registry and approval-plan assets
- Model cards for late-delivery, demand, scrap, inventory, freight, ATP, supplier-risk, and energy-anomaly use cases
- CI validation, unit tests, issue templates, seed issues, seed PRs, and project-board guidance

## Model Portfolio

| Model | Purpose | Status |
| --- | --- | --- |
| `nf_late_delivery_risk` | Predict late delivery risk across order, freight, and logistics data | candidate |
| `nf_customer_promise_risk` | Predict customer promise risk from ATP and blocked-stock patterns | candidate |
| `nf_inventory_aging_risk` | Predict lots likely to age into operational risk | candidate |
| `nf_scrap_loss_propensity` | Predict production movements likely to become scrap/loss events | candidate |
| `nf_demand_forecast_segment` | Forecast short-term demand by customer segment and SKU family | candidate |
| `nf_freight_cost_variance_detector` | Detect freight cost variance and invoice audit risk | candidate |
| `nf_supplier_risk_score` | Score supplier delivery and quality risk | data_gap |
| `nf_energy_anomaly_detection` | Detect plant energy anomalies | data_gap |

The `data_gap` models are intentionally present as roadmap items because the current generated NordForge packages do not yet include supplier performance or plant energy telemetry extracts.

## Repository Layout

```text
.
|-- config/
|   |-- airflow_dataset_contracts.json
|   |-- great_expectations_quality_manifest.json
|   |-- model_portfolio.json
|   |-- openmetadata_governance_manifest.json
|   `-- superset_bi_catalog.json
|-- data/samples/
|-- docs/
|-- mlflow/
|   |-- experiments/
|   |-- model_cards/
|   |-- registry/
|   `-- runs/
|-- pipelines/
|-- scripts/
|-- src/nordforge_ml/
|-- tests/
|-- docker-compose.yaml
|-- Makefile
`-- requirements.txt
```

## Quick Start

Generate ML lifecycle assets:

```bash
python scripts/generate_ml_assets.py
```

Validate assets:

```bash
python scripts/validate_ml_assets.py
python -m unittest discover -s tests -p "test*.py" -v
```

Run a dry-run baseline experiment:

```bash
python pipelines/train_model.py --model-id nf_late_delivery_risk --dry-run
```

Start local MLflow:

```bash
docker compose up
```

Open:

```text
http://localhost:5000
```

## MLflow Notes

This repository follows the current MLflow pattern of experiment tracking, run metadata, artifacts, tracking server, and model registry planning. It is intentionally local-first for demonstration, with production notes for Postgres-backed tracking and managed artifact storage.

Official references:

- https://github.com/mlflow/mlflow
- https://mlflow.org/docs/latest/ml/tracking/
- https://mlflow.org/docs/latest/ml/model-registry/
- https://mlflow.org/docs/latest/self-hosting/architecture/tracking-server/
