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
