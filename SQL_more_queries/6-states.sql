-- creates the states table
CREATE DATABASE IF NOT EXISTS hbtn_od_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id),
    name VARCHAR(256) NOT NULL
);
