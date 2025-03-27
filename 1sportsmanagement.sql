-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 28, 2024 at 09:49 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1sportsmanagement`
--

-- --------------------------------------------------------

--
-- Table structure for table `applytb`
--

CREATE TABLE `applytb` (
  `aid` bigint(250) NOT NULL auto_increment,
  `Ename` varchar(250) NOT NULL,
  `Place` varchar(250) NOT NULL,
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Dob` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Adress` varchar(250) NOT NULL,
  `Pincode` varchar(250) NOT NULL,
  `Height` varchar(250) NOT NULL,
  `Weight` varchar(250) NOT NULL,
  `Profile` varchar(250) NOT NULL,
  `Proof` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `cat` varchar(250) NOT NULL,
  PRIMARY KEY  (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `applytb`
--


-- --------------------------------------------------------

--
-- Table structure for table `categorytb`
--

CREATE TABLE `categorytb` (
  `cid` bigint(250) NOT NULL auto_increment,
  `category` varchar(250) NOT NULL,
  PRIMARY KEY  (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `categorytb`
--


-- --------------------------------------------------------

--
-- Table structure for table `eventtb`
--

CREATE TABLE `eventtb` (
  `eid` bigint(250) NOT NULL auto_increment,
  `Ename` varchar(250) NOT NULL,
  `Category` varchar(250) NOT NULL,
  `Place` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  `Time` varchar(250) NOT NULL,
  `Date1` varchar(250) NOT NULL,
  `Time1` varchar(250) NOT NULL,
  `Image` varchar(250) NOT NULL,
  PRIMARY KEY  (`eid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `eventtb`
--


-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `uid` bigint(250) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Adress` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `regtb`
--


-- --------------------------------------------------------

--
-- Table structure for table `winnertb`
--

CREATE TABLE `winnertb` (
  `wid` bigint(250) NOT NULL auto_increment,
  `PlayerName` varchar(250) NOT NULL,
  `Category` varchar(250) NOT NULL,
  `Pos` varchar(250) NOT NULL,
  PRIMARY KEY  (`wid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `winnertb`
--

