import marimo

__generated_with = "0.23.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    return mo, pd, plt


@app.cell
def _(mo):
    mo.md("# Event Duration Report")
    return


@app.cell
def _(pd):
    df = pd.read_csv("data/features/events.csv")
    df.head()
    return (df,)


@app.cell
def _(mo, df):
    mo.md(f"**Dataset:** {len(df)} events | **Columns:** {', '.join(df.columns.tolist())}")
    return


@app.cell
def _(df, plt):
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(df["duration_minutes"], bins=20, color="#4C72B0", edgecolor="white", linewidth=0.6)
    ax.set_xlabel("Duration (minutes)", fontsize=12)
    ax.set_ylabel("Count", fontsize=12)
    ax.set_title("Distribution of Event Durations", fontsize=14, fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    fig
    return ax, fig


@app.cell
def _(mo, df):
    stats = df["duration_minutes"].describe().round(2)
    mo.md(f"""
    ### Summary Statistics — duration_minutes

    | Stat | Value |
    |------|-------|
    | Count | {stats['count']:.0f} |
    | Mean | {stats['mean']:.2f} |
    | Std | {stats['std']:.2f} |
    | Min | {stats['min']:.2f} |
    | 25% | {stats['25%']:.2f} |
    | Median | {stats['50%']:.2f} |
    | 75% | {stats['75%']:.2f} |
    | Max | {stats['max']:.2f} |
    """)
    return (stats,)


@app.cell
def _(df, plt):
    fig2, ax2 = plt.subplots(figsize=(9, 4))
    weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    counts = df["weekday"].value_counts().reindex(weekday_order, fill_value=0)
    ax2.bar(counts.index, counts.values, color="#55A868", edgecolor="white", linewidth=0.6)
    ax2.set_xlabel("Day of Week", fontsize=12)
    ax2.set_ylabel("Event Count", fontsize=12)
    ax2.set_title("Events by Day of Week", fontsize=14, fontweight="bold")
    ax2.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    fig2
    return ax2, counts, fig2, weekday_order


if __name__ == "__main__":
    app.run()
