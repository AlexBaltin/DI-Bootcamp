SELECT * FROM students;

UPDATE students SET birth_date = '02/11/1998' WHERE last_name = 'Benichou' AND first_name IN ('Lea', 'Marc');
UPDATE students SET last_name = 'Guez' WHERE first_name = 'David' AND last_name = 'Grez';

DELETE FROM students WHERE first_name = 'Lea' AND last_name = 'Benichou';

SELECT COUNT (*) FROM students;
SELECT COUNT (*) FROM students WHERE birth_date > '01/01/2000';

ALTER TABLE students
ADD COLUMN math_grade INTEGER;
UPDATE students SET math_grade = 80 WHERE id = 1;
UPDATE students SET math_grade = 90 WHERE id = 2 OR id = 4;
UPDATE students SET math_grade = 40 WHERE id = 6;
SELECT COUNT(*) FROM students WHERE math_grade > 83;

INSERT INTO students (first_name, last_name, birth_date, math_grade)
VALUES ('Omer', 'Simpson', '03/10/1980', 70);

SELECT first_name, last_name, COUNT (math_grade) AS total_grade FROM students GROUP BY first_name, last_name; 

SELECT COUNT(math_grade) FROM students;
