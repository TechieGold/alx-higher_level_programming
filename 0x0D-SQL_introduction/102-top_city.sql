-- Displays the 3 cities with the highest average
-- temperatures between July and August.
SELECT city, AVG(value) AS arg_temp
FROM `temperatures`
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY arg_temp DESC
LIMIT 3;
