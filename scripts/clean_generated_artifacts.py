from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    removed = 0
    for pattern in ["**/__pycache__", "**/*.pyc"]:
        for path in REPO_ROOT.glob(pattern):
            if path.is_dir():
                for child in path.glob("*"):
                    child.unlink()
                path.rmdir()
                removed += 1
            elif path.is_file():
                path.unlink()
                removed += 1
    print(f"Removed {removed} generated Python cache artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
