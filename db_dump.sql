-- MySQL dump 10.13  Distrib 9.2.0, for macos15.2 (arm64)
--
-- Host: db-mysql-fra1-do-user-11632409-0.k.db.ondigitalocean.com    Database: allium
-- ------------------------------------------------------
-- Server version	8.0.35

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '34b33178-20f5-11f0-b900-3254585e6da4:1-233';

--
-- Table structure for table `Applications`
--

DROP TABLE IF EXISTS `Applications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Applications` (
  `application_id` int NOT NULL AUTO_INCREMENT,
  `applicant_id` int NOT NULL,
  `internship_id` int NOT NULL,
  `status` enum('pending','interview','rejected','offer','hired') DEFAULT 'pending',
  `resume` varchar(256) DEFAULT NULL,
  `applied_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`application_id`),
  KEY `applicant_id` (`applicant_id`),
  KEY `internship_id` (`internship_id`),
  CONSTRAINT `Applications_ibfk_1` FOREIGN KEY (`applicant_id`) REFERENCES `Students` (`student_id`) ON DELETE CASCADE,
  CONSTRAINT `Applications_ibfk_2` FOREIGN KEY (`internship_id`) REFERENCES `Internships` (`internship_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Applications`
--

LOCK TABLES `Applications` WRITE;
/*!40000 ALTER TABLE `Applications` DISABLE KEYS */;
INSERT INTO `Applications` VALUES (1,1,5,'interview','test_resume','2025-05-07 15:12:32'),(4,64,5,'pending','test123','2025-05-24 13:36:44'),(5,64,10,'pending','test123','2025-05-24 13:39:45'),(6,64,9,'pending','test123','2025-05-24 13:40:38'),(7,64,7,'pending','test123','2025-05-24 13:49:10'),(10,65,8,'hired','https://linkedin.com/in/ludwigsterner','2025-05-24 17:40:12'),(12,65,9,'pending','https://linkedin.com/in/ludwigsterner','2025-05-24 18:09:01'),(14,1,7,'pending','CV.docx','2025-05-24 18:13:53'),(16,67,10,'hired','https://linkedin.com/in/ludwigsterner','2025-05-25 15:42:50');
/*!40000 ALTER TABLE `Applications` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'REAL_AS_FLOAT,PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ONLY_FULL_GROUP_BY,ANSI,STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`william`@`%`*/ /*!50003 TRIGGER `update_internship_is_filled` AFTER UPDATE ON `Applications` FOR EACH ROW BEGIN
    IF NEW.status = 'Hired' THEN
        UPDATE Internships
        SET is_filled = 1
        WHERE internship_id = NEW.internship_id;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `Companies`
--

DROP TABLE IF EXISTS `Companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Companies` (
  `company_id` int NOT NULL AUTO_INCREMENT,
  `company_name` varchar(128) DEFAULT NULL,
  `industry` varchar(64) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  `website` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Companies`
--

LOCK TABLES `Companies` WRITE;
/*!40000 ALTER TABLE `Companies` DISABLE KEYS */;
INSERT INTO `Companies` VALUES (1,'New Name AB','Tech','New Street 456','info@new.com','www.newsite.com'),(4,'Outpost24','Technology','Onion Road 2','hello@outpost24.com','https://outpost24.com'),(5,'Outpost','Technology','Onion Road 3','hello@outpost.com','https://outpost.com'),(9,'TEst','Technology','Test Road 2222222221','hello@testcompany.com','https://testcompany.com'),(10,'WILLIEAM','Technology','WILLIEAM','hello@WILLIEAM.com','https://WILLIEAM.com'),(11,'WILLIEAM','Technology','WILLIEAM','hello@WILLIEAM.com','https://WILLIEAM.com');
/*!40000 ALTER TABLE `Companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Internships`
--

DROP TABLE IF EXISTS `Internships`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Internships` (
  `internship_id` int NOT NULL AUTO_INCREMENT,
  `company_id` int NOT NULL,
  `recruiter_id` int NOT NULL,
  `title` varchar(128) NOT NULL,
  `description` varchar(128) NOT NULL,
  `location` varchar(128) NOT NULL,
  `is_remote` tinyint(1) DEFAULT '0',
  `department` varchar(64) DEFAULT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `is_paid` tinyint(1) DEFAULT '1',
  `salary` int NOT NULL,
  `is_filled` tinyint(1) NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`internship_id`),
  KEY `company_id` (`company_id`),
  KEY `recruiter_id` (`recruiter_id`),
  CONSTRAINT `Internships_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `Companies` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Internships_ibfk_2` FOREIGN KEY (`recruiter_id`) REFERENCES `Recruiters` (`recruiter_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Internships`
--

LOCK TABLES `Internships` WRITE;
/*!40000 ALTER TABLE `Internships` DISABLE KEYS */;
INSERT INTO `Internships` VALUES (5,1,63,'Gyros provsmakare','Äta mat','Distans',0,'Ätarklubben','1998-10-13','2025-05-07',0,100,0,'2025-05-07 12:05:16','2025-05-24 13:52:12'),(7,1,63,'Test Internship Position','Work on exciting projects and learn valuable skills.','Stockholm',1,'Engineering','2025-06-01','2025-08-31',1,15000,0,'2025-05-22 14:42:04','2025-05-24 13:52:12'),(8,4,63,'Vulnerability Researcher','','Karlskrona',0,'Vulnerability Research','2025-06-16','2025-08-30',1,30000,1,'2025-05-22 19:29:39','2025-05-25 09:36:06'),(9,4,63,'Vulnerability Researcher','','Karlskrona',0,'Vulnerability Research','2025-06-16','2025-08-30',1,30000,0,'2025-05-23 14:17:00','2025-05-24 13:52:12'),(10,4,63,'Vulnerability Researcher','','Karlskrona',0,'Vulnerability Research','2025-06-16','2025-08-30',1,30000,1,'2025-05-23 14:17:00','2025-05-25 15:46:44'),(11,10,63,'test123','test123','test123',0,'test123','2025-05-30','2025-05-31',1,123,0,'2025-05-25 09:33:55','2025-05-25 09:33:55'),(12,10,63,'test internship presentation','test','Campus Gräsvik',0,'DIVA','2025-06-14','2025-08-31',1,773,0,'2025-05-25 15:48:17','2025-05-25 15:48:17');
/*!40000 ALTER TABLE `Internships` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Recruiters`
--

DROP TABLE IF EXISTS `Recruiters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Recruiters` (
  `recruiter_id` int NOT NULL,
  `company_id` int NOT NULL,
  `job_title` varchar(128) NOT NULL,
  `phone_number` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`recruiter_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `Recruiters_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `Companies` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Recruiters_ibfk_2` FOREIGN KEY (`recruiter_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Recruiters`
--

LOCK TABLES `Recruiters` WRITE;
/*!40000 ALTER TABLE `Recruiters` DISABLE KEYS */;
INSERT INTO `Recruiters` VALUES (2,1,'Temp Manager','46123456789'),(55,4,'123','123'),(59,11,'1','1'),(60,4,'jiljila','0329402394'),(63,10,'VD','000');
/*!40000 ALTER TABLE `Recruiters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Students`
--

DROP TABLE IF EXISTS `Students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Students` (
  `student_id` int NOT NULL,
  `university` varchar(128) NOT NULL,
  `degree` enum('bachelor','masters','upper-secondary','none') DEFAULT 'none',
  `graduation_year` year DEFAULT NULL,
  `resume` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  CONSTRAINT `Students_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Students`
--

LOCK TABLES `Students` WRITE;
/*!40000 ALTER TABLE `Students` DISABLE KEYS */;
INSERT INTO `Students` VALUES (1,'BTH','masters',2030,'CV.docx'),(48,'bth','bachelor',2026,'tralalero tralalala'),(56,'123','bachelor',2026,'123'),(57,'UTH','upper-secondary',2044,'159'),(58,'Allium','bachelor',2026,'Allium'),(61,'kaskad','bachelor',2028,'dksajdkl'),(62,'Livets Hårda Skola','none',2099,'-'),(64,'Test University','bachelor',2026,'test123'),(65,'Robin Hood University','bachelor',2026,'https://linkedin.com/in/ludwigsterner'),(66,'Blekinge Institute of Technology','bachelor',2026,'https://linkedin.com/in/ludwigsterner'),(67,'Blekinge Institute of Technology ','masters',2026,'https://linkedin.com/in/ludwigsterner');
/*!40000 ALTER TABLE `Students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(256) NOT NULL,
  `first_name` varchar(64) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `password_hash` varchar(256) NOT NULL,
  `user_type` enum('student','recruiter') NOT NULL DEFAULT 'student',
  `profile_picture` varchar(256) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'detta@är.test','Donald','Duck','scrypt:32768:8:1$icPKrs6vWrJ9xKvK$daa7c7cba9ee4a950f8d6ad9cfb63659f72144c0469dcf3e2b201481c19608cb81f66aff43753f63495074b9748b5f5de6f10bae817bd438d73d2d3d9e07ca4c','student','https://example.com/anka.jpg','2025-04-24 16:23:20','2025-05-19 11:29:13'),(2,'recruiter@recruiter.com','William','Silvstrand Olsson','scrypt:32768:8:1$yHvjyCCu4SDrGrBu$338ee449677076a59ecb5bc95948f634f0898468dedf9c1e32d849d8104cef8d1651040267718e1a0792b6b6864c630be79706b5a2e97a656c9b7d0e624d2c73','recruiter',NULL,'2025-04-24 18:18:23','2025-04-24 18:18:23'),(5,'t@t.t','t','t','scrypt:32768:8:1$Xw5yvKEASwrNgD2t$7f795cc762753784be1aa3b84a43bb6f92c4d7ea70e7e32b55536f2467813a184107299a7d5da729a7d3122a9e2389d849c318f715d4999f5985e101b19d7e66','student',NULL,'2025-05-07 11:38:45','2025-05-07 11:38:45'),(8,'test_email@email.com','test_fname','test_lname','scrypt:32768:8:1$mApFPjiSieOzndwN$8d66cd7d7f8e0d89825485bf6b17d07e8c6143527fd7cb04132ab9b345fb4e7a8684d06807a74797eb049b79f6a911a1fd556d3cc0905b40758efe28aa124f99','student',NULL,'2025-05-19 11:09:13','2025-05-19 11:09:13'),(11,'test_email@email.coma','test_fname','test_lname','scrypt:32768:8:1$NNsEgYvSWaWaJbuF$2c6241e0df5be890b8ff53ebd4c4159ba25d97999b4ae86fa90aea2f6ea3c63e2779917045f0a291dbcc220a1abe337be04d1837917851cf80266cf7c83b104f','student',NULL,'2025-05-19 11:09:40','2025-05-19 11:09:40'),(13,'testemail@email.com','test_fname','test_lname','scrypt:32768:8:1$UlC4nEWIzvKywrSm$58d1667b0214cb770d3c72e683e8da7bcfe0e188bc8b08d7d06cfa84f5f93277605ffa97597f0cebe2f0f413119b856bc9c5b5170632f25cdc8fb8528e57996d','student',NULL,'2025-05-19 11:24:39','2025-05-19 11:24:39'),(15,'test@email.com','test_fname','test_lname','scrypt:32768:8:1$nbAJBxvhpxMIV6fx$03cda1c08690339643a949a72c8b8a8f4bdb8ab0bd03228e9947b6e32dda5c9be17f13890366278094d03165869f5ac38a1e2698f38ebf9adde332a14dcc1df0','student',NULL,'2025-05-19 11:26:27','2025-05-19 11:26:27'),(16,'tesat@email.com','test_fname','test_lname','scrypt:32768:8:1$fuzHUTwBDofNNrl1$91054e66e843e64f30c59e7dbd759180acf88841ea470f378e71ec0985fde652e533a9c074a642185965215d47e59e3fceee105cb2a7531572a4ef669395c34d','student',NULL,'2025-05-19 11:28:15','2025-05-19 11:28:15'),(18,'ludwig@email.com','test_fname','test_lname','scrypt:32768:8:1$uYBNJjlwTgKb2AhK$06a0034031bd64737b670698499dd244b068e79b0ee5c1a72506969f1d5acf329f6edecdf37d90adeaf8bcb36ee7ad69b4af4d6d2d22b8de5025a4fa7ad244bc','student',NULL,'2025-05-19 11:28:26','2025-05-19 11:28:26'),(20,'lodd@email.com','test_fname','test_lname','scrypt:32768:8:1$4npZo9IJpAEpo9DF$41f9033b5d937a1232c094f2a394a7a8c84b8cadb69811113054bcc2ca8c0c68f3909688bcfd6382067f6b80665ae0d629d393378ced825c5ddceb8986a72749','student',NULL,'2025-05-19 11:31:00','2025-05-19 11:31:00'),(21,'lodd@email.coma','test_fname','test_lname','scrypt:32768:8:1$o8JhVVxeViFaFedJ$66f471ecbae67a10fbc93f6f2c8fc1226f5c52e788780b215158800adce97155b5e0fa819c891395b964e3a0cd934d41a20807b3f485d44c11faa0e95f2d4461','student',NULL,'2025-05-19 11:31:22','2025-05-19 11:31:22'),(22,'lodda@email.coma','test_fname','test_lname','scrypt:32768:8:1$hgjot4XtN6VLZHw1$3121fee1124ec41901998c48f58f607530a4c43b7bd7c80d0c525a0a3f043193cad137d7ca956cf4780d1d5ee563ae3b29883fc508c4692b0b1d21e9b1e9c9de','student',NULL,'2025-05-19 11:59:32','2025-05-19 11:59:32'),(23,'loddaaa@email.coma','test_fname','test_lname','scrypt:32768:8:1$gfnD0cDVZ8U2ktwO$c86a1b3721735a9f8a1c4cc2b3d071db8d26f3a214a51b7c732e6a35fddce403bc8fc16e50ff0e0a562796fbbab531ae24dd13c1be4bf0d3f476aaadbe62ed46','student',NULL,'2025-05-19 12:00:47','2025-05-19 12:00:47'),(24,'lodda@email.comaa','test_fname','test_lname','scrypt:32768:8:1$J5NHKzNjVuXZRCEk$3a5042d80f84961c2b2c2d2ef10cb2cfa257ce99add28c2c4d0d54afb29366617f55ffa5099c140f2561e7437fab7bea35772eb212833eea0294df33f39b0fa7','student',NULL,'2025-05-19 12:02:38','2025-05-19 12:02:38'),(25,'lodda@email.comaaa','test_fname','test_lname','scrypt:32768:8:1$JK9HTQIFbF4zQ644$3748daf6b4a43300b92972d7a74c87f336f2fd8d21e5667074c154ab5ee699186836229beb3ad8ef21ee97c78f26de7bd212f4eb52aba1a370036d094458fd38','student',NULL,'2025-05-19 12:03:16','2025-05-19 12:03:16'),(26,'lodda@email.comaaaa','test_fname','test_lname','scrypt:32768:8:1$xDA5JsyeR0lYBpkW$7c38249559e2e1db51a4fa79d2a3802489e3f4de67cb127d4927561121e2ccb596a1e0ccda063a605f2cc908669e838dd298ce9e87e2011c62787af1dd54651e','recruiter',NULL,'2025-05-19 12:03:30','2025-05-19 12:03:30'),(27,'lodda@email.comaaaaa','test_fname','test_lname','scrypt:32768:8:1$8badClN2Z6scycli$2d53253c6eb57f3156d447316a73a4f2808bb2f8b46fd418890c167284a9840a348a4caa54970ecb3c9fe80eef5c235173af02b5ddc734a665f04d745e74e5e0','recruiter',NULL,'2025-05-19 12:03:45','2025-05-19 12:03:45'),(28,'ginger@hogwarts.uk','Ronald','Wesley','scrypt:32768:8:1$eqyCZiSMB8D5hYrM$b6769237d34a66ea99cbff4b80ccc15babba128a173ef3ecd2cf38d43701d1df892936e27e826688d0c9b4858335f662f461a8d3c4d23aa0e752a2db14ee2100','student',NULL,'2025-05-19 12:17:37','2025-05-19 12:17:37'),(29,'te@te.com','te','te','scrypt:32768:8:1$mzGpN3JdTlyBL8kx$36ab4f840ba8d6b1082e2d457511d86c4fd15be54a7fe922c8ab81001bb871b11930bb1098dc6ee05ae93826d3176ecb9662f806403c0a2f9df5f13ffd9bd9d7','student',NULL,'2025-05-19 12:18:07','2025-05-19 12:18:07'),(31,'tea@te.com','tea','tea','scrypt:32768:8:1$pRTXpegKVVO2v4Du$fb729dda3ea1e43f0dca63bf7789c0bd64b3fc1457392dd815a79c6390b8431d30124600af71be7231d86e556fae2fd55402a67b2f15bfe752fb341fcbe1d3da','student',NULL,'2025-05-19 12:20:59','2025-05-19 12:20:59'),(32,'tess@skolmail.com','Tess','Molin Snippert','scrypt:32768:8:1$qL1cHOeemIVrhRuH$fdd8f76fbf9d634c3cb137fc8359f2f496e8cabe1c181525503982876771462e96459f6c6fe2784e93489863327475999834048041f3250ef2e344fbcef776a8','student',NULL,'2025-05-19 19:43:28','2025-05-19 19:43:28'),(33,'tester@tester.test','test','test','test','student',NULL,'2025-05-22 08:54:08','2025-05-22 08:54:08'),(35,'b@b.b','b','b','scrypt:32768:8:1$PuyoVM5EcP2zfHD5$0a6b9de4a41e3122d91d6e030d7b80ec14be9abb35ea2a1c04e53959918ce52dfc9241b4920aaf961edca8db6f63ba5dfec5abaf6532150ad10f1eef2f44aa5c','student',NULL,'2025-05-22 09:09:55','2025-05-22 09:09:55'),(36,'ludwig@allium.com','Ludwig','Sterner','scrypt:32768:8:1$NQsTZy7iHrSsEUxG$043c5c5f0b512485a8c0ab97262b7028d4865037a0e1e2821c76e6fc3c6ea51037858b8e71753d8bb2c3b930233753a55582aa40c78840344e3d6b95ea6c87ae','student',NULL,'2025-05-22 09:32:06','2025-05-22 09:32:06'),(37,'kalle@anka.se','kalle','anka','scrypt:32768:8:1$T7nLPC8Km5CL9eZK$74f8ceb231d757f2ffcb7c061eedbb2a3b9ced9b5ad034ba4a8678a84e1ece15df7e3a1c2cb44d8a09eee9f5080dc43ac32ccbc3f2f5d6361c95b379c2027f9f','recruiter',NULL,'2025-05-22 09:36:48','2025-05-22 09:36:48'),(38,'mario@nintendo.jp','Super','Mario','scrypt:32768:8:1$RnFdm6z2mVSReI63$d820f8373fd52fd6ff57206d28bc0d8e4fcd79f15cf8704cfea619c022c061f0618575b54750140f82251de5fb3bd5ee7d5adc4db82f768744abf40e9edbb330','recruiter',NULL,'2025-05-22 09:39:43','2025-05-22 09:39:43'),(40,'c@c.c','c','c','scrypt:32768:8:1$NwEtmnwVuX91VUMb$0d01da3ef8527555a851fea656977bae111ebe9af145b01db5f752ff85cc69ebbf61e26513666ba201051232a97b588ad03d4472c56ce6f35bd797cebddbbf58','student',NULL,'2025-05-22 09:41:50','2025-05-22 09:41:50'),(41,'d@d.d','d','d','scrypt:32768:8:1$qgw9P9dUYFnFeSaW$a45d2dba416a1931740118980fac37c382db23435217393bdf7473bb4ea1d52c6e990dd6ae37b55e518d02e96a2a3f3fe07b349fcae661f3afb34e17f7d1cfac','recruiter',NULL,'2025-05-22 09:42:09','2025-05-22 09:42:09'),(42,'e@e.e','e','e','scrypt:32768:8:1$zzDvU9QQqXyIx7va$9b60f15c48f6b41ca4d99046cc4993fc648311a449e8672b8e25d395b8e3139e215c29e7c7cdd9ccee7e3dc980140e87e1ccf06768d2ce3c30adcc1a6a80f6e1','student',NULL,'2025-05-22 09:43:09','2025-05-22 09:43:09'),(43,'h@h.h','h','h','scrypt:32768:8:1$ZbsIo7zhhN6yJ1Y5$0e031aeb4a0e8e3a813216ce30b71f6a6ff48d85133bbff2f2172c391e2282bd1083edb5fbf9b50234b932a981185b2df5618d48b69000a5fcf74d9c2c6dbf99','student',NULL,'2025-05-22 10:09:05','2025-05-22 10:09:05'),(44,'p@p.p','p','p','scrypt:32768:8:1$kPiagUkgyFrwLvb7$eacc78f8d792b357bfd242c3016bb6fdd29472e0a62287f5360d7bc04ae7692322677f3122bcfba3cff35478945674d7fb8e8c90f3c849b3eaa4b62211106086','recruiter',NULL,'2025-05-22 10:11:00','2025-05-22 10:11:00'),(45,'k@k.k','k','k','scrypt:32768:8:1$9MuxCxdH4PM8s7vG$af5d3fb3d0db980de8fa1544a8da58ed2151e11d1d29e82b1acdf59c6b59851d43138b1cf1b7dc12459a374503c1b8bae7d8f6ea3e8ce57270fc74e9191c6166','student',NULL,'2025-05-22 10:11:19','2025-05-22 10:11:19'),(46,'lod@lod.lod','lod','lod','scrypt:32768:8:1$VV1VGabucjoeW0vc$459e811e294243dcf11f591fc17956f6e4a7d4892b019f5f5c3b2ce14c6543a759d2f9fb01b365da900f07638dc47c0e49ff89158196a37f6208fc3b4f339796','recruiter',NULL,'2025-05-22 10:14:39','2025-05-22 10:14:39'),(47,'r@r.r','r','r','scrypt:32768:8:1$Bktn3EsCIqdXFknE$a1b54965932b7e833d3acf3d4c5309607c42e7e8b563739a43fd0b8a9210cfd1500146f418dc9389c2cc19406f10e396430071a9d72babf44c6ef1f2600413b3','recruiter',NULL,'2025-05-22 10:17:05','2025-05-22 10:17:05'),(48,'will@iam.com','will','iam','scrypt:32768:8:1$QT4DpvbdnepRFrBY$a7d7449144f42d5915d9dbb0d7315ee2be2556b5fb5747d7604aba69c8046ce2babe6ac7eaca1d3f5297c61c2b94105d3287b860f970e2d039007ea4623fc1d8','student',NULL,'2025-05-22 10:19:50','2025-05-22 10:19:50'),(49,'rec@r.r','rec','rec','scrypt:32768:8:1$UPmfNNINjY1VCTZm$a7cee3de84124a51a7b7757dff713d0fc8bdd016cc151bc39664c4e4510159aba9e1116738a7d06339d5f0afbac8bc3c7e85a0d567b1ec527da30c4a78fefb63','recruiter',NULL,'2025-05-22 10:53:50','2025-05-22 10:53:50'),(50,'rec@out.se','se','se','scrypt:32768:8:1$oRC5T2j3tDXZaa8P$638cd861d6c62c20a456dc7361d26f17aca55b07f932d4b6dae89408f48fe503a61e7e9ec74222880ac861963d0a5d5bed598df31d2a6db1a0753953f5775205','recruiter',NULL,'2025-05-22 10:59:44','2025-05-22 10:59:44'),(51,'rec@outs.se','se','se','scrypt:32768:8:1$I774w47Zark6ryVg$8e581296fcd72fb15d1c21762246017b5e1283c1bdd9e6eab8c4692f0f5d170a00fd1c821136bd792d061453475b3a556b80c4b0fbc4719c968f67504bc551ca','recruiter',NULL,'2025-05-22 11:01:02','2025-05-22 11:01:02'),(52,'rec@ousts.se','se','se','scrypt:32768:8:1$hlAARVoNUM8UcTbG$b3d29a929532364b02547c7eff1539d9dec1a102b5af176f7b56835bc287d5b2bbda5e62fdf878602dfdd68db7b8a565a356b9f4587edb159aa762841251ccfa','recruiter',NULL,'2025-05-22 11:02:11','2025-05-22 11:02:11'),(53,'rec@oustas.se','se','se','scrypt:32768:8:1$g990ZG243Q0Bwy0q$b71fe07b98068d0752fca2381f4022354e2d3459ef124397a2f27494af8c4124e911d64bc0c85e0a629bc96fc5a230bc3936d326646c905ec218cfb2a8757cc9','recruiter',NULL,'2025-05-22 11:08:53','2025-05-22 11:08:53'),(54,'rec@oustaas.se','se','se','scrypt:32768:8:1$FkMdzRswAF0TJ2lb$9ba458d3fdf8607212c1416af38e63a839127e9848426485459fb3d35d8ffc8b102fa470b6d093428553808a2533227e6923df87f5e636929c03baf2344c5052','recruiter',NULL,'2025-05-22 11:10:56','2025-05-22 11:10:56'),(55,'rec@oustaaas.se','se','se','scrypt:32768:8:1$cl1EKB7wStcMAVUB$6d0360b222756e7e5432efa319fdeb5fe8b098d555b547fc910259a407922a55928b46293f2680c725bebbda01eafc80be932bd7abcaba059e33f7da9ef90b04','recruiter',NULL,'2025-05-22 11:11:49','2025-05-22 11:11:49'),(56,'oidsa@jdioas.com','dioas','jdoisa','scrypt:32768:8:1$B1UabyAT3kjQfFiT$360132c7c56b34e15fab0cf3d41c7809167d69eb385d446a3be24093caada61e103fecd11cd357c01396014615552d45d3a31ce7ddb745a05dfa784c0df9a5e8','student',NULL,'2025-05-22 11:19:54','2025-05-22 11:19:54'),(57,'ludwig@a.com','Ludwig','Sterner','scrypt:32768:8:1$bXWd261aprF92SR8$3052d7180be8e4a61df37d649cffc9402384839170786dde078d8c2a87cb8e7f7cab17f5de2f313eeda88085eb04f42866573829464e109dac3e923f93ca60e8','student',NULL,'2025-05-22 13:04:54','2025-05-22 13:04:54'),(58,'allium@allium.com','Allium','Allium','scrypt:32768:8:1$wyMNF9nlMig8bkGY$20d591870ad1eabbd7d3a3bdb05e96a5e4c0f3096f9d26e1bb744c01a09dbd9549a5a8462bf7cebda364467fa0975a19a49e35f2333a320bc93e66c3f1f35156','student',NULL,'2025-05-23 07:33:59','2025-05-23 07:33:59'),(59,'a@a.se','a','a','scrypt:32768:8:1$8mFa2Pc0gbF3lF9w$e6a8960d1fc5ca9ce57a40f657c94048f9f8fd58855105b952254a60ab27be0c9087f2e8c58557c2d0c62772245f309178cb852e8887b2d616bd63a9bc616a43','recruiter',NULL,'2025-05-23 07:41:53','2025-05-23 07:41:53'),(60,'lu@d.com','Ludwig','Sterner','scrypt:32768:8:1$zviZH2Wl3Hmrg4k3$ed2b581440f9d5d50d24fc1fe2bab499adb436acadf3ce882609f15d3fd018dbd20a21150388ffccb63cc6d61f46240aa7896cc7aa0db598f5f9469fad042179','recruiter',NULL,'2025-05-23 12:30:45','2025-05-23 12:30:45'),(61,'kdoas@dkasd.com','kdlask','djkasjild','scrypt:32768:8:1$psTdi87BDffDwCRd$6fa2dbbf0292e915df740b409b7a67cc138827076660a682c5ce9026d06bdfc6d4263200f3a966ee9adcdb0fc29be6318be6b307b448c00fbbde7b7eda8c4a86','student',NULL,'2025-05-23 12:31:25','2025-05-23 12:31:25'),(62,'g@g.g','Hulken','Giga','scrypt:32768:8:1$oIqaY4xx5yXQQWUv$0844f3008da2a354267b644fc2fa69af9945778797907b35b7b6d22c916bcb96e349ab04b97bbdeef26548164826154465a582a9a74fe51e3dd6044624d73b85','student',NULL,'2025-05-24 12:18:11','2025-05-24 12:18:11'),(63,'w@w.w','Rekryteraren','Sir','scrypt:32768:8:1$4ucN0hZp9FbFPlFL$33143ae99a70df377e16cb50d15d7b5f3314a86a34cd8ce07f69d507ba6715309c5acb75c3a9c764353e536a549a84c292439ed419c9b63b8df1725156241f60','recruiter',NULL,'2025-05-24 13:06:44','2025-05-24 13:06:44'),(64,'testymctestface@test.com','testy','mctestface','scrypt:32768:8:1$wb8vY2c7ZMdLiRNw$ab3f0a69199bfd949c77c0830f1f8299b5c1e1e6edd17c93e21280606aa534503374b9931a6d7fb1f6bd8d1d90754f74006e5b6391da7ec59d1d1abd0716aabf','student',NULL,'2025-05-24 13:34:44','2025-05-24 13:34:44'),(65,'sir_vas@hood.com','Sir','Väs','scrypt:32768:8:1$AmBPnx23CNWPTRW8$af1db11c03f8657279074d8daeab88b317f885c6365df25973881b1e6a9f6404a8a5aa8292ab219415b289326afb6bd5b10f97f00e835417cf2dc6878b2e2f54','student',NULL,'2025-05-24 16:45:22','2025-05-24 16:45:22'),(66,'presentation@allium.com','Ludwig','Sterner','scrypt:32768:8:1$PEXSP1iTXqZpqJR7$c6a4e39033c1917cd8a0b3f38c5439742f85c22c0edc1ea64d337414eecfda3ed8e7bb43b9f6d42b6ccb9d308315e9dbf65dc485c4b1a916f69d56894357a71e','student',NULL,'2025-05-25 15:35:07','2025-05-25 15:35:07'),(67,'presentation@dv1663.com','Ludwig','Sterner','scrypt:32768:8:1$l8rly9wgL0XWHyDj$898a544656e65e59f016120d1eb9821b66d2285bbba5afda921bdb1685ec40ee71d2989b2044e24fb134bbaee292e7ce6a47d8c10f5aa578d022404e4077ab19','student',NULL,'2025-05-25 15:41:23','2025-05-25 15:41:23'),(68,'jdisa@doisadji.com','asdjioasjdi','djasidiosa','scrypt:32768:8:1$DLf88IYkaPQaZUvr$74e19cfe5f306f447a24d2808cb8510b60b06d716d256205ece20a4acb22a3faaf291630eec5381dd698213e47e7ec16d8e9873f6c6a5f566180ed431e5e7181','recruiter',NULL,'2025-05-25 15:45:02','2025-05-25 15:45:02');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-25 18:28:21
