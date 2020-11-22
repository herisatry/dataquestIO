## 1. Introducing Joins ##

SELECT *
FROM facts f
INNER JOIN cities c ON c.facts_id = f.id
LIMIT 10

## 2. Understanding Inner Joins ##

SELECT c.*, f.name as country_name
FROM facts f
INNER JOIN cities c ON c.facts_id = f.id
LIMIT 5

## 3. Practicing Inner Joins ##

SELECT f.name as country, c.name as capital_city 
FROM facts f
INNER JOIN cities c ON c.facts_id = f.id
WHERE c.capital = 1

## 4. Left Joins ##

SELECT f.name as country, f.population 
FROM facts f
LEFT JOIN cities c ON c.facts_id = f.id 
WHERE c.population IS NULL;

## 6. Finding the Most Populous Capital Cities ##

SELECT c.name as capital_city,f.name as country , c.population
FROM facts f
left JOIN cities c ON c.facts_id=f.id
where c.capital =1
ORDER BY 3 DESC
limit 10;

## 7. Combining Joins with Subqueries ##

SELECT c.name as capital_city,
f.name as country,
c.population
from facts f
INNER JOIN ( SELECT * 
            FROM cities
            WHERE population > 10000000 AND capital=1) c
            ON c.facts_id=f.id
ORDER BY 3 DESC;

## 8. Challenge: Complex Query with Joins and Subqueries ##

SELECT
    f.name country,
    c.urban_pop,
    f.population total_pop,
    (c.urban_pop / CAST(f.population AS FLOAT)) urban_pct
FROM facts f
INNER JOIN (
            SELECT
                facts_id,
                SUM(population) urban_pop
            FROM cities
            GROUP BY 1
           ) c ON c.facts_id = f.id
WHERE urban_pct > .5
ORDER BY 4 ASC;