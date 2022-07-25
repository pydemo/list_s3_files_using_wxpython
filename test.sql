--

SELECT salary FROM (
    SELECT salary,  ROW_NUMBER() OVER (ORDER BY salary desc) srank
      FROM Emplyees
    ) v
WHERE v.srank=2 LIMIT 1;

--
WITH t_ranked as(
    SELECT salary,  ROW_NUMBER() OVER (ORDER BY salary desc) srank
      FROM Emplyees
    )
SELECT salary FROM t_ranked WHERE srank=2 LIMIT 1;  
