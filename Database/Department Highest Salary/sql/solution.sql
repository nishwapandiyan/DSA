SELECT departmentId, MAX(salary)
FROM Employee
GROUP BY departmentId;