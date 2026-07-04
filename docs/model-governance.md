# Model Governance

## Promotion Requirements

A model cannot move beyond candidate status until:

- Source packages are validated by Great Expectations.
- Feature lineage is documented in OpenMetadata.
- Model card is complete.
- Metric gates meet or exceed portfolio thresholds.
- Bias, drift, and business-risk notes are reviewed.
- Rollback owner is assigned.

## Review Gates

| Gate | Owner |
| --- | --- |
| Data quality readiness | Data Platform |
| Feature lineage and ownership | Data Governance |
| Business metric approval | Domain owner |
| Model performance | Data Science |
| Dashboard monitoring | Enterprise Analytics |

## Registry Policy

The generated `mlflow/registry/model_registry_plan.json` is a dry-run registry plan. Production registration should be executed only after a model-promotion issue is approved.

## Monitoring Expectations

Every production model should have:

- Feature freshness checks
- Prediction volume checks
- Drift thresholds
- Business KPI backtesting
- Owner notification path
- Retirement criteria

## Candidate Promotion Workflow

Candidate model promotion requires evidence from four areas:

- Data Science confirms the experiment run, metric gates, and model card.
- Data Platform confirms Airflow and MLflow run reproducibility.
- Data Governance confirms source lineage and ownership.
- The domain owner confirms the business decision can safely use the model output.

Promotion requests should include the MLflow run artifact, model card link, observed metrics, rollback owner, and monitoring plan. Models must remain at candidate status until all required reviewers approve the promotion issue.

## Data Gap Roadmap

Two models remain intentionally blocked until new source packages exist:

- `nf_supplier_risk_score`: requires supplier delivery history, purchase order schedule lines, supplier quality claims, and supplier master enrichment.
- `nf_energy_anomaly_detection`: requires plant energy meter telemetry, production-line runtime, production volume, and weather-normalization data.

These models should stay in `data_gap` status until source contracts are approved, Great Expectations checks are defined, and ownership is assigned in OpenMetadata.
