CREATE DATABASE tienda_ejemplo;
USE tienda_ejemplo;

CREATE TABLE clientes (
id_cliente INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE
);

CREATE TABLE productos (
id_producto INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
precio DECIMAL(10,2) NOT NULL
);

CREATE TABLE ventas(
id_venta INT AUTO_INCREMENT PRIMARY KEY,
fecha DATE NULL,
id_cliente INT,
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE detalle_venta(
id_venta INT,
id_producto INT,
cantidad INT NOT NULL,
PRIMARY KEY (id_venta , id_producto),
FOREIGN KEY (id_venta) REFERENCES ventas(id_venta),
FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

INSERT INTO clientes (nombre, email) VALUES
('Ana','ana@gmail.com'),
('Marta','marta@gmail.com');

INSERT INTO productos (nombre, precio) VALUES
('Mouse', 350),
('Teclado',500),
('Monitor', 2500);

INSERT INTO ventas (fecha, id_cliente) VALUES
('2025-11-05', 3),
('2025-11-05', 4);

INSERT INTO detalle_venta VALUES
(1,1,20),
(2,1,50),
(1,3,25);

SELECT email AS EMAIL, nombre AS NOMBRE 
FROM clientes ;

SELECT * FROM productos ORDER BY precio DESC;

SELECT v.id_venta , v.fecha, c.nombre AS cliente
FROM ventas v
INNER JOIN clientes c 
ON v.id_cliente = c.id_cliente;

SELECT p.nombre, d.cantidad
FROM productos p 
LEFT JOIN detalle_venta d
ON p.id_producto = d.id_producto;

SELECT c.nombre AS cliente, v.id_venta
FROM clientes c
RIGHT JOIN ventas v
ON c.id_cliente = v.id_cliente;