SELECT * FROM film; 

SELECT COUNT(*) FROM film WHERE rating = 'G';
SELECT COUNT(*) FROM film WHERE rating = 'PG';
SELECT COUNT(*) FROM film WHERE rating = 'PG-13';
SELECT COUNT(*) FROM film WHERE rating = 'R';
SELECT COUNT(*) FROM film WHERE rating = 'NC-17';

-- SELECT * FROM film WHERE (rating = 'G' OR rating = 'PG-13') AND length < 120;

SELECT * FROM film WHERE rating IN ('G', 'PG-13') AND length < 120 AND rental_rate < 3 ORDER BY title ASC;

SELECT * FROM customer;
UPDATE customer SET first_name = 'Alex', last_name = 'Baltin' WHERE first_name = 'Jared' AND last_name = 'Ely'; 
UPDATE customer SET address_id = 1 WHERE last_name = 'Baltin';