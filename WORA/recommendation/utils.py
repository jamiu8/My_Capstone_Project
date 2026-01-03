# recommendations/utils.py

def generate_outfit(temperature, description):
    outfit = ""
    # Temperature-based recommendation
    if temperature > 30:
        outfit = "Light T-shirt, shorts, sunglasses."
    elif 20 <= temperature <= 30:
        outfit = "Shirt and jeans recommended."
    elif 10 <= temperature < 20:
        outfit = "Sweater or hoodie recommended."
    else:
        outfit = "Heavy jacket, gloves, and boots."

    # Weather-based adjustment
    if "rain" in description.lower():
        outfit += " Don't forget an umbrella or raincoat."
    elif "snow" in description.lower():
        outfit += " Consider snow boots and warm gloves."

    return outfit
