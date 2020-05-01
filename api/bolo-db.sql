-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: bolo
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add credential',1,'add_credential'),(2,'Can change credential',1,'change_credential'),(3,'Can delete credential',1,'delete_credential'),(4,'Can add log entry',2,'add_logentry'),(5,'Can change log entry',2,'change_logentry'),(6,'Can delete log entry',2,'delete_logentry'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add user',5,'add_user'),(14,'Can change user',5,'change_user'),(15,'Can delete user',5,'delete_user'),(16,'Can add content type',6,'add_contenttype'),(17,'Can change content type',6,'change_contenttype'),(18,'Can delete content type',6,'delete_contenttype'),(19,'Can add session',7,'add_session'),(20,'Can change session',7,'change_session'),(21,'Can delete session',7,'delete_session'),(22,'Can add shipment retailer',8,'add_shipmentretailer'),(23,'Can change shipment retailer',8,'change_shipmentretailer'),(24,'Can delete shipment retailer',8,'delete_shipmentretailer'),(25,'Can add shipment item',9,'add_shipmentitem'),(26,'Can change shipment item',9,'change_shipmentitem'),(27,'Can delete shipment item',9,'delete_shipmentitem'),(28,'Can view credential',1,'view_credential'),(29,'Can view shipment item',9,'view_shipmentitem'),(30,'Can view shipment retailer',8,'view_shipmentretailer'),(31,'Can view log entry',2,'view_logentry'),(32,'Can view permission',3,'view_permission'),(33,'Can view group',4,'view_group'),(34,'Can view user',5,'view_user'),(35,'Can view content type',6,'view_contenttype'),(36,'Can view session',7,'view_session'),(37,'Can add crontab',10,'add_crontabschedule'),(38,'Can change crontab',10,'change_crontabschedule'),(39,'Can delete crontab',10,'delete_crontabschedule'),(40,'Can view crontab',10,'view_crontabschedule'),(41,'Can add interval',11,'add_intervalschedule'),(42,'Can change interval',11,'change_intervalschedule'),(43,'Can delete interval',11,'delete_intervalschedule'),(44,'Can view interval',11,'view_intervalschedule'),(45,'Can add periodic task',12,'add_periodictask'),(46,'Can change periodic task',12,'change_periodictask'),(47,'Can delete periodic task',12,'delete_periodictask'),(48,'Can view periodic task',12,'view_periodictask'),(49,'Can add periodic tasks',13,'add_periodictasks'),(50,'Can change periodic tasks',13,'change_periodictasks'),(51,'Can delete periodic tasks',13,'delete_periodictasks'),(52,'Can view periodic tasks',13,'view_periodictasks'),(53,'Can add solar event',14,'add_solarschedule'),(54,'Can change solar event',14,'change_solarschedule'),(55,'Can delete solar event',14,'delete_solarschedule'),(56,'Can view solar event',14,'view_solarschedule'),(57,'Can add clocked',15,'add_clockedschedule'),(58,'Can change clocked',15,'change_clockedschedule'),(59,'Can delete clocked',15,'delete_clockedschedule'),(60,'Can view clocked',15,'view_clockedschedule');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$jMJfblw5dbXL$ppdBILWrC+IjJrCxx8hdDi09DGS3RiG8JQ1LWLVH3bg=','2020-04-27 01:57:32.479745',1,'divya','','','',1,1,'2020-04-27 01:57:11.329926');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crud_credential`
--

