
import json
import os
import re
import time
import urllib.request
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

TOKEN = os.environ["WAKATIME_API_KEY"]

API_URL = (
    "https://api.wakatime.com/api/v1/"
    "users/current/stats/last_7_days"
)

README_PATH = Path("README.md")
OUTPUT_PATH = Path("Assets/ai-coding.svg")

CHART_COLOR = "#3985d6"
BACKGROUND_COLOR = "#ffffff"
TEXT_COLOR = "#24292f"
MUTED_COLOR = "#6e7781"


# ============================================================
# FETCH WAKATIME STATISTICS
# ============================================================

def fetch_stats():
    request = urllib.request.Request(
        API_URL,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/json",
        },
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)

    data = result["data"]

    # WakaTime may return statistics that are still updating.
    for attempt in range(5):
        if data.get("is_up_to_date", True):
            return data

        if attempt == 4:
            raise RuntimeError(
                "WakaTime statistics are still being updated. "
                "Run the workflow again later."
            )

        print("WakaTime stats are not up to date. Retrying...")
        time.sleep(10)

        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.load(response)

        data = result["data"]

    return data


# ============================================================
# CALCULATE AI CODING PERCENTAGE
# ============================================================

def calculate_percentage(data):
    ai_lines = data.get("ai_line_changes_total")

    if ai_lines is None:
        ai_lines = (
            data.get("ai_additions", 0)
            + data.get("ai_deletions", 0)
        )

    human_lines = (
        data.get("human_additions", 0)
        + data.get("human_deletions", 0)
    )

    total_lines = ai_lines + human_lines

    percentage = (
        ai_lines / total_lines * 100
        if total_lines > 0
        else 0.0
    )

    return round(percentage, 2)


# ============================================================
# GENERATE DOUGHNUT CHART
# ============================================================

def generate_chart(percentage):
    circumference = 2 * 3.141592653589793 * 65
    progress = circumference * percentage / 100

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
     width="400" height="220" viewBox="0 0 400 220">

  <rect width="400" height="220" rx="12"
        fill="{BACKGROUND_COLOR}"/>

  <text x="200" y="30"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="17"
        font-weight="600"
        fill="{TEXT_COLOR}">
    AI Coding
  </text>

  <circle cx="200" cy="119" r="65"
          fill="none"
          stroke="#e1e4e8"
          stroke-width="13"/>

  <circle cx="200" cy="119" r="65"
          fill="none"
          stroke="{CHART_COLOR}"
          stroke-width="13"
          stroke-dasharray="{progress:.2f} {circumference:.2f}"
          stroke-linecap="round"
          transform="rotate(-90 200 119)"/>

  <text x="200" y="125"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="30"
        font-weight="700"
        fill="{TEXT_COLOR}">
    {percentage:.2f}%
  </text>

  <text x="200" y="145"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="10"
        fill="{MUTED_COLOR}">
    AI-assisted coding
  </text>

  <text x="200" y="211"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="10"
        fill="{MUTED_COLOR}">
    Last 7 Days
  </text>

</svg>
"""

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(svg, encoding="utf-8")


# ============================================================
# UPDATE README IMAGE CACHE
# ============================================================

def update_readme_cache():
    if not README_PATH.exists():
        raise FileNotFoundError("README.md not found")

    content = README_PATH.read_text(encoding="utf-8")

    image_path = "./Assets/ai-coding.svg"

    # Generate a unique version for every workflow execution.
    version = time.time_ns()

    pattern = (
        r'(\./Assets/ai-coding\.svg)'
        r'(?:\?v=[^"\'\s)]*)?'
    )

    updated_content, matches = re.subn(
        pattern,
        lambda match: f"{match.group(1)}?v={version}",
        content,
    )

    if matches == 0:
        raise RuntimeError(
            f"Image reference {image_path} was not found in README.md"
        )

    README_PATH.write_text(
        updated_content,
        encoding="utf-8",
    )


# ============================================================
# MAIN
# ============================================================

def main():
    print("Fetching WakaTime statistics...")

    data = fetch_stats()

    percentage = calculate_percentage(data)

    print(f"AI Coding Percentage: {percentage:.2f}%")

    print("Generating SVG chart...")
    generate_chart(percentage)

    print("Updating README image cache...")
    update_readme_cache()

    print("Successfully updated AI Coding chart.")


if __name__ == "__main__":
    main()
