import re
config='''

-- MySQL dump 10.13  Distrib 5.6.23, for Win64 (x86_64)
--
-- Host: oma-gh-slams-prod.cluster-c8ezhkiocsku.eu-west-1.rds.amazonaws.com    Database: dbslamsoldmutual
-- ------------------------------------------------------
-- Server version       5.7.12

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

'''

key=False


pattern = r'Table structure for table `travelpolicycategory`'
cypher='latin1'
f=open('new.back','+wb')
f.write(config.encode(cypher))
f.close()

with open("Dump20240429.sql",encoding=cypher) as infile:
    for line in infile:

        matches = re.finditer(pattern, line)
        for match in matches:
            key= True
            print("started")
        if (key): 
                # print("c")           
                # f.write(pastcode)
                f=open('new.back','+ab')
                f.write(line.encode(cypher))
                f.close()
               
# f.close()