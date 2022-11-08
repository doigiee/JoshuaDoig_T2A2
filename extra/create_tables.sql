drop table gallerys, artists, artworks, customers;

CREATE TABLE if not exists gallerys (
id serial PRIMARY KEY,
name text NOT NULL,
location text,
phone text NOT NULL
);

CREATE TABLE if not exists artists (
id serial PRIMARY KEY,
name text NOT NULL,
location text,
phone text NOT NULL,
gallery_id integer,
foreign key (gallery_id) references gallerys (id) on delete cascade
);

CREATE TABLE if not exists artworks(
id serial PRIMARY KEY,
title text,
creator text,
dimensions text,
color_pallet text,
kilograms text,
price text,
medium text,
created date,
descriptions text,
gallery_id integer,
foreign key (gallery_id) references gallerys (id) on delete cascade,
artist_id integer,
foreign key (artist_id) references artists (id) on delete cascade
);

CREATE TABLE if not exists customers (
id serial PRIMARY KEY,
name text NOT NULL,
phone text NOT NULL,
address text,
gallery_id integer,
foreign key (gallery_id) references gallerys (id) on delete cascade
);
