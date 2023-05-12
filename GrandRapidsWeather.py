import random

def calculate_wind_chill(temp, wind_speed):
    # calculate wind chill using the formula
    wind_chill = 35.74 + (0.6215 * temp) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temp * (wind_speed ** 0.16))
    return round(wind_chill, 1)

conditions = ['Snow', 'Sleet', 'Freezing Rain', 'Blizzard', 'Windy', 'Sunny', 'Light Snow', 'Cold Snap']

condition = random.choice(conditions)
synonyms = ["gorgeous", "stunning", "breathtaking", "charming", "enchanting", "picturesque", "beautiful", "lovely", \
              "majestic", "scenic"]
descriptor = random.choice(synonyms)
print(f"Today's weather in {descriptor} Grand Rapids, Michigan:")

if condition == 'Sunny':
    temperature = random.randint(15, 40)
    wind_speed = random.randint(5, 10)
    wind_chill = calculate_wind_chill(temperature, wind_speed)
    print(f"{condition}\n{temperature}F\nWind {wind_speed} mph\nWind chill: {wind_chill}F")
elif condition == 'Windy':
    temperature = random.randint(15, 30)
    wind_speed = random.randint(20, 40)
    wind_chill = calculate_wind_chill(temperature, wind_speed)
    print(f"{condition}\n{temperature}F\nWind {wind_speed} mph\nWind chill: {wind_chill}F")
elif condition in ['Snow', 'Sleet', 'Freezing Rain', 'Blizzard Conditions', 'Light Snow']:
    temperature = random.randint(0, 20)
    wind_speed = random.randint(5, 20)
    wind_chill = calculate_wind_chill(temperature, wind_speed)
    print(f"{condition}\n{temperature}F\nWind {wind_speed} mph\nWind chill: {wind_chill}F")
elif condition == 'Cold Snap':
    temperature = random.randint(-20, 0)
    wind_speed = random.randint(0, 15)
    wind_chill = calculate_wind_chill(temperature, wind_speed)
    print(f"{condition}\n{temperature}F\nWind {wind_speed} mph\nWind chill: {wind_chill}F")
else:
    print("Error: unknown condition")
