WITH YearlyMaxSize AS (
    SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR,
           MAX(SIZE_OF_COLONY) AS MAX_SIZE
    FROM ECOLI_DATA
    GROUP BY YEAR(DIFFERENTIATION_DATE)
)
SELECT YEAR,
       (y.MAX_SIZE - e.SIZE_OF_COLONY) AS YEAR_DEV,
       e.ID
FROM ECOLI_DATA e
JOIN YearlyMaxSize y
ON YEAR(e.DIFFERENTIATION_DATE) = y.YEAR
ORDER BY YEAR, YEAR_DEV;
