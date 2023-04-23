-- creates the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
       (id INT NOT NULL AUTO_INCREMENT FOREING KEY(state_id) REFERENCES states(id),
       	name varchar(256) NOT NULL);
