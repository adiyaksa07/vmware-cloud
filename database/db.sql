-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 28, 2024 at 12:08 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rhani_cloud`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `createdServers` tinyint(1) NOT NULL,
  `servers` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`, `createdServers`, `servers`) VALUES
(19, 'jamaludin123', 'jamaludin123@aa.com', 'jamaludin123', 1, ''),
(20, 'mewing', 'mewing@gmail.com', 'mewing', 1, ''),
(21, 'sigma', 'sigma@gmail.com', 'sigma', 1, ''),
(23, 'laskarpelangi', 'laskarpelangi@gmail.com', 'laskarpelangi', 0, 'I9MJJEFIV3PA27DG046AFREETKDJVG9G'),
(24, 'asd12', 'asd12@gmail.com', 'asd12', 0, 'LMTS0QPOC0HSKNVBIFT11RN4E24HEQF3'),
(25, 'laskarpelangi12', 'laskarpelangi12@gmail.com', 'laskarpelangi12', 0, 'J9B8HPG5SC5SVAJ4EA8R9HILTEOK31IQ'),
(26, 'jamaludin12323', 'jamaludin12323@gaming.com', 'jamaludin12323', 0, 'UPCLCBCS5O3FMDNC38GF5KKVOQE4JGO8'),
(27, 'laskarpelangi1', 'laskarpelangi1@gmail.com', 'laskarpelangi1', 1, ''),
(28, 'page_created_server', 'page_created_server@gg.com', 'page_created_server', 0, '6CD7P4KR5MI83KLORT8FARG3UCDJP2U9'),
(29, 'rhani', 'rhani@gmail.com', 'rhani', 0, 'J4TJSK7PBC0D7SLLTCUMHB9379MJARF9'),
(30, 'sss', 'ss@sd.com', 'ss', 1, ''),
(31, 'dd', 'dddd@dd', 'dd', 0, 'PI96LS1SFJLRMRUJU34TCF0NI881FC4E');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
