# Seed Issues

Use these as copy-ready GitHub issues after uploading the repository.

## Issue 1 - Wire late-delivery baseline experiment into Airflow

Labels: `type: platform-task`, `area: mlflow`, `domain: logistics`, `priority: high`

Milestone: `M2 - Experiment tracking readiness`

Body:

The MLflow repo can run `nf_late_delivery_risk` in dry-run mode. The next step is to schedule a weekly baseline experiment from Airflow after Great Expectations validates order, logistics, and freight inputs.

Acceptance criteria:

- Airflow task calls `pipelines/train_model.py --model-id nf_late_delivery_risk`.
- Task logs run artifact path.
- Failed quality gates block training.
- Experiment name matches `/NordForge/IndustrialML/nf_late_delivery_risk`.

## Issue 2 - Promote customer promise risk to candidate review

Labels: `type: model-promotion`, `area: registry`, `domain: customer-availability`, `priority: high`

Milestone: `M3 - Registry and model cards`

Body:

`nf_customer_promise_risk` is aligned to ATP and customer promise data. The model card and registry plan should be reviewed before the Customer Availability Desk uses it for intervention prioritization.

Acceptance criteria:

- Model card reviewed by Customer Availability Desk.
- Metric gates confirmed.
- OpenMetadata lineage path documented.
- Candidate alias approved or rejected.

## Issue 3 - Supplier risk model blocked by missing procurement package

Labels: `type: data-gap`, `blocked`

Milestone: `M1 - Candidate model portfolio`

Body:

`nf_supplier_risk_score` is a valid business use case, but current generated NordForge packages do not include supplier delivery history, purchase order schedule lines, or supplier quality claims.

Acceptance criteria:

- Keep model status as `data_gap`.
- Define required source package.
- Link to future procurement data generation work.
- Do not schedule training until upstream package exists.

## Issue 4 - Add drift monitoring plan for freight cost variance detector

Labels: `type: platform-task`, `area: monitoring`, `domain: logistics`

Milestone: `M4 - Monitoring and production gates`

Body:

`nf_freight_cost_variance_detector` needs monitoring before registry promotion because freight cost and fuel surcharge patterns can drift quickly by carrier and lane.

Acceptance criteria:

- Define feature drift fields.
- Define alert thresholds for cost-per-ton-km and fuel surcharge.
- Define owner notification path.
- Add monitoring notes to the model card.

## Issue 5 - Add registry approval checklist to model promotion template

Labels: `type: platform-task`, `area: registry`, `good first issue`

Milestone: `M3 - Registry and model cards`

Body:

The model-promotion issue template should ask for model-card review, data-quality evidence, and rollback owner before candidate promotion.

Acceptance criteria:

- Template includes model card checkbox.
- Template includes data-quality checkbox.
- Template includes rollback owner.
- Template includes monitoring readiness.

## Issue 6 - Energy anomaly model requires telemetry data contract

Labels: `type: data-gap`, `blocked`

Milestone: `M1 - Candidate model portfolio`

Body:

`nf_energy_anomaly_detection` is included as a roadmap model, but production feasibility depends on plant energy meter telemetry and production-line runtime data.

Acceptance criteria:

- Keep model status as `data_gap`.
- Define expected source grain.
- Identify Sustainability Analytics owner.
- Add future data contract placeholder.
