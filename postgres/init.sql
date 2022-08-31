create schema ecommernce;

-- create table ecommernce.orders (
-- 	id int primary key,
--     store_id int not null,
--     order_date varchar(255) not null,
--     channel varchar(25),
--     country varchar(25),
--     total float not null,
--     status varchar(25)
-- );

create table ecommernce.orders (
	_id int primary key,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	gender VARCHAR(50),
	city VARCHAR(50),
	email VARCHAR(50)
);

-- insert into ecommernce.orders (id, store_id, order_date, channel, country, total, status) values (1, 100, '2021-08-15', 'STORE', 'Hungary', 173.04, 'ACTIVE');


-- insert into ecommernce.orders (_id, first_name, last_name, gender, city, email) values (1, 'Lynea', 'Hritzko', 'Female', 'Umeå', 'lhritzko0@comcast.net');
-- insert into ecommernce.orders (_id, first_name, last_name, gender, city, email) values (2, 'Winny', 'Gallier', 'Female', 'Anan', 'wgallier1@homestead.com');
-- insert into ecommernce.orders (_id, first_name, last_name, gender, city, email) values (3, 'Sigvard', 'Ivanov', 'Male', 'Baiyinnuole', 'sivanov2@fc2.com');
-- insert into ecommernce.orders (_id, first_name, last_name, gender, city, email) values (4, 'Clemmie', 'Clyne', 'Male', 'Xincheng', 'cclyne3@discovery.com');
-- insert into ecommernce.orders (_id, first_name, last_name, gender, city, email) values (5, 'Jeromy', 'Murty', 'Male', 'Firovo', 'jmurty4@comsenz.com');
insert into ecommernce.orders (_id, first_name, last_name, gender, city, email) values (6, 'Charline', 'Vayro', 'Female', 'Thessalon', 'cvayro5@is.gd');
insert into ecommernce.orders (_id, first_name, last_name, gender, city, email) values (7, 'Tomasine', 'McCafferty', 'Female', 'Miyata', 'tmccafferty6@vinaora.com');
-- insert into ecommernce.orders (_id, first_name, last_name, gender, city, email) values (8, 'Aleta', 'Widdecombe', 'Female', 'Narpes', 'awiddecombe7@slate.com');
-- insert into ecommernce.orders (_id, first_name, last_name, gender, city, email) values (9, 'Anna-maria', 'Springle', 'Female', 'Jatibonico', 'aspringle8@youtu.be');
-- insert into ecommernce.orders (_id, first_name, last_name, gender, city, email) values (10, 'Arielle', 'Laycock', 'Female', 'Jocón', 'alaycock9@newyorker.com');

GRANT USAGE ON SCHEMA ecommernce TO postgres;

GRANT SELECT ON ALL TABLES IN SCHEMA ecommernce TO postgres;

ALTER DEFAULT PRIVILEGES IN SCHEMA ecommernce GRANT SELECT ON TABLES TO postgres;


CREATE VIEW backup as SELECT * FROM ecommernce.orders;

GRANT SELECT ON TABLE backup to postgres;

CREATE PUBLICATION airbyte_slot FOR TABLE ecommernce.orders;

SELECT pg_create_logical_replication_slot('airbyte_slot', 'pgoutput');

CREATE PUBLICATION pub1 FOR ALL TABLES;