DROP TABLE IF EXISTS `crud_credential`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `crud_credential` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `secret_key` varchar(120) NOT NULL,
  `client_key` varchar(120) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crud_credential`
--

LOCK TABLES `crud_credential` WRITE;
/*!40000 ALTER TABLE `crud_credential` DISABLE KEYS */;
INSERT INTO `crud_credential` VALUES (2,'NfainCcmbafiCUiutV7IKmjn8NbOCbw6Xc16a-_MDVyC0jhfbekNIpQ3z3sNUHhNJJEhK3ORSbh8WWbf9zSGpQ','69bd83f1-1172-4b02-821a-b5a2af5a32da'),(3,'NfainCcmbafiCUiutV7IKmjn8NbOCbw6Xc16a-_MDVyC0jhfbekNIpQ3z3sNUHhNJJEhK3ORSbh8WWbf9zSGpQ','69bd83f1-1172-4b02-8221a-b5a2af5a32da'),(4,'NfainCcmbafiCUiutV7IKmjn8NbOCbw6Xc16a-_MDVyC0jhfbekNIpQ3z3sNUHhNJJEhK3ORSbh8WWbf9zSGpQ','69bd83f1-1172-4b02-821a-b5a2af5a32da23'),(5,'NfainCcmbafiCUiutV7IKmjn8NbOCbw6Xc16a-_MDVyC0jhfbekNIpQ3z3sNUHhNJJEhK3ORSbh8WWbf9zSGpQ','69bd83f1-1172-4b02-821a-b5a2af5a32da93');
/*!40000 ALTER TABLE `crud_credential` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-04-27 01:57:53.376313','1','1 * * * * (m/h/d/dM/MY) UTC',1,'[{\"added\": {}}]',10,1),(2,'2020-04-27 01:59:15.923349','1','task: 1 * * * * (m/h/d/dM/MY) UTC',1,'[{\"added\": {}}]',12,1),(3,'2020-04-27 02:00:18.239446','1','2020-04-27 07:31:00+05:30 True',1,'[{\"added\": {}}]',15,1),(4,'2020-04-27 02:00:31.214682','1','task: 2020-04-27 02:01:00+00:00 True',2,'[{\"changed\": {\"fields\": [\"crontab\", \"clocked\"]}}]',12,1),(5,'2020-04-27 02:02:05.409389','1','task: 1 * * * * (m/h/d/dM/MY) UTC',2,'[{\"changed\": {\"fields\": [\"regtask\", \"crontab\", \"clocked\", \"one_off\"]}}]',12,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_clockedschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_clockedschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_celery_beat_clockedschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clocked_time` datetime(6) NOT NULL,
  `enabled` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_clockedschedule`
--

LOCK TABLES `django_celery_beat_clockedschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_clockedschedule` DISABLE KEYS */;
INSERT INTO `django_celery_beat_clockedschedule` VALUES (1,'2020-04-27 02:01:00.000000',1);
/*!40000 ALTER TABLE `django_celery_beat_clockedschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_crontabschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_crontabschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_celery_beat_crontabschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `minute` varchar(240) NOT NULL,
  `hour` varchar(96) NOT NULL,
  `day_of_week` varchar(64) NOT NULL,
  `day_of_month` varchar(124) NOT NULL,
  `month_of_year` varchar(64) NOT NULL,
  `timezone` varchar(63) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_crontabschedule`
--

LOCK TABLES `django_celery_beat_crontabschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_crontabschedule` DISABLE KEYS */;
INSERT INTO `django_celery_beat_crontabschedule` VALUES (1,'1','*','*','*','*','UTC'),(2,'0','4','*','*','*','UTC'),(3,'*/1','*','*','*','*','UTC'),(4,'*/10','*','*','*','*','UTC'),(5,'*/15','*','*','*','*','UTC'),(6,'0','*/5','*','*','*','UTC');
/*!40000 ALTER TABLE `django_celery_beat_crontabschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_intervalschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_intervalschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_celery_beat_intervalschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `every` int(11) NOT NULL,
  `period` varchar(24) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_intervalschedule`
--

LOCK TABLES `django_celery_beat_intervalschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_intervalschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_intervalschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_periodictask`
--

DROP TABLE IF EXISTS `django_celery_beat_periodictask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_celery_beat_periodictask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `task` varchar(200) NOT NULL,
  `args` longtext NOT NULL,
  `kwargs` longtext NOT NULL,
  `queue` varchar(200) DEFAULT NULL,
  `exchange` varchar(200) DEFAULT NULL,
  `routing_key` varchar(200) DEFAULT NULL,
  `expires` datetime(6) DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime(6) DEFAULT NULL,
  `total_run_count` int(10) unsigned NOT NULL,
  `date_changed` datetime(6) NOT NULL,
  `description` longtext NOT NULL,
  `crontab_id` int(11) DEFAULT NULL,
  `interval_id` int(11) DEFAULT NULL,
  `solar_id` int(11) DEFAULT NULL,
  `one_off` tinyint(1) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `priority` int(10) unsigned DEFAULT NULL,
  `headers` longtext NOT NULL,
  `clocked_id` int(11) DEFAULT NULL,
  `expire_seconds` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` (`crontab_id`),
  KEY `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` (`interval_id`),
  KEY `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` (`solar_id`),
  KEY `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` (`clocked_id`),
  CONSTRAINT `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` FOREIGN KEY (`clocked_id`) REFERENCES `django_celery_beat_clockedschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` FOREIGN KEY (`crontab_id`) REFERENCES `django_celery_beat_crontabschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` FOREIGN KEY (`interval_id`) REFERENCES `django_celery_beat_intervalschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` FOREIGN KEY (`solar_id`) REFERENCES `django_celery_beat_solarschedule` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_periodictask`
