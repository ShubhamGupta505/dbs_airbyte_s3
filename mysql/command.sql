CREATE DATABASE IF NOT EXISTS ecommernce;

-- drop user 'airbyte'@'%';

FLUSH PRIVILEGES;

CREATE USER 'airbyte'@'%' IDENTIFIED BY 'password';

GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'airbyte'@'%';

use ecommernce;

-- create table orders (
-- 	_id int auto_increment primary key,
--     store_id int not null,
--     order_date varchar(255) not null,
--     channel varchar(25),
--     country varchar(25),
--     total float not null,
--     status varchar(25)
-- );

-- insert into orders (_id, store_id, order_date, channel, country, total, status) values (1, 100, '2021-08-15', 'STORE', 'Hungary', 173.04, 'ACTIVE');


create table orders (
	_id INT primary key,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	gender VARCHAR(50),
	city VARCHAR(50),
	email VARCHAR(50)
);
insert into orders (_id, first_name, last_name, gender, city, email) values (1, 'Renaud', 'McGonigal', 'Male', 'Mae Hi', 'rmcgonigal0@networkadvertising.org');
insert into orders (_id, first_name, last_name, gender, city, email) values (2, 'Millisent', 'Sutter', 'Female', 'Linqu', 'msutter1@cnbc.com');
-- insert into orders (_id, first_name, last_name, gender, city, email) values (8, 'Jessamine', 'Randle', 'Female', 'Itabaiana', 'jrandle2@godaddy.com');
-- insert into orders (_id, first_name, last_name, gender, city, email) values (4, 'Urbanus', 'Byram', 'Male', 'Frashër', 'ubyram3@hc360.com');
-- insert into orders (_id, first_name, last_name, gender, city, email) values (5, 'Obadias', 'Hirjak', 'Male', 'Carumas', 'ohirjak4@linkedin.com');
-- insert into orders (_id, first_name, last_name, gender, city, email) values (6, 'Ignaz', 'Sleaford', 'Male', 'Nesterov', 'isleaford5@jalbum.net');
-- insert into orders (_id, first_name, last_name, gender, city, email) values (7, 'Far', 'Syseland', 'Male', 'Pancan', 'fsyseland6@webmd.com');
-- insert into orders (_id, first_name, last_name, gender, city, email) values (8, 'Allx', 'Van Brug', 'Female', 'Alvalade', 'avanbrug7@about.me');
-- insert into orders (_id, first_name, last_name, gender, city, email) values (9, 'Teresita', 'Tincombe', 'Female', 'Paradahan', 'ttincombe8@google.nl');
-- insert into orders (_id, first_name, last_name, gender, city, email) values (10, 'Tally', 'Ketteman', 'Female', 'La Esperanza', 'tketteman9@networkadvertising.org');
