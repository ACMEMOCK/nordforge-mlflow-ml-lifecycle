# Scrap Loss Propensity

Model ID: `nf_scrap_loss_propensity`

Registered model name: `NordForgeScrapLossPropensity`

Status: `candidate`

Owner team: Industrial Inventory Control

## Business Purpose

Predict production movements and lots that are likely to become scrap or loss events.

## Target

`scrap_loss_flag` at grain `production_movement`.

## Source Data

- `acda4413_inventory_movements`: Inventory movement ledger, warehouse/bin/material masters, transfers, production consumption, scrap/loss, and aging risk.

## Feature Groups

- movement_type
- material_type
- stock_age
- reference_document

## Metric Gates

- `roc_auc`: 0.74
- `f1_score`: 0.58
- `precision`: 0.6

## Downstream Consumers

- Production Loss Review
- Inventory Health Daily

## Approval Notes

Candidate models require data-quality validation, model card approval, registry review, and monitoring readiness before production use.
