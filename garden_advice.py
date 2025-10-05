# Ask the user for input
season = input("Enter the season (summer or winter): ").lower()
plant_type = input("Enter the plant type (flower or vegetable): ").lower()

advice = ""

if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

print("\nYour gardening advice:\n" + advice)
