"""
Stage 2: Transform clean events data.

- Add a `date` column (YYYY-MM-DD) extracted from `timestamp`.
"""

import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/clean/events.csv")
OUTPUT_PATH = Path("data/transformed/events.csv")


def main():
    df = pd.read_csv(INPUT_PATH)

    # Add date column from timestamp
    df["date"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d")

    print(f"Transform: {len(df)} rows, added 'date' column")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
