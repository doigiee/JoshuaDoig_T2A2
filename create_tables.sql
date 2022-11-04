CREATE TABLE if not exists galleries (
id serial PRIMARY KEY,
name varchar(50) NOT NULL,
location text,
phone text NOT NULL
);

CREATE TABLE if not exists artists (
id serial PRIMARY KEY,
name varchar(100) NOT NULL,
location text,
phone text NOT NULL,
gallery_id integer,
foreign key (gallery_id) references galleries (id)
);

CREATE TABLE if not exists artworks(
id serial PRIMARY KEY,
title text,
creator varchar(150),
dimensions text,
color_pallet text,
kilograms varchar(50),
price varchar(100),
medium text,
created date,
descriptions text,
gallery_id integer,
foreign key (gallery_id) references galleries (id),
artist_id integer,
foreign key (artist_id) references artists (id)
);

CREATE TABLE if not exists customers (
id serial PRIMARY KEY,
name varchar(100) NOT NULL,
phone text NOT NULL,
address varchar(150) NOT NULL,
gallery_id integer,
foreign key (gallery_id) references galleries (id)
);


-- CREATE TABLE if not exists galleries (
-- id serial PRIMARY KEY,
-- name varchar(50) NOT NULL,
-- location text,
-- phone text NOT NULL
-- );

-- CREATE TABLE if not exists artists (
-- id serial PRIMARY KEY,
-- name varchar(100) NOT NULL,
-- location text,
-- phone text NOT NULL,
-- gallery_id serial NOT NULL,
-- foreign key (gallery_id) references galleries (id)
-- );

-- CREATE TABLE if not exists artworks(
-- id serial PRIMARY KEY,
-- title text,
-- creator varchar(150),
-- dimensions text,
-- color_pallet text,
-- kilograms varchar(50),
-- price varchar(100),
-- medium text,
-- created date,
-- descriptions text,
-- gallery_id serial NOT NULL,
-- foreign key (gallery_id) references galleries (id),
-- artist_id serial NOT NULL,
-- foreign key (artist_id) references artists (id)
-- );

-- CREATE TABLE if not exists customers (
-- id serial PRIMARY KEY,
-- name varchar(100) NOT NULL,
-- phone text NOT NULL,
-- address varchar(150) NOT NULL,
-- gallery_id serial NOT NULL,
-- foreign key (gallery_id) references galleries (id)
-- );