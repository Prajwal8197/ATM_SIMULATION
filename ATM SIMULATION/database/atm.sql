CREATE DATABASE atm;

USE atm;

CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  face VARCHAR(255) NOT NULL,
  fingerprint VARCHAR(255) NOT NULL,
  balance INT NOT NULL,
  email VARCHAR(255),
  date_of_birth DATE,
  gender VARCHAR(255),
  country_of_residence VARCHAR(255),
  mobile_number VARCHAR(255),
  PRIMARY KEY (id)
);
