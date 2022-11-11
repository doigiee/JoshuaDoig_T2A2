# T2A2

1. Once cloning the repo, you will need to create your own virtual environment and own .env (sample provided) and install requirements.txt while in your .venv environment
- python3 -m venv .venv
- source .venv/bin/activate
- pip install -r requirements.txt
2. create a user either admin (preferably) with privileges on the database.
3. now in psql, when signed in, create a database called ```art_gallery```.
4. While in your virtual environment, run the commands ```flask db create``` then ```flask db seed```. 
   Use```flask db drop``` if wanting to start over again.
   An alternative would be to, go into 'extra folder' and find the file 'create_tables.sql' to use to create the tables and 'inserts.sql' to insert the data into the tables.
5. Open postman using the route intende, ```flask run``` while in your .venv and send GET, POST, DELETE... requests, while on your intended  URI channel, to  see, create or delete 'gallerys', 'arts', 'artists' and 'customers' seeded database information (some need admin sign-in and most need a JWT token to use).

## R1 Identification of the problem you are trying to solve by building this particular app

With this app I'm trying to create a user-friendly experience for viewing and purchasing Artworks by taking a Art Gallery and representing it in the virtual world. The problem I'm solving is the difficulty art lovers face when having to look for a specific artworks. This API app shortens the amount of time it would normally take for a client to narrow down and find the type of work they want and gives them the exact updated listing ranges of the location, size, material, name. Users will be able to easily login as base users and be granted the ability to search for this a ever expanding list of artworks and pieces. The end result will hopefully be a user finding the perfect piece for their collection.

Also when in PSQL though queries and aggregate functions, the admin can find specific and desired information such as: cheapest, most expensive, location filtering, total number of items in a table and so on.

This database also lets users login and see information on categories made and also allows them to create listings.


## R2 Why is it a problem that needs solving?
It's a necessary problem that needs solving as im sure recording information on clients, artists, artworks would be a lot of work. Additionally, having to delete an artwork or artist would become cluttered if in the form of paperwork. Having a database to represent clients and artists which can be easily manipulated and deleted makes the whole process more simple and more usable. Also im sure users will enjoy being able to see a long list of their potential artworks to purchase and through contacting the creator or art gallery, likewise im sure artists will enjoy the enhanced exposure of their works and galleries will enjoy the increase of sales and ease of contacting customers and artists. Through communication (mostly mobile), galleries and artists can use location data to send a order by truck or in the mail, once communications have resulted and a payment has been confirmed.


## R3 Why have you chosen this database system. What are the drawbacks compared to others?
I have chosen PostgresQL as its a relational database which makes it easier to catalogue and and organise the logic of my app. It becomes easier to debug and visually see the app broken into separate components rather than a single file containing all the information. It also allows myself and other developers a quick and easy way to find specific portions of code and zone in on those specific sections. MVC also allows for scalability in an industrial setting so it is good for me to learn this popular style of writing an API. MVC has various other benefits though these are the main benefits to be highlighted.

Whens comparing PostgreSQL MVC to other API models like NoSQL there are some drawbacks which can be addressed which include: it being a very strict data language, tables in our database must have relations, we must follow a set of requirements of data inputs and same goes for Schemas, data entries cannot exceed column points/fields defined by the table. In addition, If I wanted to add a field to just one entry item in my table all tables are then required to have that field (empty or filled) in their rows.
Moreover, with other databases like NoSQL or MongoDB, which store their data as documents, there is no fixed Schema. Lastly, PostgreSQL has be debated as being slower to perform when compared to other databases, especially as the size of said database increases.


## R4 Identify and discuss the key functionalities and benefits of an ORM
Creates a developer friendly workflow with less and cleaner code, great with connections, migrations, seeds, easier implementation of code. ORM's also gives us 'ready to go' CRUD functionalities, the ability to map classes to tables, session level caching, custom queries which are easy to execute and so on. All really useful functions to consider when choosing a database structure.


## R5 Document all endpoints for your API

(For majority of outcomes a JWT token is required)

