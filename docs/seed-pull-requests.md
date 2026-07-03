# Seed Pull Requests

Use these to create realistic GitHub history.

## PR 1 - Bootstrap MLflow lifecycle repository

Suggested branch: `feature/bootstrap-mlflow-lifecycle`

Status: merge after upload

Body:

Bootstraps the NordForge ML lifecycle repository.

Includes:

- MLflow tracking-server scaffold
- Generated model portfolio
- Experiment and registry manifests
- Model cards
- Baseline dry-run training pipeline
- CI, tests, issue templates, seed docs, and governance runbooks

Validation:

- `python scripts/generate_ml_assets.py`
- `python scripts/validate_ml_assets.py`
- `python pipelines/train_model.py --model-id nf_late_delivery_risk --dry-run`
- `python -m unittest discover -s tests -p "test*.py" -v`

## PR 2 - Add registry checklist to model promotion template

Suggested branch: `feature/model-promotion-checklist`

Status: merge

Related issue: `Closes #<issue-number>`

Suggested change:

Edit `.github/ISSUE_TEMPLATE/model_promotion.yml` and add checklist prompts for model card, data quality, rollback owner, and monitoring readiness.

## PR 3 - Document supplier and energy data gaps

Suggested branch: `docs/data-gap-roadmap`

Status: leave open

Related issues: `Related to #<supplier-risk issue>` and `Related to #<energy issue>`

Suggested change:

Edit `docs/model-governance.md` or add a new data-gap section explaining why supplier-risk and energy-anomaly models are not trainable yet.

## PR 4 - Add freight drift monitoring plan

Suggested branch: `feature/freight-drift-monitoring-plan`

Status: draft

Related issue: `Related to #<freight monitoring issue>`

Suggested change:

Add monitoring thresholds to `mlflow/model_cards/nf_freight_cost_variance_detector.md` and update `docs/model-governance.md`.
