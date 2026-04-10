import mysql.connector
import pandas as pd
from datetime import datetime, timedelta

# Database connection details
SOURCE_DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Th36under!',
    'database': 'source_db'
}

TARGET_DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Th36under!',
    'database': 'analytics_db'
}

# Extract function
def extract_data(last_updated):
    connection = mysql.connector.connect(**SOURCE_DB_CONFIG)
    cursor = connection.cursor(dictionary=True)

    query = (
        "SELECT id, service_name, response_time_ms, error_code, created_at, updated_at "
        "FROM production_logs WHERE updated_at > %s ORDER BY updated_at ASC"
    )

    cursor.execute(query, (last_updated,))
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return pd.DataFrame(rows)

# Transform function
def transform_data(df):
    if df.empty:
        return df

    # Clean null values
    df = df.dropna()

    # Standardize timestamps
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['updated_at'] = pd.to_datetime(df['updated_at'])

    # Categorize errors
    df['error_category'] = df['error_code'].apply(
        lambda x: 'Client Error' if 400 <= x < 500 else 'Server Error' if 500 <= x < 600 else 'Other'
    )

    # Aggregate metrics
    aggregated = df.groupby(['service_name', df['created_at'].dt.date]).agg(
        total_requests=('id', 'count'),
        failures=('error_code', lambda x: x.notnull().sum()),
        avg_latency=('response_time_ms', 'mean'),
        error_rate=('error_code', lambda x: x.notnull().sum() / len(x) * 100)
    ).reset_index()

    aggregated.rename(columns={'created_at': 'date'}, inplace=True)

    return aggregated

# Load function
def load_data(df):
    connection = mysql.connector.connect(**TARGET_DB_CONFIG)
    cursor = connection.cursor()

    for _, row in df.iterrows():
        query = (
            "INSERT INTO analytics_logs (service_name, date, total_requests, failures, avg_latency, error_rate) "
            "VALUES (%s, %s, %s, %s, %s, %s) "
            "ON DUPLICATE KEY UPDATE total_requests=VALUES(total_requests), failures=VALUES(failures), "
            "avg_latency=VALUES(avg_latency), error_rate=VALUES(error_rate)"
        )

        cursor.execute(query, (
            row['service_name'], row['date'], row['total_requests'],
            row['failures'], row['avg_latency'], row['error_rate']
        ))

    connection.commit()
    cursor.close()
    connection.close()

# Main ETL function
def etl_pipeline():
    last_updated = datetime.now() - timedelta(days=1)  # Example: fetch last 1 day of data

    # Extract
    data = extract_data(last_updated)

    # Transform
    transformed_data = transform_data(data)

    # Load
    load_data(transformed_data)

if __name__ == "__main__":
    etl_pipeline()