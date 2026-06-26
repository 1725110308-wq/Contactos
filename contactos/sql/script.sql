CREATE TABLE contacto(
    id_contacto integer primary key AUTOINCREMENT,
    nombre text not null,
    primer_apellido text not null,
    segundo_apellido text not null,
    email text not null,
    telefono text not null
);
INSERT INTO contacto(nombre,primer_apellido,segundo_apellido,email,telefono) 
VALUES
('tomas','perez','martinez','tom@gmail.com','1111111111'),
('roberto','vasquez','alvarado','beto@gmail.com','2222222222');
SELECT * FROM contacto;