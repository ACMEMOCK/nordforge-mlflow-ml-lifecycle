# Energy Anomaly Detection

Model ID: `nf_energy_anomaly_detection`

Registered model name: `NordForgeEnergyAnomalyDetection`

Status: `data_gap`

Owner team: Sustainability Analytics

## Business Purpose

Detect abnormal plant energy consumption relative to production and weather context.

## Target

`energy_anomaly_flag` at grain `plant_line_hour`.

## Source Data

- Data gap: plant energy meter telemetry
- Data gap: production line schedules
- Data gap: weather-normalization feed

## Feature Groups

- meter_readings
- line_runtime
- production_volume
- weather

## Metric Gates

- `precision`: 0.68
- `recall`: 0.55

## Downstream Consumers

- Sustainability Energy Review

## Approval Notes

Candidate models require data-quality validation, model card approval, registry review, and monitoring readiness before production use.
