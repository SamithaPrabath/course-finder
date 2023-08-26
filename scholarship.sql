-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: Aug 26, 2023 at 01:21 PM
-- Server version: 5.7.28
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `course_finder_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `scholarship`
--

DROP TABLE IF EXISTS `scholarship`;
CREATE TABLE IF NOT EXISTS `scholarship` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tittle` varchar(150) NOT NULL,
  `campus` varchar(50) NOT NULL,
  `sub_tittle` varchar(150) NOT NULL,
  `desciption` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `scholarship`
--

INSERT INTO `scholarship` (`id`, `tittle`, `campus`, `sub_tittle`, `desciption`) VALUES
(1, 'All Island A/L Best Performance based scholarship offers (Nena Diriya)', 'SLIIT', 'Scholarships awarded for A/L examination', 'This is offered to the students who rank highest in the G.C.E (A/L) Mathematics or Commerce stream examination results in the country. These Island ranking student are be eligible for a Full Tuition fee waiver and a monthly stipend for the Academic Semester as a fulltime student. Scholarships are offered at the discretion of the Nena Diriya Endowmnet board'),
(3, 'Broad Based Scholarships for Outstanding Performance in Advanced Level Examination', 'SLIIT', 'Scholarships awarded for A/L examination.', 'Upon enrollment, students with 3A* in Cambridge/Edexcel A/L OR 3As in local GCE A/L in one and the same sitting and fulfilling SLIIT scholarship criteria will be eligible to APPLY for Academic Performance-Based Scholarships. Applications are called once a year after completing the undergradutes intake of the given year.\r\nApplications are reviewed by a scholarship review committee and elegible candidates are recommended for approval of the institute. \r\n'),
(4, 'Broad Based Scholarships for Outstanding achievements in Sports and Extra-curricular Activities in school', 'SLITT', 'Scholarships awarded for extracurricular activities.', 'Upon enrollment, students who have performed and achieved at international, national and provincial level, fulfilling SLIIT scholarship criteria will be eligible to APPLY for Sports and Extra-Curricular performance-based scholarship. Applications with evidence are reviewed by a scholarship review committee on a point-based criteria and eligible candidates are recommended for approval of the institute. '),
(5, 'Outstanding Performances in Sports and Extra-curricular Activities in the undergraduate period', 'SLITT', 'Scholarships awarded for extracurricular activities', 'Performed and achieved at international, national and provincial level, fulfilling SLIIT scholarship criteria are  eligible to apply for Sports and Extra-Curricular performance-based scholarship. Applications are reviewed by a scholarship review committee and eligible candidates are recommended for approval of the institute. '),
(6, 'Broad Based Scholarships for Outstanding Semester Based Performance on undergraduates ', 'SLITT', 'Scholarships awarded for academic performance.', 'Undergraduates who achieve the highest in a given semester and ranks at Top 1% of SLIIT are considered to be awarded with a one semester fee waiver. The next 2% will be considered for a partial semester fee waiver. Applications are reviewed by a scholarship review committee and eligible candidates are recommended for approval of the institute. '),
(7, 'Industry partner\'s-based scholarships offers', 'SLITT', 'Scholarships awarded by Industry partners.', 'During the academic semester industry partners who have entered into agreements with SLIIT offers Merit-based Scholarship Schemes for undergraduates of SLIIT. This may consists of an offer of full tuition fee payment and offer of an internship with the company. Candidates selection and criteria is subject to the requirements of the Industry partner.\r\n\r\na. IFS\r\nb. LOLC\r\nc. MIT Esp\r\nd. Orel IT\r\n'),
(8, 'Ministry of Education Interest Free Loan Scheme student Scholarships', 'SLITT', 'Scholarships awarded by Ministry of Education', 'The student selected by the MoE are given 50% tuition fee waiver by the institute to complete\r\nthe degree\r\nhttps://www.mohe.gov.lk/index.php?option=com_content&view=article&id=345:ifsls&catid=2&Itemid=176&lang=en'),
(9, 'Virusara Priviledge', 'SLITT', 'Scholarships awarded by Virusara Priviledge', 'Offered under the Ranaviru Seva Authority and Ministry of Defence, SLIIT support this scheme by granting a special 10% discount for students eligible for enrollment under the Virusara Privilege Scheme for the \"Bachelor of Business Administration (Hon) Degree.”\r\nApplication - at the point of enrollment http://virusara.gov.lk/en/special-card.html'),
(10, 'Need Based Fee Concessions', 'SLITT', 'Other Scholarships awarded.', 'This scholarship was widely granted during the year 2019 (Easter attack), 2020, 2021 and 2022 (during and after Covid-19 pandemic) where businesses and occupations in general deteriorated.It is still active for students who are undergoing financial issues due to legitimate reasons'),
(11, 'Individual donor/ charity organizations-based sponsorships for students', 'SLITT', 'Other Scholarships awarded.', 'a. Sunshine Holdings\r\nb. Sumi Munasinghe scholarship for data science student\r\nc. Other private donors'),
(12, 'NIBM WISHWA SCHOLARSHIP SCHEME', 'NIBM', 'NIBM WISHWA SCHOLARSHIP SCHEME', 'Following are the details of the proposed Scholarship programme:\r\n•	Only the students who achieve an island rank in the GCE Advanced Level examination or pass GCE Advanced Level with extra-curricular activities will be eligible to apply for the Scholarship Scheme.\r\n•	The Scholarship Scheme will be offered once a year.\r\n•	The scholarship scheme will be for ten selected NIBM courses. Selected ten students will get the opportunity to read the first two years of a degree programme offered by School of Computing, School of Business, School of Humanities, School of Design and Productivity & Quality Centre. The scheme will cover the full course fee for the first two years of the programme. *The selected awardees will have to finance the final year of the degree programme.\r\n•	Application process will be fully online, and an academic panel will select the suitable candidates on a marking criteria. The selected list of awardees will be published in the NIBM Website.\r\n•	Eligibility: The scheme provides higher education opportunities for students from lower income families who perform exceptionally well in the GCE Advanced Level examination with an island rank and extracurricular activities. The applicants will have to provide authentic written evidence on the income level of the family certified by the Grama Niladhari and the Divisional Secretary of the area.\r\n•	Disqualification: Any form of canvassing through political or any other authority will immediately disqualify the applicant. Above criteria will be strictly followed to ensure the transparency of the selection process.\r\nNIBM has the sole authority to take the final decision on selection of students for the Scholarship Scheme.\r\n');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