| ENDPOINT         | OUTCOME                                      | HTTP      |
|------------------|:--------------------------------------------:|----------:|
| /users           | Shows all users                              |  GET      |
| /users/int       | Shows specified user                         |  GET      |
| /users/register  | Creates a user                               |  POST     |
| /users/login     | logs in a user when using proper credentials |  POST     |
| /arts            | Shows all artworks                           |  GET      |
| /arts/int        | Shows specified artwork                      |  GET      |
| /arts/create     | allows users to create and enter an artwork  |  POST     |
| /arts/delete/int | allows a authorized user to delete a artwork |  POST     |
| /gallery         | allows user to see all galleries             |  GET      |
| /gallery/int     | allows user to see a specified gallery       |  GET      |
| /gallery/create  | allows admin to create a gallery             |  POST     |
| /gallery/delete  | allows admin to delete a gallery             |  DELETE   |
| /artist          | allows user to see all galleries             |  GET      |
| /artist/int      | allows user to see a specified artist        |  GET      |
| /artist/create   | allows user to create a artist               |  POST     |
| /artist/delete   | allows admin to delete a artist              |  DELETE   |
| /customer        | allows user to see all galleries             |  GET      |
| /customer/int    | allows user to see a specified customer      |  GET      |
| /customer/create | allows user to create a customer             |  POST     |
| /customer/delete | allows admin to delete a customer            |  DELETE   |


## R6 An ERD for your app

![image](./docs/ERD%20image.jpg)

find in docs folder titled 'ERD image.jpg'

Created 4 tables Customers, Art Gallery, Artworks and Artists.
Each have a relation to at least one other table and all connect to gallery.
Customers, Artworks and Artists all have a zero-or-one relation to Art galleries.
Art Gallery has a zero-or-many relation to Customers, Artworks and Artists.
Artworks also have a one-and-only-one relation to Artists and finally Artists has a zero-or-many relation to Artworks as shown through the crows feet.
Then each table has their specified column entry data, as listed and shown in image and shown throughout models and controllers.
All tables were given a primary key (PK) and a foreign key (FK) when being represented in another table, as a way to show their relation/connection.

These Tables are all listed as Models which are connected to controllers and the controllers are used to make changes to my database and return a view to users.


## R7 Detail any third party services that your app will use
Main libraries and third party services used:
  
Flask - lightweight WSGI web application framework in Python.

Marshmallow - is an ORM/ODM/framework-agnostic which was used to convert complex datatypes to and from native Python datatypes.

Flask-Marshmallow- added additional features to marshmallow.

SQLAlchemy - toolkit and ORM which used offer powers like SQL.

Flask-SQLAlchemy - added support for SQLAlchemy which simplified using SQLAlchemy + Flask.

marshmallow-sqlalchemy - serialization library.

Werkzeug - a WSGI web application library, which allowed me to see bugs and errors in very comprehensive and useful ways.

Postman - Used like a google chrome search engine to test routes and check CRUD functionality through GET, POST, DELETE requests.

pip-review - was used to check update requirements, though decided not to update because last time I did, it broke my app, though it was still useful to check for newer installs which could have been implemented in requirements.txt.

Bcrypt - was used in the process of encryption in order to increase security.

Jinja2 - templating engine.

six -  provided utility functions for smoothing over the differences between Python versions.

click - creating beautiful command line interfaces

PyJWT - Python library used to encode and decode JSON Web Tokens (JWT)

... 


## R8 Describe your projects models in terms of the relationships they have with each other
The main relationship my models have with each other are the Foreign Key relationships which they share. They reference each other and prevent database entries, which share foreign key ids, (parent/child relations) from being deleted.


## R9 Discuss the database relations to be implemented in your application



## R10 Describe the way tasks are allocated and tracked in your project
Was considering using trello though as it wasn't required I instead felt more comfortable mainly using pen on paper to document timestamps and milestones. When a task was started, I wrote the task description in my book and once it was completed, I wrote an update with any notes or concerns which I had along with time spent on activities, recreation, personal matter and so on. Similar to a reflective journal.

Example images provided below:

![image](./docs/example_of_notes.jpg)
![image](./docs/example_of_notes_2.jpg)
