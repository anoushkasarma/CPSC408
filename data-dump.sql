-- MySQL dump 10.13  Distrib 8.3.0, for macos14.2 (x86_64)
--
-- Host: localhost    Database: RideShare
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `driver`
--

DROP TABLE IF EXISTS `driver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `driver` (
  `driverID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) NOT NULL,
  `Phone` varchar(10) DEFAULT NULL,
  `Mode` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`driverID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `driver`
--

LOCK TABLES `driver` WRITE;
/*!40000 ALTER TABLE `driver` DISABLE KEYS */;
INSERT INTO `driver` VALUES (1,'Bob Link','3035976142',0),(2,'Bret Sarma','3035976143',1),(3,'Sophia Bliss','3035976144',0),(4,'Ruby Link','3035976145',0),(5,'Jane Becker','3035976146',1),(6,'Eli Waeher ','3035976147',0),(7,'Leah Butler','3035976148',0),(8,'Sayde Pianko','3035976149',1),(9,'Syd MB','3035976150',1),(10,'Dylan Patel','3035976151',1),(11,'Dhillon Patel','4083732107',0),(12,'Inci Yesin','9702345678',0);
/*!40000 ALTER TABLE `driver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ride`
--

DROP TABLE IF EXISTS `ride`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ride` (
  `rideID` int NOT NULL AUTO_INCREMENT,
  `driverID` int NOT NULL,
  `riderID` int NOT NULL,
  `rating` int DEFAULT NULL,
  `pickup` varchar(150) NOT NULL,
  `dropoff` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`rideID`),
  KEY `driverID` (`driverID`),
  KEY `riderID` (`riderID`),
  CONSTRAINT `ride_ibfk_1` FOREIGN KEY (`driverID`) REFERENCES `driver` (`driverID`),
  CONSTRAINT `ride_ibfk_2` FOREIGN KEY (`riderID`) REFERENCES `rider` (`riderID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ride`
--

LOCK TABLES `ride` WRITE;
/*!40000 ALTER TABLE `ride` DISABLE KEYS */;
INSERT INTO `ride` VALUES (1,1,4,5,'123 Main St','456 Elm St'),(2,5,5,5,'789 Oak St','321 Pine St'),(3,3,6,5,'456 Maple St','987 Birch St'),(4,4,7,3,'654 Cedar St ','445 Walnut St'),(5,5,6,5,'789 Spruce St','678 Laurel St'),(6,10,6,NULL,'132 N Pixley','Chapman'),(7,5,6,NULL,'132 N Pixley','Chap'),(8,4,6,3,'123 elm','432 palm'),(9,5,5,NULL,'mrow','meow'),(10,3,2,4,'1803 prairie hill','5926 tilden street'),(11,3,4,4,'blah blah','mrow mrow');
/*!40000 ALTER TABLE `ride` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rider`
--

DROP TABLE IF EXISTS `rider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rider` (
  `riderID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) NOT NULL,
  `Phone` varchar(10) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`riderID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rider`
--

LOCK TABLES `rider` WRITE;
/*!40000 ALTER TABLE `rider` DISABLE KEYS */;
INSERT INTO `rider` VALUES (1,'John Doe','1234567890','johndoe@example.com'),(2,'Jane Smith','1987654321','janesmith@example.com'),(3,'Alex Johnson','1112223333','alexjohnson@example.com'),(4,'Maria Garcia','1222333444','mariagarcia@example.com'),(5,'Chris Lee','1333444555','chrislee@example.com'),(6,'Pat Taylor','1444555666','pattaylor@example.com'),(7,'Jordan Chris','1555666777','jordanchris@example.com'),(8,'Kim Brown','1666777888','kimbrown@example.com'),(9,'Sam Robin','1777888999','samrobin@example.com'),(10,'Casey Lane','1888999111','caseylane@example.com'),(11,'Anoushka Sarma','9702863150','anoushka@gmail.com'),(12,'Luke Lamont','5032224444','lukelamont@gmail.com');
/*!40000 ALTER TABLE `rider` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-09 19:48:49
