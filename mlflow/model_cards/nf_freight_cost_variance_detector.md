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

## Monitoring Plan

Monitoring applies at model, carrier, lane-family, and monthly financial-close
levels.

### Monitored Signals

- Prediction volume by carrier and lane family
- Average predicted variance risk by carrier
- Cost-per-ton-km distribution drift
- Fuel surcharge percentage drift
- Route distance and chargeable-weight distribution drift
- Share of freight invoices routed to audit review
- Precision and false-positive rate after reviewed outcomes become available

### Provisional Drift Thresholds

| Signal | Warning | Critical |
| --- | ---: | ---: |
| Population Stability Index | `>= 0.10` | `>= 0.25` |
| Prediction volume change from trailing 30-day baseline | `> 25%` | `> 50%` |
| Median cost-per-ton-km change | `> 15%` | `> 30%` |
| Median fuel-surcharge percentage change | `> 10%` | `> 20%` |
| Audit-review share increase | `> 5 percentage points` | `> 10 percentage points` |
| Precision against approved metric gate | Within `0.05` of gate | Below gate by more than `0.05` |

These thresholds are provisional. Freight Audit and Transportation must approve
them after at least 30 days of representative historical runs.

### Notification And Response

- Warning: create a monitoring issue and notify Freight Audit within one
  business day.
- Critical: stop registry promotion, notify Freight Audit and Data Platform,
  and open an incident investigation.
- Repeated warning for three consecutive runs: treat as critical.
- Data-quality failure upstream: route to Great Expectations triage before
  investigating model drift.

Primary owner: Freight Audit and Transportation.

Technical owner: Logistics Analytics.

Escalation owner: NordForge Data Platform.

### Approval Status

- [ ] Historical baseline collected
- [ ] Freight Audit approves warning thresholds
- [ ] Freight Audit approves critical thresholds
- [ ] Notification routing tested
- [ ] Superset monitoring dataset confirmed

## Approval Notes

Candidate models require data-quality validation, model card approval, registry review, and monitoring readiness before production use.
