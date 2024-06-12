create database  if not exists nike;
drop database nike;
use nike;
drop table Productos;
CREATE TABLE PaginasWeb (
    ID_PaginaWeb INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE Productos (
    ID_Producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    género VARCHAR(50) NOT NULL,
    ID_PaginaWeb INT,
    FOREIGN KEY (ID_PaginaWeb) REFERENCES PaginasWeb(ID_PaginaWeb)
);

CREATE TABLE Calificaciones (
    ID_Calificación INT AUTO_INCREMENT PRIMARY KEY,
    calificación varchar(150)null ,
    opiniones varchar(150) null
);

CREATE TABLE Precios (
    ID_Precio INT AUTO_INCREMENT PRIMARY KEY,
    precio int
);

CREATE TABLE Opiniones (
    ID_Opinión INT AUTO_INCREMENT PRIMARY KEY,
    ID_Producto INT,
    ID_Calificación INT,
    ID_Precio INT,
    ID_PaginaWeb INT,
    FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto),
    FOREIGN KEY (ID_Calificación) REFERENCES Calificaciones(ID_Calificación),
    FOREIGN KEY (ID_Precio) REFERENCES Precios(ID_Precio),
    FOREIGN KEY (ID_PaginaWeb) REFERENCES PaginasWeb(ID_PaginaWeb)
);
SELECT
    pw.nombre AS NombrePaginaWeb,
    p.nombre AS NombreProducto,
    p.género AS GeneroProducto,
    c.calificación AS Calificacion,
    c.opiniones AS Opiniones,
    pr.precio AS Precio
FROM
    Opiniones o
JOIN
    Productos p ON o.ID_Producto = p.ID_Producto
JOIN
    Calificaciones c ON o.ID_Calificación = c.ID_Calificación
JOIN
    Precios pr ON o.ID_Precio = pr.ID_Precio
JOIN
    PaginasWeb pw ON o.ID_PaginaWeb = pw.ID_PaginaWeb;

select * from productos;
select * from Precios;
select * from Calificaciones;
select * from Opiniones;
