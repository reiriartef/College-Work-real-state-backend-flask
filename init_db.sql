CREATE TABLE Inmueble (
    ID_inmueble SERIAL PRIMARY KEY,
    Direccion VARCHAR(255),
    Ciudad VARCHAR(100),
    Estado VARCHAR(100),
    Codigo_Postal VARCHAR(20),
    Tipo_Inmueble VARCHAR(50),
    Precio_Venta DECIMAL(18, 2),
    Estado_Inmueble VARCHAR(50) DEFAULT 'Disponible',
    Descripcion TEXT
);

CREATE TABLE Cliente (
    ID_cliente SERIAL PRIMARY KEY,
    Nombre VARCHAR(100),
    Apellido VARCHAR(100),
    Telefono VARCHAR(20),
    Email VARCHAR(100) UNIQUE,
    Tipo_Cliente VARCHAR(20),
    Direccion VARCHAR(255)
);

CREATE TABLE Agente (
    ID_agente SERIAL PRIMARY KEY,
    Nombre VARCHAR(100),
    Apellido VARCHAR(100),
    Telefono VARCHAR(20),
    Email VARCHAR(100) UNIQUE,
    Especializacion VARCHAR(20)
);

CREATE TABLE Transaccion (
    ID_transaccion SERIAL PRIMARY KEY,
    Fecha_Transaccion DATE,
    Tipo_Transaccion VARCHAR(20),
    Precio_Transaccion DECIMAL(18, 2),
    Estado_Transaccion VARCHAR(20) DEFAULT 'En Proceso',
    ID_inmueble INT REFERENCES Inmueble (ID_inmueble),
    ID_cliente_comprador INT REFERENCES Cliente (ID_cliente),
    ID_cliente_vendedor INT REFERENCES Cliente (ID_cliente),
    ID_agente INT REFERENCES Agente (ID_agente)
);

CREATE TABLE Pago (
    ID_pago SERIAL PRIMARY KEY,
    Fecha_Pago DATE,
    Monto DECIMAL(18, 2),
    Metodo_Pago VARCHAR(50),
    ID_transaccion INT REFERENCES Transaccion (ID_transaccion)
);