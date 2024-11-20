-- Script to display the average temperature (Fahrenheit) by city, ordered by temperature in descending order.
SELECT city, 
       AVG(temperature) AS average_temperature
FROM temperatures
GROUP BY city
ORDER BY average_temperature DESC;
