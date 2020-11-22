## 2. A Simple Question ##

SELECT MIN(Unemployment_rate) 
  FROM recent_grads;

## 3. Aggregate Functions ##

SELECT SUM(Total)
from recent_grads

## 4. Order of Execution ##

SELECT COUNT(Major)
  FROM recent_grads
 WHERE ShareWomen < 0.5;

## 5. Missing Values ##

SELECT COUNT(*), COUNT(Unemployment_rate)
  FROM recent_grads;

## 6. Combining Multiple Aggregation Functions ##

SELECT AVG(Total), MIN(Men), MAX(Women)
  FROM recent_grads;

## 7. Customizing the Results ##

SELECT COUNT(Major) as 'Number of Majors',MAX(Unemployment_rate) as 'Highest Unemployment Rate'
from recent_grads;

## 8. Counting Unique Values ##

SELECT COUNT(DISTINCT Major) as unique_majors , COUNT(DISTINCT Major_category) as unique_major_categories ,COUNT(DISTINCT Major_code) as unique_major_codes
 FROM recent_grads
 LIMIT 5;

## 10. String Functions and Operations ##

SELECT 'Major: ' || LOWER(Major) as Major, Total, Men, Women, Unemployment_rate,LENGTH(Major) as Length_of_name
  FROM recent_grads
 ORDER BY Unemployment_rate DESC

## 11. Performing Arithmetic in SQL ##

SELECT Major,Major_category ,P75th - P25th quartile_spread
  FROM recent_grads
ORDER BY quartile_spread asc
LIMIT 20