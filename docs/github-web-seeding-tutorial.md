# GitHub Web Seeding Tutorial

## Upload

1. Create a new empty repository named `nordforge-mlflow-ml-lifecycle`.
2. Do not initialize with README, `.gitignore`, or license.
3. Use `Add file` -> `Upload files`.
4. Drag the full contents of this repository folder into GitHub.
5. Commit to branch `feature/bootstrap-mlflow-lifecycle`.
6. Open PR `Bootstrap MLflow lifecycle repository`.
7. Paste PR 1 from `docs/seed-pull-requests.md`.
8. Merge it.

## Labels

Create labels from `docs/labels-and-milestones.md`.

Minimum set:

- `type: experiment`
- `type: model-promotion`
- `type: incident`
- `type: platform-task`
- `type: data-gap`
- `area: mlflow`
- `area: registry`
- `area: monitoring`
- `domain: logistics`
- `domain: inventory`
- `domain: customer-availability`
- `priority: high`
- `blocked`

## Issues

Create one issue per section in `docs/seed-issues.md`.

Recommended initial state:

- Keep supplier-risk and energy-anomaly issues open and blocked.
- Keep freight monitoring open or draft.
- Close the promotion-template checklist issue through PR 2.

## Pull Requests

Use `docs/seed-pull-requests.md`.

Recommended states:

- PR 1 merged.
- PR 2 merged.
- PR 3 open.
- PR 4 draft.

## Project Board

Create a GitHub Project named `NordForge ML Lifecycle Readiness` and use `docs/seed-project-board.md`.
