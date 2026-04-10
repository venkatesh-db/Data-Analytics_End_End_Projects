# Project Flow and Code Execution Guide

## Overview
This document provides a clear and concise explanation of the project flow and code execution for the ETL pipeline. It is designed to help developers quickly understand and recall the functionality of the code.

---

## Project Flow

### 1. **ETL Pipeline Overview**
The ETL (Extract, Transform, Load) pipeline processes production log data stored in the `api_logs` table of the MySQL database. The processed data is aggregated and stored in the `analytics_logs` table for analytics purposes.

### 2. **Execution Steps**
1. **Table Creation**:
   - Ensures the `api_logs` table exists before processing.
2. **Data Extraction**:
   - Extracts data from the `api_logs` table in chunks for efficient processing.
3. **Data Transformation**:
   - Cleans, categorizes, and enriches the data for analysis.
4. **Data Aggregation**:
   - Groups and summarizes the data by service name and date.
5. **Data Loading**:
   - Inserts or updates the aggregated data into the `analytics_logs` table.

---

## Code Flow Summary

### 1. **Main Script**
- The script starts by ensuring the `api_logs` table exists.
- It then runs the ETL pipeline, which orchestrates the extraction, transformation, aggregation, and loading of data.

### 2. **Functions**

#### a. **Table Creation**
- Creates the `api_logs` table if it does not exist.
- Adds indexes on `created_at` and `service_name` for faster queries.

#### b. **ETL Pipeline**
- Executes the pipeline in the following steps:
  1. Extracts data from the `api_logs` table using a SQL query.
  2. Processes data in chunks to handle large datasets efficiently.
  3. Transforms the data by cleaning null values, categorizing errors, and extracting date/hour information.
  4. Aggregates the data to calculate metrics like total requests, failure counts, error rates, and peak hours.
  5. Loads the aggregated data into the `analytics_logs` table using an UPSERT query.

#### c. **Data Extraction**
- Uses Pandas to fetch data in chunks from the database.
- Ensures the database connection is properly closed after extraction.

#### d. **Data Transformation**
- Drops invalid records (e.g., null values).
- Converts timestamps to a standard format.
- Categorizes status codes into success, client errors, server errors, or others.
- Extracts date and hour fields for aggregation.

#### e. **Data Aggregation**
- Groups data by service name and date.
- Calculates metrics such as:
  - Total requests.
  - Failure counts and error rates.
  - 95th percentile latency.
  - Peak traffic hours.

#### f. **Data Loading**
- Inserts or updates aggregated data into the `analytics_logs` table.
- Uses an UPSERT query to handle duplicate records efficiently.

---

## Key Points for Developers
- **Chunk Size**: Defined as `CHUNK_SIZE = 50000` for efficient processing.
- **Database Connection**: Managed using `mysql.connector` and SQLAlchemy.
- **Error Handling**: Ensure robust exception handling for production use.
- **Logging**: Logs are configured for monitoring pipeline execution.

---

## Quick Reference
- **Source Table**: `api_logs`
- **Target Table**: `analytics_logs`
- **Pipeline Functions**: `create_api_logs_table`, `etl_pipeline`, `extract_data`, `transform_data`, `aggregate_data`, `load_data`

---

For any issues or enhancements, refer to the code comments and logs for debugging.