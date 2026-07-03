# Freight Cost Variance Detector

Model ID: `nf_freight_cost_variance_detector`

Registered model name: `NordForgeFreightCostVarianceDetector`

Status: `candidate`

Owner team: Freight Audit and Transportation

## Business Purpose

Detect freight invoices and lanes with abnormal cost variance before accrual close.

## Target

`freight_cost_variance_alert` at grain `freight_invoice_line`.

## Source Data

- `acsa2637_freight_transportation`: Freight cost detail, invoices, rate cards, accessorial review, accruals, and emissions reporting.
- `acda7982_logistics_analytics`: Delivery OTIF, carrier SLA, route lane performance, cut-off compliance, and recovery actions.

## Feature Groups

- carrier
- lane_family
- weight_distance
- rate_card
- fuel_surcharge

## Metric Gates

- `precision`: 0.7
- `f1_score`: 0.61
- `roc_auc`: 0.77

## Downstream Consumers

- Freight Cost and Audit
- Route Cost Scorecard

## Approval Notes

Candidate models require data-quality validation, model card approval, registry review, and monitoring readiness before production use.
