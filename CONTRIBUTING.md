# Contributing

## Workflow

1. Create a branch.
2. Update model specs, scripts, docs, or tests.
3. Regenerate assets.
4. Validate locally.
5. Open a pull request using the template.

## Required Checks

```bash
python scripts/generate_ml_assets.py
python scripts/validate_ml_assets.py
python pipelines/train_model.py --model-id nf_late_delivery_risk --dry-run
python -m unittest discover -s tests -p "test*.py" -v
```

## Model Changes

Every model change must include owner, source packages, feature groups, target, metric gates, model card impact, and registry impact.
