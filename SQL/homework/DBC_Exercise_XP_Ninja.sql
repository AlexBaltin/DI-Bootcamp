SELECT first_name, last_name FROM customers ORDER BY first_name DESC LIMIT 2;

SELECT customers.id FROM customers WHERE first_name = 'Scott';

DELETE FROM purchases 
WHERE customer_id = (SELECT customers.id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott' );

SELECT * FROM customers
LEFT JOIN purchases ON purchases.customer_id = customers.id;

SELECT * FROM customers
INNER JOIN purchases ON purchases.customer_id = customers.id;

