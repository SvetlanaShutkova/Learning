CREATE TABLE ordering AS
SELECT author, title, (SELECT round(AVG(amount)) FROM book) AS amount
FROM book
WHERE amount < (SELECT round(AVG(amount)) FROM book);
SELECT * FROM ordering;
