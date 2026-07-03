from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_portfolio(path: Path) -> dict[str, Any]:
    return load_json(path)


def model_by_id(portfolio: dict[str, Any], model_id: str) -> dict[str, Any]:
    for model in portfolio.get("models", []):
        if model["model_id"] == model_id:
            return model
    raise KeyError(f"Unknown model_id: {model_id}")


def active_models(portfolio: dict[str, Any]) -> list[dict[str, Any]]:
    return [model for model in portfolio.get("models", []) if model.get("status") != "data_gap"]


def registry_name(model_id: str) -> str:
    parts = model_id.replace("nf_", "").split("_")
    return "NordForge" + "".join(part.title() for part in parts)
