-- a script that lists all the cities of California 
    USE hbtn_0d_usa;
 SELECT *
   FROM cities
  WHERE state_id = (
	SELECT id 
	  FROM states 
	 WHERE name = "California"
   )
ORDERED BY id;