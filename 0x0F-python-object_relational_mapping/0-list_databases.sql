-- a script that lists all databases of your MySQL serve
-- because Batch 3 is the best!
SELECT * FROM cities INNER JOIN states WHERE cities.state_id = states.id;