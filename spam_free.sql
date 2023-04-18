-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 04, 2023 at 05:54 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `spam_free`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `chat`
--

CREATE TABLE `chat` (
  `chat_id` int(10) NOT NULL,
  `friend_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `chat` varchar(160) NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL,
  `photo` varchar(11) DEFAULT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `chat`
--

INSERT INTO `chat` (`chat_id`, `friend_id`, `user_id`, `chat`, `date`, `time`, `photo`, `status`) VALUES
(1, 2, 1, 'hey', '2021-12-08', '11:58:19', NULL, ''),
(2, 1, 2, 'hello', '2021-12-08', '12:00:01', NULL, ''),
(3, 1, 3, 'good mornin', '2021-12-09', '10:44:45', NULL, ''),
(4, 3, 1, 'mornin mornin', '2021-12-09', '10:52:40', NULL, ''),
(5, 3, 5, 'hellooooo', '2021-12-09', '11:01:40', NULL, ''),
(6, 9, 3, 'hello', '2022-03-03', '02:00:23', NULL, ''),
(7, 11, 10, 'ho', '2023-02-03', '11:11:58', NULL, '[\'ham\']'),
(8, 11, 10, 'heyyyyyyyy', '2023-02-03', '11:12:38', NULL, '[\'ham\']'),
(9, 10, 11, 'poda panni', '2023-02-03', '11:15:04', NULL, '[\'ham\']'),
(10, 11, 10, 'hello ', '2023-02-03', '11:17:30', NULL, '[\'ham\']'),
(11, 11, 10, 'cash 50000 rs', '2023-02-03', '11:18:16', NULL, '[\'ham\']'),
(12, 10, 11, 'you have won 5000 rs to claim contact me', '2023-02-03', '11:22:20', NULL, '[\'spam\']');

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

CREATE TABLE `comment` (
  `comment_id` int(10) NOT NULL,
  `friend_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `comment` varchar(100) NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL,
  `share_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `comment`
--

INSERT INTO `comment` (`comment_id`, `friend_id`, `user_id`, `comment`, `date`, `time`, `share_id`) VALUES
(1, 3, 2, 'nicee', '2021-12-08', '12:36:28', 2),
(3, 1, 7, 'good one', '2021-12-08', '04:11:20', 3),
(7, 6, 1, 'good', '2022-03-02', '10:35:49', 5),
(8, 6, 1, 'nice pic', '2022-03-02', '10:38:28', 5),
(10, 9, 3, 'nice pic', '2022-03-03', '02:00:02', 6);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-10-27 05:07:12.729854'),
(2, 'auth', '0001_initial', '2021-10-27 05:07:13.159395'),
(3, 'admin', '0001_initial', '2021-10-27 05:07:13.295683'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-10-27 05:07:13.306310'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-10-27 05:07:13.316650'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-10-27 05:07:13.371133'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-10-27 05:07:13.392113'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-10-27 05:07:13.410312'),
(9, 'auth', '0004_alter_user_username_opts', '2021-10-27 05:07:13.421705'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-10-27 05:07:13.454876'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-10-27 05:07:13.458679'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-10-27 05:07:13.462135'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-10-27 05:07:13.477768'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-10-27 05:07:13.510483'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-10-27 05:07:13.541774'),
(16, 'auth', '0011_update_proxy_permissions', '2021-10-27 05:07:13.541774'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-10-27 05:07:13.565557'),
(18, 'sessions', '0001_initial', '2021-10-27 05:07:13.600888');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1j5fw9iq4ttsk9wmli43o5kc4i7s8np9', 'eyJ1aWQiOjMsIm5hbWUiOiJhIn0:1o5jQB:hoT8T8JcvGVa8r2mJ6u4YJVY9STPfv1ERarkwm7sazU', '2022-07-11 07:44:35.372568'),
('79ecjesuwdh4i8vw83k5lg9boajb35nh', 'eyJ1aWQiOjN9:1mvH1Z:QxjWufh_4VuwjijwJzzw4vuIwz6cbZnspkURyugqvU4', '2021-12-23 10:51:41.556370'),
('9cpn86jckuov0z8kjcmriwn5iqiwhv4e', 'eyJ1aWQiOjksIm5hbWUiOiJhbiJ9:1mvC7q:GSKFC9I9mipUi2bNX2Iq5_LBwdKNN4FMgI_zn_gm1UE', '2021-12-23 05:37:50.057607'),
('g9zex7emzu5f8x68ojsr2bxlixo6dupz', 'eyJ1aWQiOjEsIm5hbWUiOiJ2YXJ1biJ9:1mjw8w:EWKj4nb9B8HjpRJDqg1XTI1QCbxzn6AYBceCC4voQz4', '2021-11-22 04:20:26.121436'),
('okqd3gti46sf3ttlxqi16ktv8rlz1mng', 'eyJ1aWQiOjF9:1mjwUQ:R1rAQ22eRsOXzNv4vQA6nOr863-GHicVw4aOi-6Sh0Q', '2021-11-22 04:42:38.410622'),
('tdmekk4m6kl75dq39dnnhc1nl0xerx65', 'eyJ1aWQiOjEwLCJuYW1lIjoiYW5qYWxpIn0:1pO0Ej:TuN8uAydl6hRK8FC6-OOLNouLa_LparCLLKxdVeQDTk', '2023-02-17 17:52:33.317850'),
('zf8a51m0n9fpeh613446zzfl27tjbz4p', 'eyJ1aWQiOjksIm5hbWUiOiJhIn0:1nPgvd:3hucnCS86BpAO-itospEuHeq5w_n-u8zFuegaPlLHa4', '2022-03-17 08:35:17.298096');

-- --------------------------------------------------------

--
-- Table structure for table `friends`
--

CREATE TABLE `friends` (
  `friend_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `f_user_id` int(10) NOT NULL,
  `request_status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `friends`
--

INSERT INTO `friends` (`friend_id`, `user_id`, `f_user_id`, `request_status`) VALUES
(1, 1, 2, 'accepted'),
(3, 2, 1, 'accepted'),
(4, 2, 3, 'accepted'),
(8, 3, 2, 'accepted'),
(9, 1, 4, 'accepted'),
(11, 4, 1, 'accepted'),
(12, 1, 3, 'accepted'),
(13, 7, 1, 'accepted'),
(14, 1, 7, 'accepted'),
(15, 3, 1, 'accepted'),
(16, 3, 5, 'accepted'),
(17, 5, 3, 'accepted'),
(18, 6, 1, 'accepted'),
(19, 1, 6, 'accepted'),
(20, 9, 1, 'requested'),
(21, 9, 3, 'accepted'),
(22, 3, 9, 'accepted'),
(23, 11, 10, 'accepted'),
(24, 10, 11, 'accepted');

-- --------------------------------------------------------

--
-- Table structure for table `like_photo`
--

CREATE TABLE `like_photo` (
  `like_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `like_count` varchar(50) NOT NULL,
  `share_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `like_photo`
--

INSERT INTO `like_photo` (`like_id`, `user_id`, `like_count`, `share_id`) VALUES
(1, 2, '0', 1),
(2, 3, '1', 2),
(3, 1, '1', 3),
(4, 7, '0', 4),
(5, 6, '0', 5),
(6, 9, '1', 6),
(7, 9, '0', 7);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `login_id` int(10) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(30) NOT NULL,
  `user_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`login_id`, `username`, `password`, `type`, `user_id`) VALUES
