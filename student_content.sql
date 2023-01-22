drop table if exists student;
create table student (
id integer primary key autoincrement,
username text not null,
name text not null,
pwd text not null,
gender text,
hostel text,
room text,
mess text,
due integer);

create table admin (
id integer primary key autoincrement,
username text not null,
name text not null,
pwd text not null,
phno text);
