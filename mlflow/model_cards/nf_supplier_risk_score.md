# Supplier Risk Score

Model ID: `nf_supplier_risk_score`

Registered model name: `NordForgeSupplierRiskScore`

Status: `data_gap`

Owner team: Procurement Analytics

## Business Purpose

Score suppliers for late deliveries, quality defects, and capacity risk.

## Target

`supplier_risk_score` at grain `supplier_material_month`.

## Source Data

- Data gap: supplier delivery history
- Data gap: quality defect claims
- Data gap: purchase order schedule lines

## Feature Groups

- supplier_otd
- quality_ppm
- material_criticality
- region_risk

## Metric Gates

- `spearman_corr`: 0.45
- `calibration_error`: 0.08

## Downstream Consumers

- Supplier Performance Review

## Approval Notes

Candidate models require data-quality validation, model card approval, registry review, and monitoring readiness before production use.
