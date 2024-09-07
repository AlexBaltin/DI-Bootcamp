SELECT * FROM customer;
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customer;
SELECT DISTINCT create_date FROM customer;
SELECT * FROM customer ORDER BY first_name DESC;
SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;
SELECT * FROM address WHERE district LIKE 'Texas';
SELECT * FROM film WHERE film_id IN (15, 150);
SELECT * FROM film WHERE title IN ('Aladdin');
SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'Al%';
SELECT title, replacement_cost FROM film ORDER BY replacement_cost ASC LIMIT 10;
-- SELECT title, replacement_cost FROM film ORDER BY replacement_cost ASC 
SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date 
FROM customer 
INNER JOIN payment 
ON customer.customer_id = payment.customer_id;

SELECT DISTINCT film.film_id, film.title, inventory.film_id
FROM film
LEFT JOIN inventory
ON film.film_id = inventory.film_id
WHERE inventory.film_id IS NULL;

SELECT city.city, country.country
FROM city
JOIN country
ON city.country_id = country.country_id;

SELECT payment.staff_id, customer.customer_id, customer.first_name, customer.last_name , payment.amount, payment.payment_date
FROM payment
INNER JOIN customer 
ON customer.customer_id = payment.customer_id
ORDER BY staff_id ASC;

SELECT COUNT(*) 
FROM payment
INNER JOIN customer
ON customer.customer_id = payment.customer_id;
