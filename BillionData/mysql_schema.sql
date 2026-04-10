-- Source Table: api_logs
CREATE TABLE api_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(255) NOT NULL,
    status_code INT NOT NULL,
    response_time FLOAT NOT NULL,
    created_at DATETIME NOT NULL,
    INDEX idx_created_at (created_at),
    INDEX idx_service_name (service_name)
);

-- Analytics Table: analytics_table
CREATE TABLE analytics_table (
    service_name VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    total_requests INT NOT NULL,
    failures INT NOT NULL,
    error_rate FLOAT NOT NULL,
    p95_latency FLOAT NOT NULL,
    peak_hour INT NOT NULL,
    PRIMARY KEY (service_name, date)
);