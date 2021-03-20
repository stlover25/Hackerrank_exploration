with temp as (
SELECT regions.name as name, coalesce(SUM(sales.amount)/COUNT(DISTINCT employees.id), 0) AS average 
FROM regions
LEFT JOIN states ON states.regionId = regions.id
LEFT JOIN employees ON states.id = employees.stateId
LEFT JOIN sales ON sales.employeeId = employees.id
GROUP BY regions.name
  )

  SELECT temp.name, temp.average, (select MAX(temp.average) from temp)-average
  
  FROM temp;
