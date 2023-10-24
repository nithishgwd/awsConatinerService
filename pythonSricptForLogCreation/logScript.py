import json
import random
import datetime

# Define the log categories and possible attributes
log_categories = ["CameraActivity", "UserInteraction", "SystemHealth", "FirmwareUpdate", "Network", "QualityOfService", "Subscription"]
detection_types = ["Human", "Animal", "Vehicle"]
error_types = ["Overheating", "Memory Full", "Network Interruption", "Application Crash"]
subscription_types = ["Basic", "Premium", "Free"]
user_actions = ["streaming", "disarm mode", "privacy"]

# Generate logs and users
logs = []

# Initialize a dictionary to keep track of user subscriptions by month
user_subscriptions = {}

# Define subscription probabilities
subscription_probabilities = [0.3, 0.3, 0.4]

# Initialize a dictionary to keep track of the last subscription date for each user
last_subscription_dates = {}

start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)
delta = datetime.timedelta(days=1)

# Create 400 unique camera IDs between 300 and 699
camera_ids = list(range(300, 700))
random.shuffle(camera_ids)

# Create 400 unique user IDs
user_ids = [f"User_{i}" for i in range(1, 401)]

current_date = start_date
while current_date <= end_date:
    date_string = current_date.strftime("%Y-%m-%d")
    for _ in range(100):
        for event in log_categories:
            timestamp = f"{date_string}"
            log = {"Timestamp": timestamp, "Event": event}

            if event == "CameraActivity":
                log["Description"] = "Camera started recording due to detected motion"
                log["DetectionType"] = random.choice(detection_types)
                if camera_ids:
                    log["CameraID"] = camera_ids.pop()
                else:
                    log["CameraID"] = f"Camera_{random.choice(range(300, 700))}"  # Reuse or generate a new CameraID

            elif event == "UserInteraction":
                action = random.choice(user_actions)
                log["Action"] = action
                log["Description"] = f"User engaged in {action}"
                if user_ids:
                    log["UserID"] = user_ids.pop()
                else:
                    log["UserID"] = f"User_{random.choice(range(1, 401))}"  # Reuse or generate a new UserID

            elif event == "SystemHealth":
                log["Description"] = "Low memory warning"
                log["Status"] = "Warning"
                if camera_ids:
                    log["CameraID"] = camera_ids.pop()
                else:
                    # Reuse camera IDs or handle as needed when the list is exhausted
                    log["CameraID"] = f"Camera_{random.choice(range(300, 700))}"

                # Simulate battery backup time up to 5 days
                last_charged_time = current_date - datetime.timedelta(hours=random.randint(0, 24 * 5 * 60))  # Simulate last charge within the past 0 to 5 days
                max_battery_backup_hours = 24 * 5 * 60  # Maximum backup time of 5 days (7200 hours)

                # Make sure "FullChargedDateTime" is within the same month as the current date
                while last_charged_time.month != current_date.month:
                    last_charged_time = current_date - datetime.timedelta(hours=random.randint(0, 24 * 5 * 60))

                # Calculate a random gap within 5 days from the last charged time
                gap_hours = random.randint(0, max_battery_backup_hours)
                low_battery_time = last_charged_time + datetime.timedelta(hours=gap_hours)

                log["FullChargedDateTime"] = last_charged_time.strftime("%Y-%m-%d")
                log["LowBatteryDateTime"] = low_battery_time.strftime("%Y-%m-%d")

            elif event == "FirmwareUpdate":
                if random.random() < 0.2:
                    # Simulate a firmware update error
                    log["FirmwareUpdateAction"] = "fail"
                    log["Description"] = "Firmware update failed"
                    log["ErrorType"] = random.choice(error_types)
                else:
                    # Simulate a successful firmware update
                    log["FirmwareUpdateAction"] = "success"
                    log["Description"] = "Firmware update successfully completed"

                if camera_ids:
                    log["CameraID"] = camera_ids.pop()
                else:
                    # Reuse camera IDs or handle as needed when the list is exhausted
                    log["CameraID"] = f"Camera_{random.choice(range(300, 700))}"

            elif event == "Network":
                # Introduce a 20% chance of error
                if random.random() < 0.2:
                    log["Description"] = "Network error - Stream interruption"
                    log["ErrorType"] = random.choice(error_types)
                else:
                    log["Description"] = "Network stream is stable"
                
                if camera_ids:
                    log["CameraID"] = camera_ids.pop()
                else:
                    # Reuse camera IDs or handle as needed when the list is exhausted
                    log["CameraID"] = f"Camera_{random.choice(range(300, 700))}"

            elif event == "QualityOfService":
                log["Description"] = "High latency observed in live stream"
                log["Latency"] = f"{random.randint(50, 500)}ms"
                if camera_ids:
                    log["CameraID"] = camera_ids.pop()
                else:
                    # Reuse camera IDs or handle as needed when the list is exhausted
                    log["CameraID"] = f"Camera_{random.choice(range(300, 700))}"

            # Update the "Subscription" event generation code
            elif event == "Subscription":
                # Ensure that the "UserID" key exists in the log
                if "UserID" not in log:
                    if user_ids:
                        log["UserID"] = user_ids.pop()
                    else:
                        log["UserID"] = f"User_{random.choice(range(1, 401))}"

                # Check if the user has already subscribed this month
                user_id = log["UserID"]
                current_date = datetime.datetime.strptime(log["Timestamp"], "%Y-%m-%d")

                if user_id in last_subscription_dates:
                    last_subscription_date = last_subscription_dates[user_id]

                    # Randomly select a subscription type based on the specified probabilities
                    subscription_type = random.choices(subscription_types, subscription_probabilities)[0]
                    log["SubscriptionType"] = subscription_type
                    log["Description"] = f"User subscribed to the {subscription_type} plan"
                else:
                    # User has not subscribed before, so set the description to "User subscribed to the Basic plan"
                    subscription_type = "Basic"
                    log["SubscriptionType"] = subscription_type
                    log["Description"] = f"User subscribed to the {subscription_type} plan"

                # Update the last subscription date for the user
                last_subscription_dates[user_id] = current_date

            logs.append(log)
    current_date += delta

# Save the generated logs to a JSON file
with open("security_camera_logs.json", "w") as json_file:
    json.dump(logs, json_file, indent=4)

