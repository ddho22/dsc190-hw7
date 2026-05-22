"""
Stage 3: Feature engineering on transformed events data.

- Add `duration_minutes`: duration_seconds / 60
- Add `weekday`: full day-of-week name (Monday, Tuesday, ..., Sunday)
"""

import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/transformed/events.csv")
OUTPUT_PATH = Path("data/features/events.csv")


def main():
    df = pd.read_csv(INPUT_PATH)
    rows_before = len(df)

    # duration_minutes
    df["duration_minutes"] = df["duration_seconds"] / 60

    # weekday: full name from the date column
    df["weekday"] = pd.to_datetime(df["date"]).dt.strftime("%A")

    rows_after = len(df)
    assert rows_before == rows_after, "Row count changed unexpectedly!"

    print(f"Features: {rows_after} rows, added 'duration_minutes' and 'weekday'")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
