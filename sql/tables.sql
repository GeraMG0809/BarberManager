USE barber_Manager;

CREATE TABLE Usuario(

    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL,
    telefono_usuario VARCHAR(12) NOT NULL,
    correo_electronico VARCHAR(35) NOT NULL,
    contraseña VARCHAR(12) NOT NULL,
    estado ENUM('Activo', 'Inactivo') NOT NULL DEFAULT 'Activo' 
    
);


CREATE TABLE Barbero (
    id_barbero INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre_barbero VARCHAR(25) NOT NULL,
    telefono VARCHAR(12) NOT NULL,
    imagenes VARCHAR(100) NOT NULL,
    estado ENUM('ACTIVO', 'INACTIVO') NOT NULL DEFAULT 'ACTIVO'
);


CREATE TABLE Comentarios (
    id_comentario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_barbero INT NOT NULL,
    comentario TEXT NOT NULL,
    fecha TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE Cita (
    id_cita INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_barbero INT NOT NULL,
    id_usuario INT NOT NULL,
    id_servicio INT NOT NULL,
    hora_cita TIME NOT NULL,
    fecha DATE NOT NULL,
    estado ENUM('PENDIENTE', 'FINALIZADA', 'CANCELADA') NOT NULL DEFAULT 'PENDIENTE',
    FOREIGN KEY (id_barbero) REFERENCES Barbero(id_barbero),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_servicio) REFERENCES Servicios(id_servicio)
);


CREATE TABLE Productos (
    id_producto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    categoria VARCHAR(30) NOT NULL,
    precio FLOAT NOT NULL,
    estado ENUM('ACTIVO', 'INACTIVO') NOT NULL DEFAULT 'ACTIVO',
    Nombre_producto VARCHAR(30) NOT NULL,
    imagen_producto VARCHAR(100) NOT NULL
);


CREATE TABLE Servicios (
    id_servicio INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    servicios VARCHAR(50) NOT NULL,
    precio FLOAT NOT NULL,
    estado ENUM('ACTIVO', 'INACTIVO') NOT NULL DEFAULT 'ACTIVO',
    nombre_servicio VARCHAR(35) NOT NULL
);

CREATE TABLE Ventas (
    id_venta INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_cita INT NOT NULL,
    fecha TIMESTAMP NOT NULL,
    tipo_pago INT NOT NULL,
    monto_final FLOAT NOT NULL,
    estado ENUM('ACTIVO', 'INACTIVO') NOT NULL DEFAULT 'ACTIVO',
    FOREIGN KEY (id_cita) REFERENCES Cita(id_cita)
);