--

LOCK TABLES `django_celery_beat_periodictask` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_periodictask` DISABLE KEYS */;
INSERT INTO `django_celery_beat_periodictask` VALUES (1,'celery.backend_cleanup','celery.backend_cleanup','[]','{}',NULL,NULL,NULL,NULL,1,NULL,0,'2020-04-29 08:00:26.139359','',2,NULL,NULL,0,NULL,NULL,'{}',NULL,43200),(3,'load_shipment','load_shipment','[]','{}',NULL,NULL,NULL,NULL,1,NULL,0,'2020-04-29 08:00:26.166329','',6,NULL,NULL,0,NULL,NULL,'{}',NULL,NULL);
/*!40000 ALTER TABLE `django_celery_beat_periodictask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_periodictasks`
--

DROP TABLE IF EXISTS `django_celery_beat_periodictasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_celery_beat_periodictasks` (
  `ident` smallint(6) NOT NULL,
  `last_update` datetime(6) NOT NULL,
  PRIMARY KEY (`ident`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_periodictasks`
--

LOCK TABLES `django_celery_beat_periodictasks` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_periodictasks` DISABLE KEYS */;
INSERT INTO `django_celery_beat_periodictasks` VALUES (1,'2020-04-29 08:00:26.159029');
/*!40000 ALTER TABLE `django_celery_beat_periodictasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_solarschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_solarschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_celery_beat_solarschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event` varchar(24) NOT NULL,
  `latitude` decimal(9,6) NOT NULL,
  `longitude` decimal(9,6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_celery_beat_solar_event_latitude_longitude_ba64999a_uniq` (`event`,`latitude`,`longitude`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_solarschedule`
--

LOCK TABLES `django_celery_beat_solarschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_solarschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_solarschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (2,'admin','logentry'),(4,'auth','group'),(3,'auth','permission'),(5,'auth','user'),(6,'contenttypes','contenttype'),(1,'crud','credential'),(15,'django_celery_beat','clockedschedule'),(10,'django_celery_beat','crontabschedule'),(11,'django_celery_beat','intervalschedule'),(12,'django_celery_beat','periodictask'),(13,'django_celery_beat','periodictasks'),(14,'django_celery_beat','solarschedule'),(7,'sessions','session'),(9,'shipment','shipmentitem'),(8,'shipment','shipmentretailer');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-04-26 16:07:19.281993'),(2,'auth','0001_initial','2020-04-26 16:07:20.038614'),(3,'admin','0001_initial','2020-04-26 16:07:20.223089'),(4,'admin','0002_logentry_remove_auto_add','2020-04-26 16:07:20.252710'),(5,'contenttypes','0002_remove_content_type_name','2020-04-26 16:07:20.343739'),(6,'auth','0002_alter_permission_name_max_length','2020-04-26 16:07:20.359142'),(7,'auth','0003_alter_user_email_max_length','2020-04-26 16:07:20.386834'),(8,'auth','0004_alter_user_username_opts','2020-04-26 16:07:20.405491'),(9,'auth','0005_alter_user_last_login_null','2020-04-26 16:07:20.456114'),(10,'auth','0006_require_contenttypes_0002','2020-04-26 16:07:20.459870'),(11,'auth','0007_alter_validators_add_error_messages','2020-04-26 16:07:20.470487'),(12,'auth','0008_alter_user_username_max_length','2020-04-26 16:07:20.543007'),(13,'auth','0009_alter_user_last_name_max_length','2020-04-26 16:07:20.579635'),(14,'crud','0001_initial','2020-04-26 16:07:20.616682'),(15,'sessions','0001_initial','2020-04-26 16:07:20.670386'),(16,'shipment','0001_initial','2020-04-26 18:11:28.479544'),(17,'shipment','0002_auto_20200426_1812','2020-04-26 18:12:23.322774'),(18,'shipment','0003_shipmentitem_fulfilment_method','2020-04-26 22:03:55.151176'),(19,'shipment','0004_auto_20200426_2203','2020-04-26 22:03:55.201641'),(20,'shipment','0005_auto_20200426_2211','2020-04-26 22:11:08.972651'),(21,'shipment','0006_auto_20200426_2223','2020-04-26 22:23:27.387559'),(22,'admin','0003_logentry_add_action_flag_choices','2020-04-27 01:48:31.355572'),(23,'auth','0010_alter_group_name_max_length','2020-04-27 01:48:31.369267'),(24,'auth','0011_update_proxy_permissions','2020-04-27 01:48:31.380249'),(25,'django_celery_beat','0001_initial','2020-04-27 01:48:31.515220'),(26,'django_celery_beat','0002_auto_20161118_0346','2020-04-27 01:48:31.740229'),(27,'django_celery_beat','0003_auto_20161209_0049','2020-04-27 01:48:31.853796'),(28,'django_celery_beat','0004_auto_20170221_0000','2020-04-27 01:48:31.870454'),(29,'django_celery_beat','0005_add_solarschedule_events_choices','2020-04-27 01:48:31.886536'),(30,'django_celery_beat','0006_auto_20180322_0932','2020-04-27 01:48:31.975183'),(31,'django_celery_beat','0007_auto_20180521_0826','2020-04-27 01:48:32.126504'),(32,'django_celery_beat','0008_auto_20180914_1922','2020-04-27 01:48:32.170357'),(33,'django_celery_beat','0006_auto_20180210_1226','2020-04-27 01:48:32.183313'),(34,'django_celery_beat','0006_periodictask_priority','2020-04-27 01:48:32.232745'),(35,'django_celery_beat','0009_periodictask_headers','2020-04-27 01:48:32.296154'),(36,'django_celery_beat','0010_auto_20190429_0326','2020-04-27 01:48:32.732400'),(37,'django_celery_beat','0011_auto_20190508_0153','2020-04-27 01:48:32.816601'),(38,'django_celery_beat','0012_periodictask_expire_seconds','2020-04-27 01:48:32.976955');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3nqa9hascwweyurpw0lgibme0vfyrg46','MTkxOWJmOGQ5NDI3OWFhYWQwNzIxNmJlNTMyYjg3YTFhOGU2YTNlZTp7InRva2VuIjoiaXV3ZWYifQ==','2020-05-11 21:02:59.944538'),('ln19t2ey6bojxguc6biebb1nzbv671th','OTcxMTY5NzdhZWVjMmIwNGM4YjRjZmYzZTFlM2MzM2E4NmJjZDYyYzp7ImNsaWVudF9rZXkiOiI2OWJkODNmMS0xMTcyLTRiMDItODIxYS1iNWEyYWY1YTMyZGEiLCJzZWNyZXRfa2V5IjoiTmZhaW5DY21iYWZpQ1VpdXRWN0lLbWpuOE5iT0NidzZYYzE2YS1fTURWeUMwamhmYmVrTklwUTN6M3NOVUhoTkpKRWhLM09SU2JoOFdXYmY5elNHcFEiLCJ0b2tlbiI6IkJlYXJlciBleUpyYVdRaU9pSnljMkV5SWl3aVlXeG5Jam9pVWxNeU5UWWlmUS5leUp6ZFdJaU9pSTJPV0prT0RObU1TMHhNVGN5TFRSaU1ESXRPREl4WVMxaU5XRXlZV1kxWVRNeVpHRWlMQ0poZW5BaU9pSTJPV0prT0RObU1TMHhNVGN5TFRSaU1ESXRPREl4WVMxaU5XRXlZV1kxWVRNeVpHRWlMQ0pqYkdsbGJuUnVZVzFsSWpvaVpHVjJaV3h2Y0dWeUxXaHBjbVVpTENKcGMzTWlPaUpvZEhSd2N6cGNMMXd2Ykc5bmFXNHVZbTlzTG1OdmJTSXNJbk5qYjNCbGN5STZJbEpGVkVGSlRFVlNJaXdpWlhod0lqb3hOVGc0TURrNU9UZzNMQ0pwWVhRaU9qRTFPRGd3T1RrMk9EY3NJbUZwWkNJNklrTk1UbFJET21KbE1tSTNNREUyTFRjek5EWXRZek0yWlMxa01UTTRMVGMzTnpBNE1UY3paamRpWXlCVFRGSTZNVE0yTXpnMU9DSXNJbXAwYVNJNklqRmxaalJsWVRWbUxUZGtOR1l0TkROaE9TMWlabUUyTFRNNVpXVmpObUpoTVRCallTSjkuZ3d2MGZIcDBvcEhYQ2ppXzIyLWxtU240MlpxU1pNVW95WjZldmxXZXRudHJuby1DWHFlcVp5VkRYTUNiWEJkcDh1S3Q2MW96OXRsUWxuU3kxdUZqS2MzS1FrX2EweWpiMTdjcmgydHlUaEctYlljR3dzTE1PLU9INkVhb21yaFl0UTdEU3ZzNVAzMVh4NVlfdm41SnZ5cTZVOWltS213VGZXRXJuSS1zMGFvUTNwcjFpbnpPR3BDY3F3VWpyZmhoY0JJUGprWmNIRGV4QWNXTko4V0tiWk1IYmljOFNMdHBpc1k3V2FuMHdFTDYteWFuSDBrRFI1VHlaQnhPNFBzVVRmOG5uTXEzMDZrQkRhcjJkQ3hjTWxOa0UzdDNScFFVaWc3aWQycGxQTXJ1WEdTdU5BRXNsbXc0WTZCMXlJODZSOGNHalVFMW5qZDBhaTNMb04zNFBBIn0=','2020-05-12 18:48:07.715172'),('sl3hhpytexzw5kqg49ssnlbcel57kbgb','ZjdiNDc2YzcxMmJmNzI5YWRkZDkzZTY5NDA2NmJiY2IxZjBjM2QzODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkODhiZmFkMzkwN2RmODBiNDQ0NGQ3NzMxZmM3YjRkYmNiMzkwMzNhIiwienViIjoxMjMsImFjY2Vzc190b2tlbiI6IkJlYXJlciBleUpyYVdRaU9pSnljMkV5SWl3aVlXeG5Jam9pVWxNeU5UWWlmUS5leUp6ZFdJaU9pSTJPV0prT0RObU1TMHhNVGN5TFRSaU1ESXRPREl4WVMxaU5XRXlZV1kxWVRNeVpHRWlMQ0poZW5BaU9pSTJPV0prT0RObU1TMHhNVGN5TFRSaU1ESXRPREl4WVMxaU5XRXlZV1kxWVRNeVpHRWlMQ0pqYkdsbGJuUnVZVzFsSWpvaVpHVjJaV3h2Y0dWeUxXaHBjbVVpTENKcGMzTWlPaUpvZEhSd2N6cGNMMXd2Ykc5bmFXNHVZbTlzTG1OdmJTSXNJbk5qYjNCbGN5STZJbEpGVkVGSlRFVlNJaXdpWlhod0lqb3hOVGc0TURFMk9EWXdMQ0pwWVhRaU9qRTFPRGd3TVRZMU5qQXNJbUZwWkNJNklrTk1UbFJET21KbE1tSTNNREUyTFRjek5EWXRZek0yWlMxa01UTTRMVGMzTnpBNE1UY3paamRpWXlCVFRGSTZNVE0yTXpnMU9DSXNJbXAwYVNJNklqSXlOR015WlRnM0xUZGpORGd0TkdZMk5pMDVZMk14TFdFek1UWTROMk5sWlRJM05DSjkuSXRkUXFsSzR0VzRlNlI2R3QzUEtiVWZDRXNqVWZTTFJ6b3FSZDNFVEtjTENwNVRsTUJUZ0E1R0FTeHhMaGJCZFZ0TUZMcmpMUkN5Qm1IbnNUallqd1U2U0hhdW5GZDUtU25FM2EzNGIzdXJBWlpVREd1cUJUd2FsLUdNVzhEdy1WOTRsSk1XVndGVkRXTVFRN0lYZ0I4Z3FYV3BkMjB4YmlEZnp0RV9hUnpmeDQyNWlDZGtLQV9Ja0dPR3FRN29WQ3phRDJMUWU4UUFqTXhrOTZEckJSZFliWUF0dnpTQ1M3c0RxRjB1NEo2cGxKU3lYUXhZNWZOUS1MOEFha2VteTBRRjk4OHpNaVJBckdiUndES2UtV2xBdXEwNXpTWjRiT0lMbTlObVZ6MERjQllhRUtDYlNoUEp6RDMzcHE1VUxGNnpnN1RmTDRSNTdJUndGR05pWDhRIiwiY2xpZW50X2tleSI6IjY5YmQ4M2YxLTExNzItNGIwMi04MjFhLWI1YTJhZjVhMzJkYSIsInNlY3JldF9rZXkiOiJOZmFpbkNjbWJhZmlDVWl1dFY3SUttam44TmJPQ2J3NlhjMTZhLV9NRFZ5QzBqaGZiZWtOSXBRM3ozc05VSGhOSkpFaEszT1JTYmg4V1diZjl6U0dwUSIsInRva2VuIjoiQmVhcmVyIGV5SnJhV1FpT2lKeWMyRXlJaXdpWVd4bklqb2lVbE15TlRZaWZRLmV5SnpkV0lpT2lJMk9XSmtPRE5tTVMweE1UY3lMVFJpTURJdE9ESXhZUzFpTldFeVlXWTFZVE15WkdFaUxDSmhlbkFpT2lJMk9XSmtPRE5tTVMweE1UY3lMVFJpTURJdE9ESXhZUzFpTldFeVlXWTFZVE15WkdFaUxDSmpiR2xsYm5SdVlXMWxJam9pWkdWMlpXeHZjR1Z5TFdocGNtVWlMQ0pwYzNNaU9pSm9kSFJ3Y3pwY0wxd3ZiRzluYVc0dVltOXNMbU52YlNJc0luTmpiM0JsY3lJNklsSkZWRUZKVEVWU0lpd2laWGh3SWpveE5UZzRNRE0xTmpjMUxDSnBZWFFpT2pFMU9EZ3dNelV6TnpVc0ltRnBaQ0k2SWtOTVRsUkRPbUpsTW1JM01ERTJMVGN6TkRZdFl6TTJaUzFrTVRNNExUYzNOekE0TVRjelpqZGlZeUJUVEZJNk1UTTJNemcxT0NJc0ltcDBhU0k2SWpsak1EZ3lPV1ZqTFRoaE9UTXROR0pqTkMwNE1qWXlMV1ZpTVRjNE5EVXlaVFptTkNKOS5HZTBvTFdCMmZxaFFxbkFwQmFjRFM5N3NZY1ZfWTdqZFJyNWJDekJSX2E3S0JldFlxeHZvemVjemRoODVNQVFaeFNPSmY5b3Q4dWp3S2dhTjNCS1MzTnlMblY0QzVRSnYwelNsY2txTXhoOHdqQlFHRWl6dFJyckVtdGhRdXVIMEtjanJ6MlZCNGR0SG1lSTZmcllWYndRN0xtUGs0SVBfamprVE91UUhSM2lPcFowVmtYSk5TNjhndllycGZhUDZTdkg2ZWFndG04dmZubjBFa281c1d3SnNOS0hsVUV0N3Z2RkhFaUJ2NkhMamZIMU9hV2FISFpxVFp5czRWVkNIbnNOUi1YaWFsdzBObnp4dHcxbmZOcENmQ0g0WS1XdjVzSE1uSWFQR3J4Q3BQaUJ6Z1JleXN4YjM1ZFkxUC0weUs0a0RfN3dudGJ6SWZHdGJMd29jYWcifQ==','2020-05-12 00:56:15.620195');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shipment_shipmentitem`
--

DROP TABLE IF EXISTS `shipment_shipmentitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shipment_shipmentitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` varchar(30) NOT NULL,
  `order_item_id` varchar(30) NOT NULL,
  `title` longtext,
  `quantity` varchar(30) DEFAULT NULL,
  `offer_price` varchar(30) DEFAULT NULL,
  `shipment_id` int(11) NOT NULL,
  `fulfilment_method` varchar(3) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shipment_shipmentite_shipment_id_f1fe6a48_fk_shipment__idx` (`shipment_id`),
  CONSTRAINT `shipment_shipmentite_shipment_id_f1fe6a48_fk_shipment_` FOREIGN KEY (`shipment_id`) REFERENCES `shipment_shipmentretailer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shipment_shipmentitem`
