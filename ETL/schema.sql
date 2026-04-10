-- Schema for Source Table (Production Logs)
CREATE TABLE production_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(255) NOT NULL,
    response_time_ms INT,
    error_code INT,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

-- Schema for Analytics Table
CREATE TABLE analytics_logs (
    service_name VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    total_requests INT NOT NULL,
    failures INT NOT NULL,
    avg_latency FLOAT NOT NULL,
    error_rate FLOAT NOT NULL,
    PRIMARY KEY (service_name, date)
);