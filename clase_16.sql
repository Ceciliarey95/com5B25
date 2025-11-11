CREATE DATABASE tienda_conectada;

USE tienda_conectada;

CREATE TABLE cliente (
id INT auto_increment PRIMARY KEY,
nombre VARCHAR(45),
email VARCHAR(100),
telefono VARCHAR(20)
);

CREATE DATABASE banco;
USE banco;

CREATE TABLE cuenta (
id INT AUTO_INCREMENT PRIMARY KEY,
titular VARCHAR(100),
saldo DECIMAL(10,2)
);

INSERT INTO cuenta(titular,saldo) VALUES 
('Ana' , 1000),
('Juan', 500);

CREATE DATABASE test_db;