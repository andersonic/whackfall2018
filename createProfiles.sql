# createProfiles.sql

USE songbyrd;

DROP TABLE if exists user;
CREATE TABLE user(
	uid int(10) unsigned AUTO_INCREMENT PRIMARY KEY NOT NULL,
    email varchar(50) NOT NULL,
    name varchar(50) NOT NULL,
	hashed char(60) NOT NULL, 
    tagline varchar(50),
    about_you varchar(5000),
    causes varchar(5000),
    social_media varchar(1000)
)