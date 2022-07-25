Object-Oriented Architecture/Design Problem

Goal: Simple Aircraft Manufacturing Facility System
Example: Boeing Manufacturing Facility in Everett, Washington

--Aircraft consist of make, model, up to 2 engines and passenger capacity.

CREATE TABLE AIRCRAFT (id NUMBER, engine_id INT, capacity INT, engine_cnt INT)

--Engines have make, model and maximum flying range in miles.

CREATE TABLE ENGINES (id NUMBER, make VARCHAR2, model VARCHAR2, max_miles NUMBER)

--Hangars consist of hangar name (e.g. B-52), aircraft capacity and up to 100 workers.

CREATE TABLE HANGARS (id NUMBER, name VARCHAR2, capacity INT, max_miles NUMBER)


--Workers have first name, last name, SSN, aircraft specialization(s) and years of experience.

CREATE TABLE WORKERS (id NUMBER, first_name VARCHAR2,last_name VARCHAR, SSN VARCHAR2, aircraft_spec INT,
years_of_experience INT)



Tech Stack: Oracle DB, Python backend application and JavaScript frontend application.

Database
Table and column name/s
Primary and foreign key/s




CREATE TABLE Employee (id INT, name VARCHAR2, manager_id INT)
INSERT INTO Employee (1, 'TOP BOSS', NULL);
INSERT INTO Employee (2, 'Manager', 1);
INSERT INTO Employee (3, 'Employee 1', 2);


Employee(eid INT)
Position(pid INT)

CREATE TABLE Reference (eid INT, pid INT)





