# Runbook

## Generate Assets

```bash
python scripts/generate_ml_assets.py
```

## Validate Assets

```bash
python scripts/validate_ml_assets.py
python -m unittest discover -s tests -p "test*.py" -v
```

## Run Baseline Experiment

```bash
python pipelines/train_model.py --model-id nf_late_delivery_risk --dry-run
```

Without `--dry-run`, the script attempts to log to MLflow using `MLFLOW_TRACKING_URI`. If the MLflow package is not installed, it writes a local run artifact instead.

## Create Registry Plan

```bash
python scripts/register_model_candidate.py --model-id nf_late_delivery_risk
```

## Start Local MLflow UI

```bash
docker compose up
```

Open `http://localhost:5000`.

## Incident Triage

| Symptom | First check |
| --- | --- |
| Experiment missing | Confirm `config/model_portfolio.json` and experiment manifest were generated |
| Metrics below gate | Compare sample data, model card, and training run artifact |
| Model references unknown package | Check copied Airflow dataset contracts |
| Data-gap model selected for training | Confirm source packages exist before changing status |
| Registry plan missing | Run `scripts/generate_ml_assets.py` again |
