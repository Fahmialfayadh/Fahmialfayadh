
import json
import os
import urllib.request
from pathlib import Path

TOKEN = os.environ["WAKATIME_API_KEY"]
API_URL = (
    "https://api.wakatime.com/api/v1/"
    "users/current/stats/last_7_days"
)

request = urllib.request.Request(
    API_URL,
    headers={"Authorization": f"Bearer {TOKEN}"},
)

with urllib.request.urlopen(request, timeout=30) as response:
    data = json.load(response)["data"]

category = next(
    (
        item for item in data["categories"]
        if item["name"].lower() == "ai coding"
    ),
    None,
)

if category is None:
    raise RuntimeError("AI Coding category not found in WakaTime stats")

percentage = float(category["percent"])
percentage = max(0.0, min(100.0, percentage))

circumference = 2 * 3.141592653589793 * 65
progress = circumference * percentage / 100

svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
     width="400" height="220" viewBox="0 0 400 220">
  <rect width="400" height="220" rx="12" fill="#ffffff"/>

  <text x="200" y="30"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="17" font-weight="600"
        fill="#24292f">
    AI Coding
  </text>

  <circle cx="200" cy="119" r="65"
          fill="none" stroke="#e1e4e8" stroke-width="13"/>

  <circle cx="200" cy="119" r="65"
          fill="none" stroke="#3985d6" stroke-width="13"
          stroke-dasharray="{progress:.2f} {circumference:.2f}"
          stroke-linecap="round"
          transform="rotate(-90 200 119)"/>

  <text x="200" y="125"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="30" font-weight="700"
        fill="#24292f">
    {percentage:.2f}%
  </text>

  <text x="200" y="145"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="10"
        fill="#6e7781">
    AI-assisted coding
  </text>

  <text x="200" y="211"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="10"
        fill="#6e7781">
    Last 7 Days
  </text>
</svg>
"""

output = Path("Assets/ai-coding.svg")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(svg, encoding="utf-8")

print(f"Updated AI Coding chart: {percentage:.2f}%")
