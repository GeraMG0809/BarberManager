USE barber_Manager;

CREATE TABLE Usuario(

    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL,
    correo_electronico VARCHAR(35) NOT NULL,
    contraseña VARCHAR(12) NOT NULL,
    estado ENUM('Activo', 'Inactivo') NOT NULL DEFAULT 'Activo' 
);


CREATE TABLE Barbero(

    id_barbero INT AUTO_INCREMENT PRIMARY KEY,
    nombre_barbero VARCHAR(25) NOT NULL,
    telefono VARCHAR(12) NOT NULL,
    imagenes VARCHAR(50) NOT NULL
);

CREATE TABLE Comentarios(
    id_comentario INT AUTO_INCREMENT PRIMARY KEY, 
    id_barbero INT NOT NULL,
    comentario  TEXT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_Barbero) REFERENCES Barbero(id_Barbero)
);


CREATE TABLE Cita(
    id_cita INT AUTO_INCREMENT PRIMARY KEY,
    id_barbero INT NOT NULL,
    id_usuario INT NOT NULL,
    hora_cita TIME NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_barbero) REFERENCES Barbero(id_Barbero),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE  Productos(

    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    categoria VARCHAR(15) NOT NULL,
    precio FLOAT NOT NULL,
    estado ENUM('ACTIVO','INACTIVO') NOT NULL DEFAULT 'ACTIVO'
);

CREATE TABLE Ventas(
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_cita  INT NOT NULL,
    id_producto INT NOT NULL,
    fecha TIMESTAMP NOT NULL,
    tipo_pago INT NOT NULL,
    estado ENUM('ACTIVO','INACTIVO') NOT NULL DEFAULT 'ACTIVO',
    FOREIGN KEY (id_cita) REFERENCES Cita(id_cita),
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);