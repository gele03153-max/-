#!/usr/bin/env python3
"""Plot audited low-temperature discharge/charge-rate ratios without editing input data.

Usage:
    python plot_figures.py
    python plot_figures.py --input /path/Origin_all_records.csv --output-dir /path/figures

The input CSV is read as UTF-8 with optional BOM. Missing ratios remain missing.
A conditional point requires BOTH Ratio_assumed > 0 and an explicitly true
Symmetry_assumption. No ratio is inferred from a single reported current, and
no field containing a maximum rate is used. This is a cycle-count/rate-ratio
comparison, not a conventional energy-density/power-density Ragone plot.
"""
from __future__ import annotations

import argparse
import csv
import math
import os
from pathlib import Path
import warnings

os.environ.setdefault("MPLCONFIGDIR", "/tmp/dib_matplotlib_cache")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp/dib_font_cache")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter, LogLocator, NullFormatter
from matplotlib.transforms import Bbox
import numpy as np


REQUIRED = {
    "Point_ID", "Ref_ID", "Temperature_C", "Cycles", "Ratio_strict",
    "Ratio_assumed", "Plot_group", "Symmetry_assumption", "Cell_format",
}
USER_COLOR = "#B83432"
LITERATURE_COLOR = "#235C87"
FOOTNOTE_CONDITIONAL = (
    "Hollow literature points assume equal charge/discharge currents; not independently reported."
)


def number(value: str | None) -> float | None:
    """Read only finite numeric values; missing/NV/NR strings stay missing."""
    if value is None:
        return None
    value = str(value).strip().replace("−", "-")
    if not value or value.lower() in {"na", "n/a", "nan", "nv", "nr", "none", "null", "-"}:
        return None
    try:
        result = float(value)
    except ValueError:
        return None
    return result if math.isfinite(result) else None


