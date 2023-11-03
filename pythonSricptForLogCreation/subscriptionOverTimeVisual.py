import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a DataFrame containing the subscription data, for example:
df = pd.read_csv('D:/cources/workspace/aws_microservice_workspace/pythonSricptForLogCreation/subscription_data.csv')

# Convert the 'Timestamp' column to a datetime type
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Set the start and end months (e.g., January to June)
start_month = 1
end_month = 3

# Filter the DataFrame to include data only for the specified month range
filtered_df = df[(df['Timestamp'].dt.month >= start_month) & (df['Timestamp'].dt.month <= end_month)]

# Create a single figure
fig, ax = plt.subplots(figsize=(12, 6))

# You can group the data by date and subscription type and count the number of subscriptions
subscription_counts = filtered_df.groupby(['Timestamp', 'SubscriptionType'])['UserID'].count().unstack().fillna(0)

# Reorder the columns to display Free, Basic, Premium
subscription_counts = subscription_counts[['Free', 'Basic', 'Premium']]

# Plot the data on the existing figure
subscription_counts.plot(kind='line', marker='o', ax=ax)

# Set labels and title
plt.xlabel('Date')
plt.ylabel('Number of Subscriptions')
plt.title('Subscription Trends Over Time')

# Add a legend with custom labels and order
plt.legend(title='Subscription Type', labels=['Free', 'Basic', 'Premium'], loc='upper left')

# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show()
