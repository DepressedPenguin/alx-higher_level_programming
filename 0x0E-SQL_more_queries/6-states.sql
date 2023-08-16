-- creat untiq
create database if not exists hbtn_0d_usa;
USE hbtn_0d_usa;
create table if not exists states (
id INT not null PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256) not null
);
