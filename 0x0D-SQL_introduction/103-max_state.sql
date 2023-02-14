-- displays the max temperature of each state (ordered by State name).
SELECT `city`, AVG(`value`) AS `max_temp` FROM `temperatures` GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;
