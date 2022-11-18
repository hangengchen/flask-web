/*
 Navicat Premium Data Transfer

 Source Server         :
 Source Server Type    : MySQL
 Source Server Version : 80020
 Source Host           : localhost:3306
 Source Schema         : music

 Target Server Type    : MySQL
 Target Server Version : 80020
 File Encoding         : 65001

 Date: 25/5/2021 14:25:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`email`),
  UNIQUE KEY `admin_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of admin
-- ----------------------------
BEGIN;
INSERT INTO `admin` VALUES (1, 'admin@kiki-group.top', 'pbkdf2:sha256:150000$U6pefrSk$80167a721f799a6c9ec01a8bfc472b1ed9ffae7e973dd5b1fd9af1a5634c405f', '2020-11-19 15:42:37');
INSERT INTO `admin` VALUES (3, 'admin@admin.com', 'pbkdf2:sha256:150000$U6pefrSk$80167a721f799a6c9ec01a8bfc472b1ed9ffae7e973dd5b1fd9af1a5634c405f', NULL);
COMMIT;

-- ----------------------------
-- Table structure for album
-- ----------------------------
DROP TABLE IF EXISTS `album`;
CREATE TABLE `album` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `creater_id` int NOT NULL,
  `music_id` int DEFAULT NULL,
  PRIMARY KEY (`id`,`creater_id`),
  KEY `music` (`music_id`),
  KEY `user` (`creater_id`),
  CONSTRAINT `album_creater` FOREIGN KEY (`creater_id`) REFERENCES `business` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `album_music` FOREIGN KEY (`music_id`) REFERENCES `vinyls` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of album
-- ----------------------------
BEGIN;
INSERT INTO `album` VALUES (2, 'none', 2, 2);
INSERT INTO `album` VALUES (3, 'none', 2, 3);
INSERT INTO `album` VALUES (8, 'none', 2, 334);
COMMIT;

-- ----------------------------
-- Table structure for business
-- ----------------------------
DROP TABLE IF EXISTS `business`;
CREATE TABLE `business` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`email`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of business
-- ----------------------------
BEGIN;
INSERT INTO `business` VALUES (2, '1@1.business', 'pbkdf2:sha256:150000$8u9zZdYQ$a9ca19357c99fcada670255e7cd9eba55c13df87c37873602b2b0768512320e9', NULL);
COMMIT;

-- ----------------------------
-- Table structure for music_list
-- ----------------------------
DROP TABLE IF EXISTS `music_list`;
CREATE TABLE `music_list` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `creater_id` int NOT NULL,
  `music_id` int DEFAULT NULL,
  PRIMARY KEY (`id`,`creater_id`),
  KEY `music` (`music_id`),
  KEY `user` (`creater_id`),
  CONSTRAINT `music` FOREIGN KEY (`music_id`) REFERENCES `vinyls` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user` FOREIGN KEY (`creater_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of music_list
-- ----------------------------
BEGIN;
INSERT INTO `music_list` VALUES (5, 'aa', 2, 3);
INSERT INTO `music_list` VALUES (8, '1@1.com', 2, 3);
INSERT INTO `music_list` VALUES (11, '1@1.com', 2, 2);
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`email`),
  KEY `id` (`id`),
  KEY `user` (`id`,`email`),
  KEY `user_2` (`id`,`email`,`password`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (2, '1@1.com', 'pbkdf2:sha256:150000$dZeBkWvS$4fa9b5c5dfc44bc01891fd5205c0c3828857facdcc15ebcede354839bfcc4e75', '2020-11-22 19:45:24');
INSERT INTO `user` VALUES (12, '2@1.com', 'pbkdf2:sha256:150000$FFNmq7Wy$ddc1496c9b6c8a0e70ea87883c972d86b5595c9ce14437619cd1c7f1e30f7860', NULL);
INSERT INTO `user` VALUES (13, '3@1.com', 'pbkdf2:sha256:150000$w7ZFXvhp$ed0006eaac7626dc0d01bba10fb50b2db391d37267d020514687b62b8dc21830', NULL);
COMMIT;

-- ----------------------------
-- Table structure for vinyls
-- ----------------------------
DROP TABLE IF EXISTS `vinyls`;
CREATE TABLE `vinyls` (
  `id` int NOT NULL AUTO_INCREMENT,
  `add_id` int NOT NULL,
  `addtime` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  `name` varchar(50) NOT NULL,
  `singer` varchar(50) DEFAULT NULL,
  `price` decimal(10,2) NOT NULL,
  `picture` varchar(255) DEFAULT NULL,
  `infomation` varchar(255) DEFAULT NULL,
  `musicpath` varchar(255) DEFAULT NULL,
  `lyric` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`,`add_id`),
  KEY `add_id` (`add_id`),
  KEY `id` (`id`),
  CONSTRAINT `add_id` FOREIGN KEY (`add_id`) REFERENCES `business` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=339 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of vinyls
-- ----------------------------
BEGIN;
INSERT INTO `vinyls` VALUES (2, 2, '2020-12-14 16:33:36', 'Tea picking period', 'Shuangsheng', 19.00, '/static/custom/img/02.jpg', 'In June 2015, the cover song \"Gu Meng\" was released on the original music website \"5sing\"; in the same year, the original song \"tea picking\" was released [2]. In March 2018,', '/static/custom/mp3/02.mp3', '/static/custom/lrc/02.lrc');
INSERT INTO `vinyls` VALUES (3, 2, '2020-12-14 16:33:41', 'hide', 'Shuangsheng', 19.00, '/static/custom/img/03.jpg', 'In June 2015, the cover song \"Gu Meng\" was released on the original music website \"5sing\"; in the same year, the original song \"tea picking\" was released [2]. In March 2019,', '/static/custom/mp3/03.mp3', '/static/custom/lrc/03.lrc');
INSERT INTO `vinyls` VALUES (334, 2, '2020-12-18 16:33:07', 'Gu Meng', 'Shuangsheng', 20.00, '/static/custom/img/1608280387.493935.jpg', 'none', '/static/custom/mp3/1608280387.493935.mp3', '/static/custom/lrc/1608280387.493935.lrc');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
