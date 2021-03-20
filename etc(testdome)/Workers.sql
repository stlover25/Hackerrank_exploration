-- Write only the SQL statement that solves the problem and nothing else.

SELECT A.name
FROM employees AS A
WHERE A.id NOT IN (SELECT B.managerId 
                   FROM employees AS B
                  WHERE B.managerId NOT NULL);