--

LOCK TABLES `shipment_shipmentitem` WRITE;
/*!40000 ALTER TABLE `shipment_shipmentitem` DISABLE KEYS */;
INSERT INTO `shipment_shipmentitem` VALUES (1,'2877252670','BFC0000373770915',NULL,NULL,NULL,1,'FBB'),(2,'2920640550','BFC0000373560385',NULL,NULL,NULL,2,'FBB'),(3,'2920640550','BFC0000373560385',NULL,NULL,NULL,3,'FBB'),(4,'2919439470','BFC0000373387003',NULL,NULL,NULL,4,'FBB'),(5,'2919439470','BFC0000373387003',NULL,NULL,NULL,4,'FBB'),(6,'2918335920','2373228549',NULL,NULL,NULL,5,'FBB'),(7,'2918335920','2373228549',NULL,NULL,NULL,5,'FBB'),(8,'2910871500','2372153626',NULL,NULL,NULL,6,'FBB'),(9,'2910871500','2372153626',NULL,NULL,NULL,6,'FBB'),(10,'2910274500','2372070168',NULL,NULL,NULL,7,'FBB'),(11,'2909136170','2371902775',NULL,NULL,NULL,8,'FBB'),(12,'2870788630','2366436162',NULL,NULL,NULL,9,'FBB'),(13,'2870788630','2366436162',NULL,NULL,NULL,9,'FBB'),(14,'2878188480','2367494957',NULL,NULL,NULL,10,'FBR'),(15,'2878186540','2367494693',NULL,NULL,NULL,11,'FBR'),(16,'2878145890','2367489108',NULL,NULL,NULL,12,'FBR'),(17,'2878150030','2367489619',NULL,NULL,NULL,13,'FBR'),(18,'2878150030','2367489619',NULL,NULL,NULL,13,'FBR'),(19,'2878147630','2367489264',NULL,NULL,NULL,14,'FBR'),(20,'2878147630','2367489264',NULL,NULL,NULL,14,'FBR'),(21,'2878150860','2367489707',NULL,NULL,NULL,15,'FBR'),(22,'2878150860','2367489707',NULL,NULL,NULL,15,'FBR'),(23,'2878146990','2367489203',NULL,NULL,NULL,16,'FBR');
/*!40000 ALTER TABLE `shipment_shipmentitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shipment_shipmentretailer`
--

DROP TABLE IF EXISTS `shipment_shipmentretailer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shipment_shipmentretailer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shipment_id` int(11) NOT NULL,
  `shipment_date` datetime(6) NOT NULL,
  `transport_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_shipment_shipmentretailer_1_idx` (`shipment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shipment_shipmentretailer`
--

LOCK TABLES `shipment_shipmentretailer` WRITE;
/*!40000 ALTER TABLE `shipment_shipmentretailer` DISABLE KEYS */;
INSERT INTO `shipment_shipmentretailer` VALUES (1,724849260,'2020-03-04 19:23:25.000000',465285366),(2,724627419,'2020-03-03 22:28:56.000000',465050882),(3,724627419,'2020-03-03 22:28:56.000000',465050882),(4,724627160,'2020-03-03 22:27:26.000000',465050616),(5,724206868,'2020-03-02 15:45:01.000000',464615163),(6,723361306,'2020-02-27 20:48:10.000000',463746066),(7,723264631,'2020-02-27 15:07:33.000000',463646498),(8,723084558,'2020-02-26 21:35:16.000000',463459446),(9,718479058,'2020-02-07 18:29:24.000000',458697241),(10,719226009,'2020-02-11 08:22:32.000000',459463081),(11,719225910,'2020-02-11 08:21:47.000000',459462980),(12,719223851,'2020-02-11 08:09:53.000000',459460793),(13,719223849,'2020-02-11 08:09:53.000000',459460791),(14,719223847,'2020-02-11 08:09:53.000000',459460790),(15,719223845,'2020-02-11 08:09:53.000000',459460788),(16,719223850,'2020-02-11 08:09:53.000000',459460787);
/*!40000 ALTER TABLE `shipment_shipmentretailer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-02  4:41:18
