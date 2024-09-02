SELECT first_name, last_name, birth_date FROM students;
SELECT first_name, last_name, birth_date FROM students ORDER BY last_name LIMIT 4;
SELECT first_name, last_name, birth_date FROM students ORDER BY birth_date DESC LIMIT 1;
SELECT first_name, last_name, birth_date FROM students OFFSET 2 LIMIT 3;


