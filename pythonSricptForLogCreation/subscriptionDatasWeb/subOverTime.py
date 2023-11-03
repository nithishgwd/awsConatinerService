import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template
from io import BytesIO
import base64

app = Flask(__name__)

# Replace with the path to your CSV file
csv_file = 'D:/cources/workspace/aws_microservice_workspace/pythonSricptForLogCreation/subscriptionDatasWeb/subscription_data.csv'

@app.route('/')
def show_subscription_trends():
    # Load the CSV data
    df = pd.read_csv(csv_file)

    # Convert the 'Timestamp' column to a datetime type
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Set the start and end months (e.g., January to March)
    start_month = 1
    end_month = 6

    # Filter the DataFrame to include data only for the specified month range
    filtered_df = df[(df['Timestamp'].dt.month >= start_month) & (df['Timestamp'].dt.month <= end_month)]

    # Create a single figure
    _, ax = plt.subplots(figsize=(12, 6))

    # You can group the data by date and subscription type and count the number of subscriptions
    subscription_counts = filtered_df.groupby(['Timestamp', 'SubscriptionType'])['UserID'].count().unstack().fillna(0)

    # Plot the data on the existing figure
    subscription_counts.plot(kind='line', marker='o', ax=ax)

    # Set labels and title
    plt.xlabel('Date')
    plt.ylabel('Number of Subscriptions')
    plt.title('Subscription Trends Over Time')

    # Add a legend
    plt.legend(title='Subscription Type', loc='upper left')

    # Save the plot to a BytesIO object
    img = BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the plot as a base64 string for HTML rendering
    img_base64 = base64.b64encode(img.read()).decode()

    # Close the plot to release resources
    plt.close()

    return render_template('subscription_trends.html', img_base64=img_base64)

if __name__ == '__main__':
    # Run the app on port 80 (requires administrative access)
    app.run(debug=True, host='0.0.0.0', port=80)
