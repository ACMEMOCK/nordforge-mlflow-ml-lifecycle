# Inventory Aging Risk

Model ID: `nf_inventory_aging_risk`

Registered model name: `NordForgeInventoryAgingRisk`

Status: `candidate`

Owner team: Industrial Inventory Control

## Business Purpose

Identify lots likely to age into excess, blocked, or slow-moving inventory.

## Target

`aging_risk_flag` at grain `warehouse_sku_lot`.

## Source Data

- `acda4413_inventory_movements`: Inventory movement ledger, warehouse/bin/material masters, transfers, production consumption, scrap/loss, and aging risk.
- `accu1533_customer_availability`: Customer-facing stock availability, ATP constraints, blocked-stock release planning, and promise queue orchestration.

## Feature Groups

- stock_age
- movement_velocity
- warehouse_zone
- material_family

## Metric Gates

- `roc_auc`: 0.76
- `f1_score`: 0.6
- `precision`: 0.62

## Downstream Consumers

- Inventory Health Daily
- Working Capital Review

## Approval Notes

Candidate models require data-quality validation, model card approval, registry review, and monitoring readiness before production use.
