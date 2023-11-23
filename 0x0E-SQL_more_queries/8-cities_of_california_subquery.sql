-- Script to list all cities in California without using JOIN

USE hbtn_0d_usa;

SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
