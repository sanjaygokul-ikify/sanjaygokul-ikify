import random
import time
import logging
from datetime import datetime, timedelta

# Log setup to track food safety, waste, and hygiene reminders
logging.basicConfig(filename='food_safety_hygiene.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# This class helps us manage food safety conditions and store expiration dates.
class FoodItem:
    def __init__(self, name, temp_limit, humidity_limit, shelf_life):
        self.name = name  # Name of the food item
        self.temp_limit = temp_limit  # Max temp for safety
        self.humidity_limit = humidity_limit  # Max humidity level
        self.shelf_life = shelf_life  # How long it can stay safe in storage
        self.added_on = datetime.now()  # Track the date it was stored

# Adding various food items with specific safety parameters
foods_list = [
    FoodItem(name="Milk", temp_limit=4, humidity_limit=65, shelf_life=7),
    FoodItem(name="Chicken", temp_limit=5, humidity_limit=70, shelf_life=5),
    FoodItem(name="Apple", temp_limit=8, humidity_limit=60, shelf_life=10),
    FoodItem(name="Carrot", temp_limit=10, humidity_limit=75, shelf_life=14)
]

# Simulating sensors that collect temperature and humidity readings
def fetch_sensor_data():
    # Generate random temperature and humidity readings
    current_temp = round(random.uniform(2, 12), 2)
    current_humidity = round(random.uniform(50, 80), 2)
    return current_temp, current_humidity

# Function to determine whether the food is safe
def check_safety(current_temp, current_humidity, food):
    status = True
    reasons = []

    # Is the temperature safe?
    if current_temp > food.temp_limit:
        status = False
        reasons.append(f"Temperature {current_temp}°C exceeds the safe limit for {food.name}.")
    else:
        reasons.append(f"Temperature {current_temp}°C is safe for {food.name}.")

    # Is the humidity safe?
    if current_humidity > food.humidity_limit:
        status = False
        reasons.append(f"Humidity {current_humidity}% is too high for {food.name}.")
    else:
        reasons.append(f"Humidity {current_humidity}% is fine for {food.name}.")

    # Has the food expired?
    days_in_storage = (datetime.now() - food.added_on).days
    if days_in_storage > food.shelf_life:
        status = False
        reasons.append(f"{food.name} is expired after {days_in_storage} days of storage.")
    else:
        reasons.append(f"{food.name} is still fresh after {days_in_storage} days.")

    if status:
        return "Yes", "All good!"
    else:
        return "No", " ".join(reasons)

# Logging each check result
def log_check(outcome, details, temp, humidity, food):
    log_entry = (f"Result: {outcome} | {food.name}: Temp={temp}°C, "
                 f"Humidity={humidity}% | {details}")
    logging.info(log_entry)
    print(log_entry)

# Sanitization reminder before eating food
def hand_sanitizer_prompt():
    """
    A simple prompt asking if the user has sanitized their hands
    before they handle or eat food.
    """
    response = input("Have you sanitized your hands before eating? (yes/no): ").strip().lower()
    if response == "yes":
        print("Great! You can now safely enjoy your meal.")
        logging.info("User confirmed sanitizing hands before eating.")
    else:
        print("Please sanitize your hands before eating.")
        logging.info("User skipped sanitizing hands.")

# Alerts for unsafe food conditions
def notify_issues(outcome, details, food):
    if outcome == "No":
        print(f"WARNING: {food.name} is not safe to consume! {details}")
    # Remind the user about hand hygiene
    hand_sanitizer_prompt()

# Checking stock to avoid food waste
def check_food_stock(food):
    days_stored = (datetime.now() - food.added_on).days
    days_remaining = food.shelf_life - days_stored

    if days_remaining <= 2:
        print(f"NOTICE: {food.name} is about to expire (Stored for {days_stored} days, {days_remaining} days left).")
        print(f"Consider using {food.name} soon to prevent waste.")

# A quick report summarizing food safety and waste checks
def generate_daily_report(all_checks):
    print("\n--- Daily Food Safety Report ---")
    for entry in all_checks:
        time_checked, food, outcome, details, temp, humidity = entry
        print(f"[{time_checked}] {food.name} - {outcome} (Temp={temp}°C, Humidity={humidity}%)")
        print(f"Details: {details}\n")
    print("--- End of Report ---")

# Main monitoring function
def run_food_monitoring():
    print("Food safety and hygiene monitoring started...\n")
    check_records = []

    try:
        while True:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            for food in foods_list:
                # Get sensor data
                temp, humidity = fetch_sensor_data()

                # Run safety checks
                outcome, details = check_safety(temp, humidity, food)

                # Log the result and notify if issues exist
                log_check(outcome, details, temp, humidity, food)
                notify_issues(outcome, details, food)

                # Keep an eye on stock to prevent food waste
                check_food_stock(food)

                # Record this check for the daily summary report
                check_records.append((current_time, food, outcome, details, temp, humidity))

            # Simulate a delay between checks (10 seconds)
            time.sleep(10)

            # After 10 checks, we generate a daily report
            if len(check_records) >= 10:
                generate_daily_report(check_records)
                check_records.clear()  # Reset records for the next "day"
    except KeyboardInterrupt:
        print("\nMonitoring interrupted.")

# Run the system
if __name__ == "__main__":
    run_food_monitoring()
    import time
import random
import logging

# Setup logging to track fumigation process
logging.basicConfig(filename='fumigation_log.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Function to simulate air quality sensor readings (returns random values)
def get_air_quality():
    return random.randint(50, 200)  # Air quality levels (lower is better)

# Function to perform fumigation and clean the air
def fumigate_room():
    logging.info("Fumigation started.")
    print("Fumigation in progress...")
    time.sleep(5)  # Simulating time it takes to fumigate
    logging.info("Fumigation completed.")
    print("Fumigation complete. Air should be cleaner now.")

# Function to check if air quality needs fumigation
def check_air_and_fumigate():
    air_quality = get_air_quality()
    print(f"Current air quality index: {air_quality}")

    if air_quality > 100:  # Threshold for fumigation
        logging.info(f"Poor air quality detected: {air_quality}. Fumigation required.")
        fumigate_room()
        print("Air quality is poor, fumigation completed.")
    else:
        logging.info(f"Air quality is good: {air_quality}. No fumigation needed.")
        print("Air quality is good. No fumigation needed.")



