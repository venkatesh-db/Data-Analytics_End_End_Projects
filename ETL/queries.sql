-- Query to get daily error rates per service
SELECT 
    service_name, 
    date, 
    total_requests, 
    failures, 
    avg_latency, 
    error_rate
FROM analytics_logs
ORDER BY date DESC;

-- Query to get services with the highest failure rates
SELECT 
    service_name, 
    AVG(error_rate) AS avg_error_rate
FROM analytics_logs
GROUP BY service_name
ORDER BY avg_error_rate DESC
LIMIT 10;

-- Query to get average response time trends
SELECT 
    date, 
    AVG(avg_latency) AS avg_response_time
FROM analytics_logs
GROUP BY date
ORDER BY date;