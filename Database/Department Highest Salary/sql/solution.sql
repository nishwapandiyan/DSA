SELECT departmentId, name, MAX(salary)
FROM Employee
GROUP BY departmentId;