

SELECT veh_reg, COUNT(*)
	FROM mot
	WHERE pass = False
	GROUP BY veh_reg
	ORDER BY COUNT(*) DESC;
	
	
	
SELECT veh_reg, COUNT(*)
	FROM mot
	WHERE pass = False
	GROUP BY veh_reg
	ORDER BY COUNT(*) DESC;
	
	
	
select *
from repair
where veh_reg = "AW61 BRE";