(1, 'anagha02@gmail.com', 'anagha', 'user pending', 1),
(2, 'rahul18@gmail.com', 'rahul', 'user pending', 2),
(3, 'anjali', 'anjali', 'user', 3),
(4, 'manu11@gmail.com', 'manu', 'user', 4),
(5, 'roshi08@gmail.com', 'roshi', 'user pending', 5),
(6, 'arun23@gmail.com', 'aruns', 'user', 6),
(7, 'sherin29@gmail.com', 'sherina', 'user', 7),
(8, 'rani04@gmail.com', 'rani', 'user pending', 8),
(9, 'admin', 'admin', 'admin', 9),
(10, 'rakeshkk5780@gmail.com', 'rakesh', 'user', 9),
(11, 'anumoop@gmail.com', 'moops', 'user', 10),
(12, 'mwle@gmail.com', '123456789', 'user', 11);

-- --------------------------------------------------------

--
-- Table structure for table `reported_comments`
--

CREATE TABLE `reported_comments` (
  `report_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `comment_id` int(10) NOT NULL,
  `report` varchar(50) NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reported_comments`
--

INSERT INTO `reported_comments` (`report_id`, `user_id`, `comment_id`, `report`, `date`, `time`) VALUES
(1, 2, 2, 'I swear some people iq is insanely low\'', '2021-12-08', '02:59:01'),
(2, 5, 4, 'I swear some people iq is insanely low\'', '2021-12-09', '04:19:42'),
(3, 1, 4, 'stupid monkey face', '2022-03-02', '10:07:58'),
(6, 1, 9, 'stupid idiot', '2022-03-02', '10:40:28'),
(7, 6, 9, 'stupid', '2022-03-02', '12:08:41'),
(8, 3, 9, 'stupid monkey face', '2022-03-03', '01:58:42');

-- --------------------------------------------------------

--
-- Table structure for table `share`
--

CREATE TABLE `share` (
  `share_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `media` varchar(100) NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `share`
--

INSERT INTO `share` (`share_id`, `user_id`, `media`, `date`, `time`) VALUES
(1, 2, '2nd-item.jpg', '2021-12-08', '12:04:01'),
(2, 3, 'photo10.jpg', '2021-12-08', '12:17:21'),
(3, 1, 'photo11.jpg', '2021-12-08', '12:18:06'),
(4, 7, 'team4.jpg', '2021-12-08', '03:55:31'),
(5, 6, 'OIP (1).jpg', '2022-03-02', '10:01:52'),
(6, 9, 'cropped-Shammi.png', '2022-03-03', '01:53:49'),
(7, 9, 'OIP.jpg', '2022-03-03', '01:54:21');

-- --------------------------------------------------------

--
-- Table structure for table `user_reg`
--

CREATE TABLE `user_reg` (
  `user_id` int(10) NOT NULL,
  `username` varchar(50) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `phno` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `profile_photo` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_reg`
--

INSERT INTO `user_reg` (`user_id`, `username`, `dob`, `gender`, `phno`, `email`, `password`, `profile_photo`, `status`) VALUES
(1, 'Anagha', '2005-02-02', 'Female', '8909764532', 'anagha02@gmail.com', 'anagha', 'girl1.jpg', 'cyberbullying detected'),
(2, 'Rahul', '1994-11-18', 'male', '9045678932', 'rahul18@gmail.com', 'rahul', 'boy1.jpg', 'cyberbullying detected'),
(3, 'Anjali', '2000-06-07', 'Female', '7068945632', 'anjali07@gmail.com', 'anjali', 'girl2.jpg', 'approved'),
(4, 'Manu', '1998-05-11', 'male', '8036965623', 'manu11@gmail.com', 'manu', 'boy2.jpg', 'approved'),
(5, 'Roshi', '2011-12-08', 'Female', '7063968512', 'roshi08@gmail.com', 'roshi', 'girl5.jpg', 'cyberbullying detected'),
(6, 'Arun', '2015-08-23', 'male', '6789526321', 'arun23@gmail.com', 'aruns', 'boy3.jpg', 'approved'),
(8, 'Rani', '2021-11-04', 'Other', '8025639687', 'rani04@gmail.com', 'rani', 'girl4.jpg', 'rejected'),
(9, 'rakesh', '1986-02-18', 'male', '9539497818', 'rakeshkk5780@gmail.com', 'rakesh', 'OIP (2).jpg', 'approved'),
(10, 'Anoop Bk', '2000-08-03', 'male', '8846733636', 'anumoop@gmail.com', 'moops', 'gran-turismo-34893-35697-hd-wallpapers.jpg', 'approved'),
(11, 'melvin', '1998-03-16', 'male', '8848123611', 'mwle@gmail.com', '123456789', 'gran-turismo-34893-35697-hd-wallpapers.jpg', 'approved');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `chat`
--
ALTER TABLE `chat`
  ADD PRIMARY KEY (`chat_id`);

--
-- Indexes for table `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`comment_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `friends`
--
ALTER TABLE `friends`
  ADD PRIMARY KEY (`friend_id`);

--
-- Indexes for table `like_photo`
--
ALTER TABLE `like_photo`
  ADD PRIMARY KEY (`like_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `reported_comments`
--
ALTER TABLE `reported_comments`
  ADD PRIMARY KEY (`report_id`);

--
-- Indexes for table `share`
--
ALTER TABLE `share`
  ADD PRIMARY KEY (`share_id`);

--
-- Indexes for table `user_reg`
--
ALTER TABLE `user_reg`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `chat`
--
ALTER TABLE `chat`
  MODIFY `chat_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `comment`
--
ALTER TABLE `comment`
  MODIFY `comment_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `friends`
--
ALTER TABLE `friends`
  MODIFY `friend_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `like_photo`
--
ALTER TABLE `like_photo`
  MODIFY `like_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `login_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `reported_comments`
--
ALTER TABLE `reported_comments`
  MODIFY `report_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `share`
--
ALTER TABLE `share`
  MODIFY `share_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `user_reg`
--
ALTER TABLE `user_reg`
  MODIFY `user_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
