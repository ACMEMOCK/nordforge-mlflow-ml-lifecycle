# Customer Promise Risk

Model ID: `nf_customer_promise_risk`

Registered model name: `NordForgeCustomerPromiseRisk`

Status: `candidate`

Owner team: Customer Availability Desk

## Business Purpose

Prioritize customer orders and ATP positions that need service intervention.

## Target

`promise_risk_flag` at grain `warehouse_sku_lot_segment`.

## Source Data

- `accu1533_customer_availability`: Customer-facing stock availability, ATP constraints, blocked-stock release planning, and promise queue orchestration.
- `accu1932_order_fulfillment`: Daily sales order fulfillment, ATP, delivery, backlog, and credit-block orchestration.

## Feature Groups

- atp_position
- blocked_stock
- allocation_segment
- service_history

## Metric Gates

- `roc_auc`: 0.8
- `f1_score`: 0.66
- `precision`: 0.68

## Downstream Consumers

- Customer Promise Daily
- Service Escalation Workbench

## Approval Notes

Candidate models require data-quality validation, model card approval, registry review, and monitoring readiness before production use.
