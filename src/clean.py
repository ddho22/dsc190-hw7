"""
Stage 1: Clean raw events data.

- Drop rows with any missing fields
- Drop rows with invalid event_type (only allow: click, view, purchase)
- Drop rows with non-positive duration_seconds
- Normalize timestamp to ISO 8601 format: YYYY-MM-DDTHH:MM:SS
"""

import pandas as pd
from pathlib import Path

VALID_EVENT_TYPES = {"click", "view", "purchase"}

INPUT_PATH = Path("data/raw/events.csv")
OUTPUT_PATH = Path("data/clean/events.csv")


def parse_timestamp(ts: str) -> str:
    """Parse a timestamp string (various formats) and return ISO 8601."""
    dt = pd.to_datetime(ts, dayfirst=False)
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def main():
    df = pd.read_csv(INPUT_PATH)

    before = len(df)

    # Drop rows with any missing/empty fields
    df = df.dropna(subset=["user_id", "timestamp", "event_type", "duration_seconds"])
    df = df[df["user_id"].astype(str).str.strip() != ""]
    df = df[df["timestamp"].astype(str).str.strip() != ""]

    # Drop rows with invalid event_type
    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

    # Drop rows with non-positive duration_seconds
    df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
    df = df.dropna(subset=["duration_seconds"])
    df = df[df["duration_seconds"] > 0]

    # Normalize timestamp to ISO 8601
    df["timestamp"] = df["timestamp"].apply(parse_timestamp)

    after = len(df)
    print(f"Clean: {before} rows -> {after} rows (dropped {before - after})")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
