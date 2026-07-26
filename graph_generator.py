import json
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from datetime import datetime


def generate_graph():

    if not os.path.exists("history.json"):
        return None

    with open("history.json", "r") as file:
        history = json.load(file)

    if len(history) < 2:
        return None

    dates = []
    values = []

    for item in history:
        dates.append(datetime.strptime(item["date"], "%Y-%m-%d"))
        values.append(item["portfolio_value"])

    plt.style.use("default")

    fig, ax = plt.subplots(figsize=(10, 5))

    # Background
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    # Remove unnecessary borders
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.spines["left"].set_color("#DDDDDD")
    ax.spines["bottom"].set_color("#DDDDDD")

    # Light grid
    ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.35)

    # Modern blue line
    line_color = "#2563EB"

    ax.plot(
        dates,
        values,
        color=line_color,
        linewidth=3,
        marker="o",
        markersize=8,
        markerfacecolor="white",
        markeredgewidth=2,
        markeredgecolor=line_color,
    )

    # Fill below line
    ax.fill_between(
        dates,
        values,
        min(values),
        color=line_color,
        alpha=0.12
    )

    # Title
    ax.set_title(
        "Portfolio Growth",
        fontsize=18,
        fontweight="bold",
        loc="left",
        pad=20
    )

    # Subtitle
    ax.text(
        0,
        1.02,
        "Daily portfolio value based on NAV updates",
        transform=ax.transAxes,
        fontsize=11,
        color="gray"
    )

    # Currency formatting
    ax.yaxis.set_major_formatter(
        FuncFormatter(lambda x, pos: f"₹{x:,.0f}")
    )

    # Date formatting
    ax.set_xticks(dates)
    ax.set_xticklabels(
        [d.strftime("%d %b") for d in dates],
        fontsize=10
    )

    # Axis labels
    ax.set_xlabel("")
    ax.set_ylabel("Portfolio Value", fontsize=11)

    # Add some padding
    ymin = min(values) * 0.995
    ymax = max(values) * 1.005
    ax.set_ylim(ymin, ymax)

    plt.tight_layout()

    plt.savefig(
        "portfolio_growth.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return "portfolio_growth.png"