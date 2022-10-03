SELECT m.id, a.name, c.actor_character, d.name, m.title FROM `credits` AS c
JOIN actors AS a
ON a.id = c.actor_id
JOIN department AS d
ON d.id = c.department_id
JOIN movies AS m
ON m.id = c.movie_id;

SET GLOBAL foreign_key_checks=0;