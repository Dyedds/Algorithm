WITH EmployeeScores AS (
    SELECT 
        b.EMP_NO, 
        b.EMP_NAME, 
        b.POSITION, 
        b.EMAIL, 
        SUM(c.SCORE) AS SCORE
    FROM 
        HR_EMPLOYEES b
    JOIN 
        HR_GRADE c 
    ON b.EMP_NO = c.EMP_NO
    WHERE 
        c.YEAR = 2022
    GROUP BY 
        b.EMP_NO, 
        b.EMP_NAME, 
        b.POSITION, 
        b.EMAIL
)
SELECT 
    es.SCORE, 
    es.EMP_NO, 
    es.EMP_NAME, 
    es.POSITION, 
    es.EMAIL
FROM 
    EmployeeScores es
JOIN 
    (SELECT MAX(SCORE) AS MAX_SCORE FROM EmployeeScores) max_es
ON 
    es.SCORE = max_es.MAX_SCORE;
