# ETL Pipeline for Production Logs Analysis

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline to process production logs stored in a MySQL database. The pipeline extracts data from a `production_logs` table, transforms it to calculate analytics metrics, and loads the results into an `analytics_logs` table.

## Project Structure
- **etl_pipeline.py**: Python script implementing the ETL pipeline.
- **schema.sql**: SQL file defining the schema for `production_logs` and `analytics_logs` tables.
- **requirements.txt**: Python dependencies for the project.

## Database Schema
### Source Table: `production_logs`
| Column Name    | Data Type       | Description                       |
|----------------|-----------------|-----------------------------------|
| id             | INT (Primary Key) | Auto-incremented ID              |
| service_name   | VARCHAR(255)    | Name of the service              |
| response_time_ms | INT           | Response time in milliseconds    |
| error_code     | INT             | Error code (if any)              |
| created_at     | DATETIME        | Record creation timestamp        |
| updated_at     | DATETIME        | Record update timestamp          |

### Target Table: `analytics_logs`
| Column Name    | Data Type       | Description                       |
|----------------|-----------------|-----------------------------------|
| service_name   | VARCHAR(255)    | Name of the service              |
| date           | DATE            | Date of the analytics data       |
| total_requests | INT             | Total number of requests         |
| failures       | INT             | Number of failed requests        |
| avg_latency    | FLOAT           | Average response time (ms)       |
| error_rate     | FLOAT           | Failure rate (percentage)        |

## Steps to Run the Project

### 1. Set Up the Environment
1. Install MySQL and ensure it is running.
2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### 2. Set Up the Database
1. Start the MySQL server:
   ```bash
   sudo mysql.server start
   ```
2. Create the databases and tables:
   ```bash
   mysql -u root -p'Th36under!' -e "CREATE DATABASE source_db; CREATE DATABASE analytics_db;"
   mysql -u root -p'Th36under!' source_db < schema.sql
   mysql -u root -p'Th36under!' analytics_db < schema.sql
   ```

### 3. Insert Test Data
1. Insert sample data into `production_logs`:
   ```sql
   USE source_db;
   INSERT INTO production_logs (service_name, response_time_ms, error_code, created_at, updated_at)
   VALUES
   ('ServiceA', 120, 500, NOW() - INTERVAL 2 HOUR, NOW() - INTERVAL 2 HOUR),
   ('ServiceB', 200, NULL, NOW() - INTERVAL 1 HOUR, NOW() - INTERVAL 1 HOUR);
   ```
2. Insert sample data into `analytics_logs`:
   ```sql
   USE analytics_db;
   INSERT INTO analytics_logs (service_name, date, total_requests, failures, avg_latency, error_rate)
   VALUES
   ('ServiceA', CURDATE(), 100, 5, 150.0, 0.05),
   ('ServiceB', CURDATE(), 200, 0, 180.0, 0.0);
   ```

### 4. Run the ETL Pipeline
1. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
2. Execute the ETL pipeline:
   ```bash
   python etl_pipeline.py
   ```

### 5. Verify the Results
1. Check the `analytics_logs` table for updated data:
   ```bash
   mysql -u root -p'Th36under!' -e "USE analytics_db; SELECT * FROM analytics_logs;"
   ```

## Code Flow Summary

This section provides an overview of the ETL pipeline's code flow, which can be useful for understanding the implementation or explaining it during an interview.

### Code Flow
1. **Database Configuration**:
   - The script defines connection details for the source (`source_db`) and target (`analytics_db`) databases.
   - These configurations are stored in `SOURCE_DB_CONFIG` and `TARGET_DB_CONFIG` dictionaries.

2. **Extract Data**:
   - The `extract_data(last_updated)` function connects to the `source_db` database and retrieves rows from the `production_logs` table where `updated_at` is greater than the specified `last_updated` timestamp.
   - The data is returned as a pandas DataFrame.

3. **Transform Data**:
   - The `transform_data(df)` function processes the extracted data:
     - Cleans null values.
     - Converts `created_at` and `updated_at` columns to datetime format.
     - Categorizes error codes into `Client Error`, `Server Error`, or `Other`.
     - Aggregates metrics such as total requests, failures, average latency, and error rate.
     - Renames the `created_at` column to `date` for consistency.

4. **Load Data**:
   - The `load_data(df)` function connects to the `analytics_db` database and inserts the transformed data into the `analytics_logs` table.
   - If a row with the same `service_name` and `date` already exists, it updates the existing row with the new metrics.

5. **ETL Pipeline Execution**:
   - The `etl_pipeline()` function orchestrates the entire process:
     - Sets the `last_updated` timestamp to 24 hours ago.
     - Calls `extract_data` to fetch data from the source database.
     - Calls `transform_data` to process the extracted data.
     - Calls `load_data` to insert the transformed data into the target database.

6. **Script Entry Point**:
   - The script runs the `etl_pipeline()` function when executed directly.

### Key Points for Interviews
- **Purpose**: The ETL pipeline automates the process of extracting, transforming, and loading data for analytics.
- **Technologies Used**: Python, pandas, MySQL.
- **Design Decisions**:
  - Used pandas for data transformation due to its powerful aggregation and manipulation capabilities.
  - Implemented `ON DUPLICATE KEY UPDATE` in SQL to handle upserts efficiently.
- **Error Handling**: Basic error handling is implemented via pandas' `dropna` and SQL's `ON DUPLICATE KEY UPDATE`.
- **Scalability**: The pipeline can be extended to handle larger datasets by optimizing SQL queries and using batch processing.

This summary provides a high-level understanding of the ETL pipeline's functionality and design, making it easier to explain during discussions or interviews.

## Notes
- The ETL pipeline processes data updated in the last 24 hours from the `production_logs` table.
- Warnings related to pandas' `SettingWithCopyWarning` were observed during execution. These can be resolved by modifying the script to use `.loc` for DataFrame updates.

## Future Improvements
- Add logging to the ETL script for better debugging.
- Optimize the SQL queries for large datasets.
- Implement unit tests for the ETL pipeline.

## Author
Venkatesh

---