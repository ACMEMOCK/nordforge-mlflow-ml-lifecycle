# Demand Forecast By Segment

Model ID: `nf_demand_forecast_segment`

Registered model name: `NordForgeDemandForecastSegment`

Status: `candidate`

Owner team: Commercial Operations

## Business Purpose

Forecast near-term demand by customer segment, SKU family, and allocation segment.

## Target

`next_14_day_order_qty` at grain `segment_sku_family_day`.

## Source Data

- `accu1932_order_fulfillment`: Daily sales order fulfillment, ATP, delivery, backlog, and credit-block orchestration.
- `acsa2026_contract_customer`: EMEA contract pricing, condition records, rebates, renewal pipeline, and discount audit workflow.
- `accu1533_customer_availability`: Customer-facing stock availability, ATP constraints, blocked-stock release planning, and promise queue orchestration.

## Feature Groups

- order_history
- pricing_terms
- allocation_segment
- service_atp

## Metric Gates

- `wmape`: 0.18
- `bias`: 0.04

## Downstream Consumers

- Executive Revenue Outlook
- Customer Promise Daily

## Approval Notes

Candidate models require data-quality validation, model card approval, registry review, and monitoring readiness before production use.
