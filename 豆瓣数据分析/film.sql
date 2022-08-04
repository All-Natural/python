/*
 Navicat Premium Data Transfer

 Source Server         : films
 Source Server Type    : SQLite
 Source Server Version : 3030001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3030001
 File Encoding         : 65001

 Date: 28/08/2021 16:59:16
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for film
-- ----------------------------
DROP TABLE IF EXISTS "film";
CREATE TABLE "film" (
  "fid" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "fno" text(20) NOT NULL,
  "fname" text(50) NOT NULL
);

-- ----------------------------
-- Records of film
-- ----------------------------
INSERT INTO "film" VALUES (1, 34880302, '人潮汹涌');
INSERT INTO "film" VALUES (2, 34841067, '你好李焕英');
INSERT INTO "film" VALUES (3, 26826330, '刺杀小说家');
INSERT INTO "film" VALUES (4, 26935283, '侍神令');
INSERT INTO "film" VALUES (6, 26794435, '哪吒之魔童降世');
INSERT INTO "film" VALUES (7, 27605542, '司藤');
INSERT INTO "film" VALUES (11, 26617075, '云顶天宫');
INSERT INTO "film" VALUES (31, 30435124, '白蛇2');
INSERT INTO "film" VALUES (32, 30174085, '怒火·重案 怒火');
INSERT INTO "film" VALUES (33, 35161768, '夏日友晴天');
INSERT INTO "film" VALUES (34, 35202793, '扫黑风暴');
INSERT INTO "film" VALUES (35, 25828589, '黑寡妇 Black Widow (2021)');
INSERT INTO "film" VALUES (36, 35288767, '革命者');
INSERT INTO "film" VALUES (37, 34845781, '鬼灭之刃 剧场版 无限列车篇');
INSERT INTO "film" VALUES (38, 26703121, '黑白魔女库伊拉 Cruella');
INSERT INTO "film" VALUES (40, 35472124, '普吉岛的最后黄昏');

-- ----------------------------
-- Auto increment value for film
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 40 WHERE name = 'film';

PRAGMA foreign_keys = true;
