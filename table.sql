SELECT name, city,
    (SELECT DATEDIFF(date_last, date_first)+1) AS Длительность
FROM trip
WHERE city <> 'Москва' && city <> 'Санкт-Петербург'
ORDER BY Длительность DESC, city DESC