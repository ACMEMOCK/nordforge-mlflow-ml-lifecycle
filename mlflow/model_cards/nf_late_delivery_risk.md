# Late Delivery Risk

Model ID: `nf_late_delivery_risk`

Registered model name: `NordForgeLateDeliveryRisk`

Status: `candidate`

Owner team: Logistics Analytics

## Business Purpose

Predict order and shipment lines likely to miss promised delivery windows.

## Target

`late_delivery_flag` at grain `shipment_or_order_line`.

## Source Data

- `accu1932_order_fulfillment`: Daily sales order fulfillment, ATP, delivery, backlog, and credit-block orchestration.
- `acda7982_logistics_analytics`: Delivery OTIF, carrier SLA, route lane performance, cut-off compliance, and recovery actions.
- `acsa2637_freight_transportation`: Freight cost detail, invoices, rate cards, accessorial review, accruals, and emissions reporting.

## Feature Groups

- order_promise
- freight_lane
- carrier_performance
- warehouse_capacity

## Metric Gates

- `roc_auc`: 0.78
- `f1_score`: 0.62
- `precision`: 0.64

## Downstream Consumers

- Logistics OTIF Control Tower
- Executive Operations Scorecard

## Approval Notes

Candidate models require data-quality validation, model card approval, registry review, and monitoring readiness before production use.
