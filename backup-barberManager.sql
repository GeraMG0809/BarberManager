-- MySQL dump 10.13  Distrib 8.0.41, for Linux (x86_64)
--
-- Host: localhost    Database: barberManager
-- ------------------------------------------------------
-- Server version	8.0.41-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Barbero`
--

DROP TABLE IF EXISTS `Barbero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Barbero` (
  `id_barbero` int NOT NULL AUTO_INCREMENT,
  `nombre_barbero` varchar(25) NOT NULL,
  `telefono` varchar(12) NOT NULL,
  `imagenes` varchar(100) NOT NULL,
  `estado` enum('ACTIVO','INACTIVO') NOT NULL DEFAULT 'ACTIVO',
  PRIMARY KEY (`id_barbero`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Barbero`
--

LOCK TABLES `Barbero` WRITE;
/*!40000 ALTER TABLE `Barbero` DISABLE KEYS */;
INSERT INTO `Barbero` VALUES (1,'Juan Perez','3355760127','team-1.png','ACTIVO'),(2,'Carlos Rodriguez','3322473597','team-2.png','ACTIVO'),(3,'Mario Gomez','3331262513','team-3.png','ACTIVO');
/*!40000 ALTER TABLE `Barbero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cita`
--

DROP TABLE IF EXISTS `Cita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cita` (
  `id_cita` int NOT NULL AUTO_INCREMENT,
  `id_barbero` int NOT NULL,
  `id_usuario` int NOT NULL,
  `id_servicio` int NOT NULL,
  `hora_cita` time NOT NULL,
  `fecha` date NOT NULL,
  `estado` enum('PENDIENTE','FINALIZADA','CANCELADA') NOT NULL DEFAULT 'PENDIENTE',
  PRIMARY KEY (`id_cita`),
  KEY `id_servicio` (`id_servicio`),
  KEY `id_barbero` (`id_barbero`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `Cita_ibfk_1` FOREIGN KEY (`id_servicio`) REFERENCES `Servicios` (`id_servicio`),
  CONSTRAINT `Cita_ibfk_2` FOREIGN KEY (`id_barbero`) REFERENCES `Barbero` (`id_barbero`),
  CONSTRAINT `Cita_ibfk_3` FOREIGN KEY (`id_usuario`) REFERENCES `Usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cita`
--

LOCK TABLES `Cita` WRITE;
/*!40000 ALTER TABLE `Cita` DISABLE KEYS */;
INSERT INTO `Cita` VALUES (1,1,1,1,'15:00:00','2025-03-29','PENDIENTE'),(2,1,4,1,'15:00:00','2025-04-02','PENDIENTE'),(3,2,1,1,'16:00:00','2025-04-30','PENDIENTE'),(4,2,1,1,'16:00:00','2025-04-30','PENDIENTE'),(5,1,1,1,'17:00:00','2025-05-14','PENDIENTE');
/*!40000 ALTER TABLE `Cita` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Comentarios`
--

DROP TABLE IF EXISTS `Comentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Comentarios` (
  `id_comentario` int NOT NULL AUTO_INCREMENT,
  `id_barbero` int NOT NULL,
  `comentario` text NOT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_comentario`),
  KEY `id_barbero` (`id_barbero`),
  CONSTRAINT `Comentarios_ibfk_1` FOREIGN KEY (`id_barbero`) REFERENCES `Barbero` (`id_barbero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comentarios`
--

LOCK TABLES `Comentarios` WRITE;
/*!40000 ALTER TABLE `Comentarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `Comentarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Productos`
--

DROP TABLE IF EXISTS `Productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Productos` (
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(30) NOT NULL,
  `precio` float NOT NULL,
  `estado` enum('ACTIVO','INACTIVO') NOT NULL DEFAULT 'ACTIVO',
  `Nombre_producto` varchar(30) NOT NULL,
  `imagen_producto` varchar(100) NOT NULL,
  PRIMARY KEY (`id_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Productos`
--

LOCK TABLES `Productos` WRITE;
/*!40000 ALTER TABLE `Productos` DISABLE KEYS */;
INSERT INTO `Productos` VALUES (7,'Estilizado',120,'ACTIVO','Cera para cabello','product-8.jpg'),(8,'Cuidado capilar',85.5,'ACTIVO','Shampoo nutritivo','product-1.jpg'),(9,'Estilizado',95,'ACTIVO','Balsamo para barba','product-2.jpg'),(10,'Cuidado de barba',150,'INACTIVO','Aceite para barba','product-3.jpg'),(11,'Cuidado de barba',110,'ACTIVO','Kit de cuidado de barba','product-4.jpg'),(12,'Cuidado de barba',249,'ACTIVO','Kit de afeitar','product-5.jpg'),(13,'Estilizado',249,'ACTIVO','Cera para el cabello','product-6.jpg'),(14,'Cuidado de barba',249,'ACTIVO','Kit de cepillos','product-7.jpg');
/*!40000 ALTER TABLE `Productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Servicios`
--

DROP TABLE IF EXISTS `Servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Servicios` (
  `id_servicio` int NOT NULL AUTO_INCREMENT,
  `servicios` varchar(50) NOT NULL,
  `precio` float NOT NULL,
  `estado` enum('ACTIVO','INACTIVO') NOT NULL DEFAULT 'ACTIVO',
  `nombre_servicio` varchar(35) NOT NULL,
  PRIMARY KEY (`id_servicio`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Servicios`
--

LOCK TABLES `Servicios` WRITE;
/*!40000 ALTER TABLE `Servicios` DISABLE KEYS */;
INSERT INTO `Servicios` VALUES (1,'corte completo',130,'ACTIVO','Corte'),(2,'afeitado',100,'ACTIVO','afeitado'),(3,'paquete completo',200,'ACTIVO','paquete completo');
/*!40000 ALTER TABLE `Servicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuario`
--

DROP TABLE IF EXISTS `Usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Usuario` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(50) NOT NULL,
  `correo_electronico` varchar(35) NOT NULL,
  `contraseña` varchar(12) NOT NULL,
  `estado` enum('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
  `telefono_usuario` varchar(12) NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario`
--

LOCK TABLES `Usuario` WRITE;
/*!40000 ALTER TABLE `Usuario` DISABLE KEYS */;
INSERT INTO `Usuario` VALUES (1,'gabriel','gerardo.mercado2h@gmail.com','gerardo','Activo','3312278893'),(2,'perla','','','Activo',''),(3,'daniel','daniel.gac182@gmail.com','onepiece13','Activo','3339054714'),(4,'daniel','kevin.corredor.rondon@gmail.com','1234','Activo','3123238947'),(5,'Diego','wero@gmail.com','wero123','Activo','3355877159'),(6,'liza','eli@gmail.com','liza2005','Activo','331579875'),(7,'prueba','prueba@gmail.com','prueba','Activo','4857469116'),(8,'prueba2','prueba2@gmail.com','prueba','Activo','5486759873');
/*!40000 ALTER TABLE `Usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ventas`
--

DROP TABLE IF EXISTS `Ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ventas` (
  `id_venta` int NOT NULL AUTO_INCREMENT,
  `id_cita` int NOT NULL,
  `fecha` timestamp NOT NULL,
  `tipo_pago` int NOT NULL,
  `monto_final` float NOT NULL,
  `estado` enum('ACTIVO','INACTIVO') NOT NULL DEFAULT 'ACTIVO',
  PRIMARY KEY (`id_venta`),
  KEY `id_cita` (`id_cita`),
  CONSTRAINT `Ventas_ibfk_1` FOREIGN KEY (`id_cita`) REFERENCES `Cita` (`id_cita`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ventas`
--

LOCK TABLES `Ventas` WRITE;
/*!40000 ALTER TABLE `Ventas` DISABLE KEYS */;
/*!40000 ALTER TABLE `Ventas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-12  5:02:18
