import pandas as pd
import matplotlib.pyplot as plt

# Load the subscription data from a CSV file
df = pd.read_csv("subscription_data.csv")

# Extract subscription data for the specific year (e.g., 2023)
year = "2023"
subscription_data = df[(df["Event"] == "Subscription") & df["Timestamp"].str.startswith(year)]

# Define colors for each subscription type
colors = {"Basic": "blue", "Premium": "green", "Free": "orange"}

# Count the number of subscriptions for each type
subscription_counts = {"Basic": 0, "Premium": 0, "Free": 0}
for _, row in subscription_data.iterrows():
    subscription_type = row["SubscriptionType"]
    subscription_counts[subscription_type] += 1

# Create a bar chart with different colors for each subscription type
subscription_types = list(subscription_counts.keys())
counts = list(subscription_counts.values())

# Get the corresponding color for each subscription type
bar_colors = [colors[subscription_type] for subscription_type in subscription_types]

plt.bar(subscription_types, counts, color=bar_colors)
plt.xlabel("Subscription Type")
plt.ylabel("Number of Subscriptions")
plt.title(f"Subscription Counts for {year}")

# Add labels on top of each bar
for i in range(len(subscription_types)):
    plt.text(subscription_types[i], counts[i] + 1, str(counts[i]), ha='center', va='bottom')

# Add a legend to clarify the colors
legend_labels = [f"{subscription_type} ({counts[i]})" for i, subscription_type in enumerate(subscription_types)]
plt.legend(legend_labels)

plt.show()