def true_value(value: str | None) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def read_records(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = REQUIRED.difference(reader.fieldnames or ())
        if missing:
            raise ValueError("Missing CSV columns: " + ", ".join(sorted(missing)))
        records = list(reader)
    seen: set[str] = set()
    for row in records:
        ident = row["Point_ID"].strip()
        if not ident:
            raise ValueError("Every record must have a Point_ID")
        if ident in seen:
            raise ValueError(f"Duplicate Point_ID: {ident}")
        seen.add(ident)
    return records


def choose_records(records: list[dict], conditional: bool) -> list[dict]:
    selected = []
    for row in records:
        cycles = number(row.get("Cycles"))
        temperature = number(row.get("Temperature_C"))
        if cycles is None or cycles <= 0 or temperature is None or temperature >= 0:
            continue
        strict = number(row.get("Ratio_strict"))
        assumed = number(row.get("Ratio_assumed"))
        if strict is not None and strict > 0:
            ratio, is_assumed = strict, False
        elif conditional and assumed is not None and assumed > 0 and true_value(row.get("Symmetry_assumption")):
            # An explicit assumption supplied in the audited CSV is mandatory.
            ratio, is_assumed = assumed, True
        else:
            continue
        item = dict(row)
        item.update(
            _x=cycles, _y=ratio, _temperature=temperature,
            _assumed=is_assumed,
            _user=row.get("Plot_group", "").strip().lower() == "this work",
        )
        if item["_user"] and is_assumed:
            warnings.warn(f"Skipping assumed This work point: {item['Point_ID']}")
            continue
        selected.append(item)
    return selected


def label_for(row: dict, duplicated_labels: set[str]) -> str:
    temperature = f"{row['_temperature']:g}".replace("-", "−")
    if row["_user"]:
        cell = row.get("Cell_format", "").strip()
        # Short descriptive English supplied by the data producer is retained.
        suffix = f", {cell}" if cell else ""
        label = f"This work: {temperature} °C{suffix}"
    else:
        label = f"{row['Ref_ID']}: {temperature} °C"
    if label in duplicated_labels:
        current = row.get('Reported_single_current', '')
        unit = row.get('Current_unit', '').replace('g^-1', 'g⁻¹')
        label += f", {current} {unit}" if current else f" [{row['Point_ID']}]"
    return label


def collision_area(first: Bbox, second: Bbox) -> float:
    w = max(0.0, min(first.x1, second.x1) - max(first.x0, second.x0))
    h = max(0.0, min(first.y1, second.y1) - max(first.y0, second.y0))
    return w * h


def add_labels(fig, ax, records: list[dict]) -> None:
    """Place compact labels with leader lines using measured text bounding boxes.

    Placement moves labels only. It never moves or jitters any data point.
    """
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    font = FontProperties(family="DejaVu Sans", size=8.0)
    point_to_px = fig.dpi / 72
    axes_box = ax.get_window_extent(renderer)
    interior = Bbox.from_extents(axes_box.x0 + 3, axes_box.y0 + 3,
                                axes_box.x1 - 3, axes_box.y1 - 3)
    occupied: list[Bbox] = []
    marker_boxes = []
    for row in records:
        px, py = ax.transData.transform((row["_x"], row["_y"]))
        marker_boxes.append(Bbox.from_bounds(px - 6, py - 6, 12, 12))
    base_labels = [label_for(row, set()) for row in records]
    duplicates = {label for label in base_labels if base_labels.count(label) > 1}
    # Give prominent supplied results first choice of an uncluttered label position.
    order = sorted(range(len(records)), key=lambda i: (not records[i]["_user"], records[i]["_x"]))
    for index in order:
        row = records[index]
        label = label_for(row, duplicates)
        width, height, _ = renderer.get_text_width_height_descent(label, font, ismath=False)
        width += 7
        height = max(height, 10) + 5
        px, py = ax.transData.transform((row["_x"], row["_y"]))
        candidates = []
        # Literature ratios often coincide at one, so several annotation lanes are needed.
        y_offsets = (18, 34, 50, 66, -19, -35, 82, -51, 98, 114, -67)
        x_offsets = (0, 28, -28, 56, -56, 84, -84, 112, -112, 140, -140)
        for dy in y_offsets:
            for dx in x_offsets:
                tx, ty = px + dx * point_to_px, py + dy * point_to_px
                box = Bbox.from_bounds(tx - width / 2, ty - height / 2, width, height)
                inside = collision_area(box, interior)
                outside = width * height - inside
                overlaps = sum(collision_area(box, other) for other in occupied)
                marker_overlap = sum(collision_area(box, other) for other in marker_boxes)
                score = outside * 200 + overlaps * 90 + marker_overlap * 8
                score += (dx * dx + dy * dy) ** 0.5
                candidates.append((score, dx, dy, box))
        _, dx, dy, best_box = min(candidates, key=lambda item: item[0])
        occupied.append(best_box.expanded(1.015, 1.12))
        color = USER_COLOR if row["_user"] else LITERATURE_COLOR
        ax.annotate(
            label, (row["_x"], row["_y"]), xytext=(dx, dy),
            textcoords="offset points", ha="center", va="center",
            fontproperties=font, color=color,
            bbox={"boxstyle": "square,pad=0.12", "fc": "white", "ec": "none", "alpha": 0.93},
            arrowprops={"arrowstyle": "-", "color": color, "lw": 0.6, "shrinkA": 3, "shrinkB": 6},
            zorder=5,
        )


def clean_tick(value: float, _position: int) -> str:
    if value <= 0:
        return ""
    return f"{value:,.0f}" if value >= 1 else f"{value:g}"


def make_figure(records: list[dict], conditional: bool, output_dir: Path) -> dict:
    chosen = choose_records(records, conditional)
    prefix = "conditional_rate_ratio_vs_cycles" if conditional else "strict_rate_ratio_vs_cycles"
    fig, ax = plt.subplots(figsize=(8.4, 6.25), dpi=110)
    fig.subplots_adjust(left=0.115, right=0.975, bottom=0.235, top=0.88)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Low-temperature cycle count", labelpad=9)
    ax.set_ylabel("Low-temperature discharge / charge rate ratio", labelpad=10)
    ax.set_title("Low-temperature cycling and charge/discharge-rate ratio", pad=28,
                 fontsize=12.1, loc="left")
    ax.text(0, 1.035,
            "Conditional literature comparison" if conditional else "Strict plot: explicitly specified protocols only",
            transform=ax.transAxes, fontsize=9.3, color="#555555", ha="left")
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(which="both", direction="out", labelsize=9)
    ax.grid(axis="both", which="major", lw=0.55, color="#E2E5E8", zorder=0)
    ax.axhline(1, color="#93999D", ls=(0, (3, 3)), lw=0.8, zorder=1)
    ax.xaxis.set_major_locator(LogLocator(base=10, subs=(1, 2, 5), numticks=12))
    ax.yaxis.set_major_locator(LogLocator(base=10, subs=(1, 2, 5), numticks=12))
    ax.xaxis.set_major_formatter(FuncFormatter(clean_tick))
    ax.yaxis.set_major_formatter(FuncFormatter(clean_tick))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.yaxis.set_minor_formatter(NullFormatter())
    if chosen:
        xx = np.array([r["_x"] for r in chosen], dtype=float)
        yy = np.array([r["_y"] for r in chosen], dtype=float)
        log_span = max(math.log10(xx.max()) - math.log10(xx.min()), 0.8)
        margin = max(0.13 * log_span, 0.11)
        ax.set_xlim(10 ** (math.log10(xx.min()) - margin), 10 ** (math.log10(xx.max()) + margin))
        ax.set_ylim(min(0.47, yy.min() / 2.1), max(15, yy.max() * 1.65))
        for row in chosen:
            if row["_user"]:
                ax.scatter(row["_x"], row["_y"], s=92, marker="*", color=USER_COLOR,
                           edgecolors=USER_COLOR, linewidths=0.9, zorder=4)
            elif row["_assumed"]:
                ax.scatter(row["_x"], row["_y"], s=58, marker="o", facecolors="white",
                           edgecolors=LITERATURE_COLOR, linewidths=1.3, zorder=3)
            else:
                ax.scatter(row["_x"], row["_y"], s=48, marker="o", color=LITERATURE_COLOR,
                           edgecolors="white", linewidths=0.45, zorder=3)
        add_labels(fig, ax, chosen)
    else:
        ax.set_xlim(10, 100000)
        ax.set_ylim(0.47, 15)
        ax.text(0.5, 0.55, "No eligible records with verified ratios", transform=ax.transAxes,
                ha="center", va="center", fontsize=11)
    handles = []
    if any(r["_user"] for r in chosen):
        handles.append(Line2D([], [], marker="*", ls="none", markersize=9,
                              color=USER_COLOR, label="This work: user supplied"))
    if any(not r["_user"] and not r["_assumed"] for r in chosen):
        handles.append(Line2D([], [], marker="o", ls="none", markersize=6,
                              color=LITERATURE_COLOR, label="Literature: verified rates"))
    if any(r["_assumed"] for r in chosen):
        handles.append(Line2D([], [], marker="o", ls="none", markersize=6,
                              markerfacecolor="white", markeredgewidth=1.2,
                              color=LITERATURE_COLOR, label="Literature: equal-current assumption"))
    if handles:
        fig.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.11, 0.105),
                   frameon=False, fontsize=9, ncol=2, handletextpad=0.45, columnspacing=1.2)
    if conditional:
        fig.text(0.115, 0.072, FOOTNOTE_CONDITIONAL, fontsize=8.2,
                 color="#8D2927", ha="left", va="center")
        fig.text(0.115, 0.043, "A single reported current does not independently establish both directional rates.",
                 fontsize=8.0, color="#555555", ha="left", va="center")
    else:
        fig.text(0.115, 0.065, "Only non-missing Ratio_strict values are plotted; literature values are not inferred.",
                 fontsize=8.2, color="#555555", ha="left", va="center")
        fig.text(0.115, 0.039, "User-supplied results have not been independently experimentally verified.",
                 fontsize=8.0, color="#555555", ha="left", va="center")
    saved = []
    for extension in ("png", "pdf", "svg"):
        target = output_dir / f"{prefix}.{extension}"
        fig.savefig(target, dpi=600 if extension == "png" else None,
                    facecolor="white", metadata={"Creator": "Audited DIB scientific plotting script"})
        saved.append(str(target))
    plt.close(fig)
    return {"figure": prefix, "count": len(chosen), "point_ids": [r["Point_ID"] for r in chosen], "files": saved}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    default_input = Path(__file__).resolve().parent / "交付文件_V2" / "Origin_all_records.csv"
    parser.add_argument("--input", type=Path, default=default_input)
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()
    output_dir = args.output_dir or args.input.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 10,
        "axes.linewidth": 0.8, "svg.fonttype": "none", "pdf.fonttype": 42,
        "savefig.pad_inches": 0.08,
    })
    records = read_records(args.input)
    for conditional in (False, True):
        result = make_figure(records, conditional, output_dir)
        print(f"{result['figure']}: {result['count']} points; IDs=" + ", ".join(result["point_ids"]))
        for path in result["files"]:
            print(path)


if __name__ == "__main__":
    main()
