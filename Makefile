.PHONY: generate validate test train dry-run registry clean

PYTHON ?= python

generate:
	$(PYTHON) scripts/generate_ml_assets.py

validate:
	$(PYTHON) scripts/validate_ml_assets.py

test:
	$(PYTHON) -m unittest discover -s tests -p "test*.py" -v

train:
	$(PYTHON) pipelines/train_model.py --model-id nf_late_delivery_risk

dry-run:
	$(PYTHON) pipelines/train_model.py --model-id nf_late_delivery_risk --dry-run

registry:
	$(PYTHON) scripts/register_model_candidate.py --model-id nf_late_delivery_risk

clean:
	$(PYTHON) scripts/clean_generated_artifacts.py
