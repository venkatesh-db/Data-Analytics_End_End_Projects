-- Top Failing Services by Error Rate
SELECT service_name, AVG(error_rate) AS avg_error_rate
FROM analytics_logs
GROUP BY service_name
ORDER BY avg_error_rate DESC
LIMIT 10;

-- High Latency Services (Avg Latency Spikes)
SELECT service_name, date, avg_latency
FROM analytics_logs
WHERE avg_latency > 1000  -- Example threshold
ORDER BY avg_latency DESC;

-- Peak Traffic Hours
SELECT service_name, date, COUNT(*) AS frequency
FROM analytics_logs
GROUP BY service_name, date
ORDER BY frequency DESC;