 SELECT VERSION(), CURRENT_DATE;
----------------------------------
 SELECT (4+1)*5;
---------------------------------
 SELECT NOW();
-- -------------------------
 SELECT CURRENT_DATE()
 ,
 CURRENT_TIME();

 -------------------------------------
 SHOW DATABASES; --USE TO SHOW ALL DATABASE

 --- HOW TO CREATE DATABASE 

 CREATE DATABASE DATABASE_NAME;
 --EX
 CREATE DATABASE PY8

 --- HOW TO Delete DATABASE 

DROP DATABASE DATABASE_NAME 
--EX
 DROP DATABASE PY8

 SHOW TABLES; --USE TO SHOW TABLE 

 --- HOW TO CREATE TABLE

 CREATE TABLE TABLE_name() 
 --ex
 CREATE TABLE student(
    id int primary key auto_increament,
    name varchar(128),
    std int ,
    email varchar(128),
    number varchar(10),
    dob date
 ); 

DESCRIBE student; --To view a table structure,

  
 --- HOW TO Delete table

 DROP TABLE TABLE_name;

-- EX 
DROP TABLE PY8;


-- insert 
 
INSERT INTO TABLE_NAME (PROPARTI1,PROPARTI2,PROPARTI3,PROPARTI4...N) VALUES (VALUE1,VALUE2,VALUE3,VALUE4,...N)

--ex
INSERT INTO student (name,std,email,number,dob) VALUES('sahil',11,'sahilbelim@gmail.com','9924254332','2005-05-30')

INSERT INTO student  VALUES(2,'sahil',11,'sahilbelim@gmail.com','9924254332','2005-05-30')

-- UPDATE VALUE
UPDATE TABLE_NAME SET PROPARTI=new_value where PROPARTI= condition_value ;
--ex
UPDATE student SET dob='2005-05-30' where id= 1 ;

--Delete

Delete FROM TABLE_NAME where PROPARTI=condition_value;

Delete FROM student where id=2;