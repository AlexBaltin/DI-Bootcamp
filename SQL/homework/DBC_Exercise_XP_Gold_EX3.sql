CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity_purchased INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

SELECT * FROM purchases;
SELECT * FROM customers;
SELECT * FROM items;

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
		(SELECT id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'),
		(SELECT id FROM items WHERE name = 'Fan'),
		1
	);
	
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
		(SELECT id FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson'),
		(SELECT id FROM items WHERE name = 'Large Desk'),
		10
	);

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
		(SELECT id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'),
		(SELECT id FROM items WHERE name = 'Small Desk'),
		2
	);
	
SELECT * FROM purchases;

SELECT customers.first_name, customers.last_name, items.name, purchases.quantity_purchased, items.price FROM purchases 
INNER JOIN customers ON purchases.customer_id = customers.id
INNER JOIN items ON purchases.item_id = items.id;

SELECT * FROM purchases WHERE customer_id = 5;

SELECT items.name, purchases.quantity_purchased FROM purchases 
INNER JOIN items ON purchases.item_id = items.id 
WHERE items.name = 'Large Desk' OR items.name = 'Small Desk';

SELECT customers.first_name, customers.last_name, items.name FROM purchases 
INNER JOIN customers ON purchases.customer_id = customers.id
INNER JOIN items ON purchases.item_id = items.id;


INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
		(SELECT id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'),
		NULL,
		1
	);
--  It doesnt work because when we created a table we wrote that it can not be NULL
