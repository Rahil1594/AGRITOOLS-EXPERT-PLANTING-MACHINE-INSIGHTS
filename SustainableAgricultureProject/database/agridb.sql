-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 05, 2024 at 11:11 AM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `agridb`
--
CREATE DATABASE IF NOT EXISTS `agridb` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `agridb`;

-- --------------------------------------------------------

--
-- Table structure for table `costtable`
--

CREATE TABLE IF NOT EXISTS `costtable` (
  `pid` int(11) DEFAULT NULL,
  `pname` varchar(50) DEFAULT NULL,
  `nodevice` int(11) DEFAULT NULL,
  `cost` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `farmertable`
--

CREATE TABLE IF NOT EXISTS `farmertable` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `address` varchar(250) DEFAULT NULL,
  `cname` varchar(50) DEFAULT NULL,
  `mno` varchar(20) DEFAULT NULL,
  `uname` varchar(50) DEFAULT NULL,
  `pword` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

-- --------------------------------------------------------

--
-- Table structure for table `planttable`
--

CREATE TABLE IF NOT EXISTS `planttable` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `pname` varchar(50) DEFAULT NULL,
  `pimage` varchar(250) DEFAULT NULL,
  `plocation` varchar(100) DEFAULT NULL,
  `devicename` varchar(50) DEFAULT NULL,
  `devicedesc` varchar(250) DEFAULT NULL,
  `devicevideo` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
