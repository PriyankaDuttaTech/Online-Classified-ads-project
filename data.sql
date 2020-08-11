-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Aug 29, 2019 at 12:20 PM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 5.6.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `data`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL COMMENT '1',
  `a_mail` varchar(255) NOT NULL,
  `a_pass` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `a_mail`, `a_pass`, `name`) VALUES
(1, 'Adsfactoryadmin@mail.com', 'Adsadmin', 'Priyanka');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `cat_id` int(11) NOT NULL COMMENT '1',
  `category_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`cat_id`, `category_name`) VALUES
(1, 'Automobiles'),
(2, 'Electronics');

-- --------------------------------------------------------

--
-- Table structure for table `post_table`
--

CREATE TABLE `post_table` (
  `post_id` int(11) NOT NULL COMMENT '1',
  `pname` varchar(150) NOT NULL,
  `pkey` varchar(255) NOT NULL,
  `pprice` int(10) NOT NULL,
  `fpath` varchar(255) NOT NULL,
  `pbrand` varchar(100) NOT NULL,
  `pdate` date NOT NULL,
  `approve` enum('0','1') DEFAULT '0',
  `User_id` int(11) DEFAULT NULL,
  `cat_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `post_table`
--

INSERT INTO `post_table` (`post_id`, `pname`, `pkey`, `pprice`, `fpath`, `pbrand`, `pdate`, `approve`, `User_id`, `cat_id`) VALUES
(184, 'Maruti', 'good condition', 12000000, 'images2/image_1.png', 'MARUTI', '2019-08-04', '1', 1, 1),
(186, 'suzuki', 'good condition and high seed', 1233333, 'images2/icon1.png', 'Maruti ', '2019-08-01', '1', 1, 1),
(188, 'Lenovo vibe k4 note', 'High quality camera,Good battery optimization,3 GB RAM', 4500, 'images2/product.jpg', 'Lenovo', '2019-08-16', '1', 1, 2),
(192, 'Galaxy s7', 'Good battery optimization,13mp camera', 7000, 'images2/product2.jpg', 'Samsung', '2019-08-04', '1', 6, 2),
(193, 'Micromax', 'Good battery optimization', 2000, 'images2/product5.jpg', 'Micromax', '2019-08-13', '1', 6, 2),
(194, 'redmi note 4', 'Good battery optimization,13mp camera', 10000, 'images2/product.jpg', 'xiomi', '2019-08-08', '1', 6, 2),
(195, 'Micromax', 'Good battery optimization,13mp camera', 2500, 'images2/product.jpg', 'Micromax', '2019-08-29', '1', 9, 2);

-- --------------------------------------------------------

--
-- Table structure for table `userdata`
--

CREATE TABLE `userdata` (
  `User_id` int(11) NOT NULL COMMENT '1',
  `F_name` varchar(255) NOT NULL,
  `L_name` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `city` varchar(255) NOT NULL,
  `pin` varchar(20) NOT NULL,
  `Password` varchar(244) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userdata`
--

INSERT INTO `userdata` (`User_id`, `F_name`, `L_name`, `Address`, `mobile`, `city`, `pin`, `Password`, `email`) VALUES
(1, 'Priyanka ', 'Dutta', 'Jajodia garden , belur', '9088647002', 'Kolkata', '711202', 'Pikunit', 'piku@mail.c0m'),
(2, 'Lalantika', 'Sengupta', 'Bagnan', '12345678', 'Kolkata', '711344', 'Kuttush', 'lallu@mail.c0m'),
(5, 'Piku', 'Dutta', 'Jajodia garden , belur', '9088647002', 'Kolkata', '711202', 'sdf', 'piku@mail.c0m'),
(6, 'Lalanika', 'Sengupta', 'Bagnan', '12345678', 'Kolkata', '711344', 'Lallu', 'lallu@mail.c0m'),
(7, 'erettfhfmj', 'hjkjnknj', 'Jajodia garden , belur', '1234567', 'Kolkata', '711202', '1234', 'qw@mail.com'),
(8, 'debjoyti', 'Bhattacharjee', 'Jajodia garden , belur', '12345678', 'Kolkata', '711202', 'Lallu', 'justin@mail.com'),
(9, 'Saumitra', 'Das', 'CZ-32 Metropolitan', '9876543210', 'Kolkata', '700105', '123456', 'sau@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`cat_id`);

--
-- Indexes for table `post_table`
--
ALTER TABLE `post_table`
  ADD PRIMARY KEY (`post_id`);

--
-- Indexes for table `userdata`
--
ALTER TABLE `userdata`
  ADD PRIMARY KEY (`User_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1', AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `cat_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1', AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `post_table`
--
ALTER TABLE `post_table`
  MODIFY `post_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1', AUTO_INCREMENT=196;
--
-- AUTO_INCREMENT for table `userdata`
--
ALTER TABLE `userdata`
  MODIFY `User_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1', AUTO_INCREMENT=10;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
