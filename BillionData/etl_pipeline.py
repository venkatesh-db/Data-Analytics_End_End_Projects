import pandas as pd
import mysql.connector
from sqlalchemy import create_engine, text
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# MySQL connection details
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Th36under!'
MYSQL_DATABASE = 'analytics_db'

# Chunk size for processing
CHUNK_SIZE = 50000

# Create MySQL connection
def get_mysql_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

# Create SQLAlchemy engine for Pandas
def get_sqlalchemy_engine():
    return create_engine(f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}")

# Data extraction
def extract_data(query, chunksize):
    conn = get_mysql_connection()
    try:
        for chunk in pd.read_sql(query, conn, chunksize=chunksize):
            yield chunk
    finally:
        conn.close()

# Data transformation
def transform_data(chunk):
    # Clean null and invalid records
    chunk = chunk.dropna(subset=['service_name', 'status_code', 'response_time', 'created_at'])

    # Convert timestamps to standard datetime format
    chunk['created_at'] = pd.to_datetime(chunk['created_at'])

    # Categorize errors
    chunk['error_category'] = chunk['status_code'].apply(lambda x: 'Success' if 200 <= x < 300 else
                                                         'Client Error' if 400 <= x < 500 else
                                                         'Server Error' if 500 <= x < 600 else 'Other')

    # Extract date and hour for aggregation
    chunk['date'] = chunk['created_at'].dt.date
    chunk['hour'] = chunk['created_at'].dt.hour

    return chunk

# Data aggregation
def aggregate_data(chunk):
    # Group by service_name and date
    aggregated = chunk.groupby(['service_name', 'date']).agg(
        total_requests=('status_code', 'count'),
        failures=('error_category', lambda x: (x != 'Success').sum()),
        error_rate=('error_category', lambda x: round((x != 'Success').mean() * 100, 2)),
        p95_latency=('response_time', lambda x: x.quantile(0.95)),
        peak_hour=('hour', lambda x: x.value_counts().idxmax())
    ).reset_index()

    return aggregated

# Data loading
def load_data(aggregated_data, table_name):
    engine = get_sqlalchemy_engine()
    with engine.connect() as conn:
        for _, row in aggregated_data.iterrows():
            # UPSERT query
            upsert_query = f"""
            INSERT INTO {table_name} (service_name, date, total_requests, failures, error_rate, p95_latency, peak_hour)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                total_requests = VALUES(total_requests),
                failures = VALUES(failures),
                error_rate = VALUES(error_rate),
                p95_latency = VALUES(p95_latency),
                peak_hour = VALUES(peak_hour)
            """
            conn.execute(upsert_query, (
                row['service_name'], row['date'], row['total_requests'], row['failures'],
                row['error_rate'], row['p95_latency'], row['peak_hour']
            ))

# Update the create_api_logs_table function to use SQLAlchemy's text() for raw SQL queries
def create_api_logs_table():
    engine = get_sqlalchemy_engine()
    with engine.connect() as conn:
        create_table_query = text("""
        CREATE TABLE IF NOT EXISTS api_logs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            service_name VARCHAR(255) NOT NULL,
            status_code INT NOT NULL,
            response_time FLOAT NOT NULL,
            created_at DATETIME NOT NULL,
            INDEX idx_created_at (created_at),
            INDEX idx_service_name (service_name)
        )
        """)
        conn.execute(create_table_query)
        conn.commit()

# Main ETL pipeline
def etl_pipeline():
    logging.info("Starting ETL pipeline...")
    query = """
    SELECT service_name, status_code, response_time, created_at
    FROM api_logs
    WHERE created_at >= '2026-01-01'  -- Example for incremental load
    """
    for chunk in extract_data(query, CHUNK_SIZE):
        logging.info("Processing a new chunk...")
        transformed_chunk = transform_data(chunk)
        aggregated_data = aggregate_data(transformed_chunk)
        load_data(aggregated_data, 'analytics_table')
    logging.info("ETL pipeline completed successfully.")

if __name__ == "__main__":
    create_api_logs_table()  # Ensure the table is created before running the pipeline
    etl_pipeline()