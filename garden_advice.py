"""
Garden advice generator.

- Uses mapping dicts instead of long if/elif chains
- Splits logic into functions
- Easy to extend: add keys to SEASON_TIPS / PLANT_TIPS
"""

SEASON_TIPS = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
}

PLANT_TIPS = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}

def normalise(text: str) -> str:
    """Trim and lowercase user input."""
    return (text or "").strip().lower()

def advice_for(season: str, plant_type: str) -> str:
    """Return combined advice lines for the chosen season and plant type."""
    s = normalise(season)
    p = normalise(plant_type)

    season_line = SEASON_TIPS.get(s, "No advice for this season.")
    plant_line  = PLANT_TIPS.get(p, "No advice for this type of plant.")
    return f"{season_line}\n{plant_line}"

def main():
    # I/O kept simple for CLI; reuse advice_for() in tests or UI
    season = input("Enter the season (e.g., summer / winter): ")
    plant_type = input("Enter the plant type (e.g., flower / vegetable): ")
    print("\nYour gardening advice:\n" + advice_for(season, plant_type))

if __name__ == "__main__":
    main()
