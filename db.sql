create table account (
	id serial primary key,
	name varchar(150) not null,
	email varchar(254) not null unique,
	password varchar(254) not null
);