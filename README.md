# T2A2 

[Github repo](https://github.com/doigiee/JoshuaDoig_T2A2)

https://github.com/doigiee/JoshuaDoig_T2A2

NOTE: was going to place all, 'source code for your entire project' in a /src folder, as per requirements, though it seemed to break the app for multiple reasons (possibly due to the .venv or maybe pychache folders being moved). Though these files wont be included in submission I'd rather not risk it and thus have submitted assignment as was developed.

1. Once cloning the repo, you will need to create your own virtual environment and own .env (sample provided -: Example of database_url and jwt_secret_key (if lost or confused)
(DATABASE_URL=postgresql+psycopg2://doigiee:ectjyrj76@127.0.0.1:5432/art_gallery)
(JWT_SECRET_KEY=art is good):-
- and install requirements.txt while in your .venv environment 
- python3 -m venv .venv
- source .venv/bin/activate
- pip install -r requirements.txt
2. create a user either admin (preferably) with privileges on the database.
3. now in psql, when signed in, create a database called ```art_gallery```.
4. While in your virtual environment, run the commands ```flask db create``` then ```flask db seed```. 
   Use```flask db drop``` if wanting to start over again.
   (```flask db create && flask db seed && flask db drop``` for shorthand).
   An alternative would be to, go into 'extra folder' and find the file 'create_tables.sql' to use to create the tables and 'inserts.sql' to insert the data into the tables.
5. Open postman using the route intende, ```flask run``` while in your .venv and send GET, POST, DELETE... requests, while on your intended  URI channel, to  see, create or delete 'gallerys', 'arts', 'artists' and 'customers' seeded database information (some need admin//dev sign-in credentials or a JWT security token).



## R1 Identification of the problem you are trying to solve by building this particular app

With this app I'm trying to create a user-friendly experience for viewing and purchasing Artworks by taking a Art Gallery and representing it in the virtual world. The problem I'm solving is the difficulty art lovers face when having to look for a specific artworks. This API app shortens the amount of time it would normally take for a client to narrow down and find the type of work they want and gives them the exact updated listing ranges of the location, size, material, name. Users will be able to easily login as base users and be granted the ability to search for this a ever expanding list of artworks and pieces. The end result will hopefully be a user finding the perfect piece for their collection.

Also when in PSQL though queries and aggregate functions, the admin can find specific and desired information such as: cheapest, most expensive, location filtering, total number of items in a table and so on.

This database also lets users login and see information on categories made and also allows them to create listings.


## R2 Why is it a problem that needs solving?
It's a necessary problem that needs solving as im sure recording information on clients, artists, artworks would be a lot of work. Additionally, having to delete an artwork or artist would become cluttered if in the form of paperwork. Having a database to represent clients and artists which can be easily manipulated and deleted makes the whole process more simple and more usable. Also im sure users will enjoy being able to see a long list of their potential artworks to purchase and through contacting the creator or art gallery, likewise im sure artists will enjoy the enhanced exposure of their works and galleries will enjoy the increase of sales and ease of contacting customers and artists. Through communication (mostly mobile), galleries and artists can use location data to send a order by truck or in the mail, once communications have resulted and a payment has been confirmed.


## R3 Why have you chosen this database system. What are the drawbacks compared to others?
I have chosen PostgresQL as its a relational database which makes it easier to catalogue and organise the logic of my app. It becomes easier to debug and visually see the app broken into separate components rather than a single file containing all the information. It also allows myself and other developers a quick and easy way to find specific portions of code and zone in on those specific sections. MVC also allows for scalability in an industrial setting so it is good for me to learn this popular style of writing an API. MVC has various other benefits though these are the main benefits to be highlighted.

Whens comparing PostgreSQL MVC to other API models like NoSQL there are some drawbacks which can be addressed which include: it being a very strict data language, tables in our database must have relations, we must follow a set of requirements of data inputs and same goes for Schemas, data entries cannot exceed column points/fields defined by the table. In addition, If I wanted to add a field to just one entry item in my table all tables are then required to have that field (empty or filled) in their rows.
Moreover, with other databases like NoSQL or MongoDB, which store their data as documents, there is no fixed Schema. Lastly, PostgreSQL has be debated as being slower to perform when compared to other databases, especially as the size of said database increases. Say for instance my entries becomes in the range of 1,000, or 100,000 it will be interesting to see just how much the database slows down.


## R4 Identify and discuss the key functionalities and benefits of an ORM
ORM or Object Relational Mapping helps create a developer friendly workflow with less and cleaner code, better connections, migrations, seedings and easier implementation of code. ORM's also gives us 'ready to go' CRUD functionalities, the ability to map classes to tables, session level caching, custom queries which are easy to execute ORM's also allow developers to enter data into objects of a relational database without having to know raw SQL commands and so on. All really useful topics to consider when constructing a database and API.


## R5 Document all endpoints for your API

| ROUTE              | RESULT                                       | METHOD       |
|--------------------|:--------------------------------------------:|-------------:|
| /users             | Shows all users                              |  GET         |
| /users/register    | Creates a user                               |  POST        |
| /users/login       | logs in a user when using proper credentials |  POST        |
| /arts              | Shows all artworks                           |  GET         |
| /arts/int          | Shows specified artwork                      |  GET         |
| /arts/create       | allows users to create and enter an artwork  |  POST        |
| /arts/delete/int   | allows a authorized user to delete a artwork |  POST        |
| /gallery           | allows user to see all galleries             |  GET         |
| /gallery/int       | allows user to see a specified gallery       |  GET         |
| /gallery/create    | allows admin to create a gallery             |  POST        |
| /gallery/delete    | allows admin to delete a gallery             |  DELETE      |
| /artists           | allows user to see all galleries             |  GET         |
| /artists/int       | allows user to see a specified artist        |  GET         |
| /artists/create    | allows user to create a artist               |  POST        |
| /artist/delete     | allows admin to delete a artist              |  DELETE      |
| /customer          | allows user to see all galleries             |  GET         |
| /customer/int      | allows user to see a specified customer      |  GET         |
| /customer/create   | allows user to create a customer             |  POST        |
| /customer/delete   | allows admin to delete a customer            |  DELETE      |
| /customer/delete   | allows admin to delete a customer            |  DELETE      |
| /customer/delete   | allows admin to delete a customer            |  DELETE      |
| /customer/delete   | allows admin to delete a customer            |  DELETE      |
| /customers/patch/2 | allows admin to delete a customer            |  PUT/PATCH   |
| /gallerys/patch/2  | allows admin to delete a customer            |  PUT/PATCH   |
| /artists/patch/2   | allows admin to delete a customer            |  PUT/PATCH   |
| /arts/patch/2      | allows admin to delete a customer            |  PUT/PATCH   |

And Authorize JWT function is used to allow only admin to create galleries, delete an artist, delete an artwork, delete a customer or create and delete a gallery.

(For majority of outcomes a JWT token is required, some being admin//_dev is required)

### Results:

### /users         
[
    {
        "id": 1,
        "name": "Bobby Brown",
        "email": "admin@super.com",
        "is_admin": "True"
    },
    {
        "id": 2,
        "name": "John Smithers",
        "email": "JohnSmithersss@super.com",
        "is_admin": "False"
    },
    {
        "id": 3,
        "name": "Disnay Price",
        "email": "DisneyyPPrice28@super.com",
        "is_admin": "False"
    },
    {
        "id": 4,
        "name": "Random Man",
        "email": "user3@super.com",
        "is_admin": "False"
    }
]


### /users/register      (password omitted on view)
{
    "id": 6,
    "name": "Saaaaa Aaaaa",
    "email": "adpoww@spam.com",
    "is_admin": "False"
}


### /users/login 
{
    "email": "adpoww@spam.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODIzODIzNSwianRpIjoiMjkxMjFjN2ItZGExOC00ODU2LThjMzMtNzcyY2Q0NGYxNDI3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjYiLCJuYmYiOjE2NjgyMzgyMzUsImV4cCI6MTY2ODMyNDYzNX0.-Y3KoF8614DunRjJbrzbmiAy881vhJnENkgXDEnCyeo",
    "is_admin": false
}

### /arts
[
    {
        "dimensions": "5m x 10m",
        "price": "$4,555",
        "artist_id": 2,
        "descriptions": "A beautiful and lengthy piece which could adorn an open outdoor setting. The colors dance together to create a optical illusion",
        "title": "Essence of Life",
        "color_pallet": "blue, yellow, green, purple",
        "kilograms": "20kg",
        "created": "1988-07-16",
        "creator": "Sandra Bullocks",
        "gallery_id": 2,
        "medium": "Oil on Canvas"
    },
        {
        "dimensions": "1m x 1m",
        "price": "$2,500",
        "artist_id": 2,
        "descriptions": "Stones places and stuck together to create a giant natural stone display, great in a central area either indoors or outside",
        "title": "Karma in Spite",
        "color_pallet": "grey",
        "kilograms": "30kg",
        "created": "1984-06-15",
        "creator": "Sandra Bullocks",
        "gallery_id": 2,
        "medium": "stone and rock"
    },

   ... etc ...
]

### /arts/int
{
    "dimensions": "1m x 1m",
    "price": "$500",
    "artist_id": 2,
    "descriptions": "Sandras personal collection of books becomes a masterpiece which draws viewers into the novels on display",
    "title": "Open Book",
    "color_pallet": "red, blue, green, white",
    "kilograms": "10kg",
    "created": "1999-01-23",
    "creator": "Sandra Bullocks",
    "gallery_id": null,
    "medium": "paper"
}

### /arts/create
{"kilograms": "aasa", "color_pallet": "aasaaaddsdf1341341", "title": "This is my cobra", "artist_id": 2, "creator":
"John Smithers", "medium": "aasaa1234@#$%^&*(123412341243", "dimensions": "aasaaa", "gallery_id": 1, "created":
"2022-11-12", "price": "aasaa", "descriptions": "Sss"}


### /arts/delete/2
{
    "message": "Artwork 'Essence of Life' was successfully deleted."
}

### /gallery
[
    {
        "id": 1,
        "name": "Brightwaters",
        "location": "131 Simple Road, Brisbane",
        "phone": "041556691"
    },
    {
        "id": 2,
        "name": "Schulshetch",
        "location": "45 Chambers Road, Sydney",
        "phone": "0471717171"
    },
    {
        "id": 3,
        "name": "Artsalive",
        "location": "Goombar, Brisbane",
        "phone": "0477889989"
    }
]

### /gallery/2
{
    "id": 1,
    "name": "Brightwaters",
    "location": "131 Simple Road, Brisbane",
    "phone": "041556691"
}

### /gallery/create
{"id": 4, "name": "Brightwaterssss", "location": "132 Simple Road, Brisbane", "phone": "041556692"}

### /gallery/delete
{
    "message": "Gallery '4' was successfully deleted."
}

### example of user trying to delete someting they arent authorized to delete
{
    "error": "401 Unauthorized: The server could not verify that you are authorized to access the URL requested. You either supplied the wrong credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required."
}

### /artists
[
    {
        "id": 1,
        "name": "John Smithers",
        "location": "2 Coombayar Street, Adelaide",
        "phone": "0411235558",
        "gallery_id": 1
    },
    {
        "id": 2,
        "name": "Sandra Bullocks",
        "location": "43 Epistien Road, Cambera",
        "phone": "0421555668",
        "gallery_id": 2
    },
    ... etc ...

### /artists/int
{
    "id": 1,
    "name": "John Smithers",
    "location": "2 Coombayar Street, Adelaide",
    "phone": "0411235558",
    "gallery_id": 1
}



### /artists/create 
{"id": 9, "name": "Bobby Brown", "location": "111 street, Brisbane", "phone": "0432344666", "gallery_id": 1}

### /artist/delete
{
    "message": "Artist '9' was successfully deleted."
}

OR

{
    "message": "Artist '4' was successfully deleted."
}

### /customers
[
    {
        "id": 1,
        "name": "Disnay Price",
        "phone": "0436987456",
        "address": "47 field Street, Brisbane"
    },
    {
        "id": 2,
        "name": "Donna Monopoly",
        "phone": "0411224455",
        "address": "81 Ashfrank Street, Brisbane"
    },
    ... etc ...


### /customers/1
{
    "id": 1,
    "name": "Disnay Price",
    "phone": "0436987456",
    "address": "47 field Street, Brisbane"
}

### /customers/create
{"id": 5, "name": "Hello", "phone": "0489356555", "address": "47 walllably way, Sydney", "gallery_id": 3}


### /customers/delete
{
    "message": "Customer '1' was successfully deleted."
}

### customers/patch/2
{
    "id": 2,
    "name": "Hell",
    "phone": "048935655",
    "address": "81 Ashfrank Street, Brisbane",
    "gallery_id": 3
}

### gallerys/patch/2
{
    "id": 2,
    "name": "Hell",
    "location": "43 sherbert",
    "phone": "048935655"
}

### artists/patch/2
{
    "id": 2,
    "name": "Hell",
    "location": "43 sherbert",
    "phone": "048935655",
    "gallery_id": 2
}

### arts/patch/2
{
    "descriptions": "A beautiful and lengthy piece which could adorn an open outdoor setting. The colors dance together to create a optical illusion",
    "kilograms": "20kg",
    "price": "$4,555",
    "dimensions": "43 x 43",
    "creator": "Sandra Bullocks",
    "created": "1988-07-16",
    "artist_id": 2,
    "title": "Hell",
    "medium": "wood",
    "gallery_id": 2,
    "color_pallet": "blue, yellow, green, purple"
}



## R6 An ERD for your app

![image](./docs/ERD%20image.jpg)

find in docs folder titled 'ERD image.jpg'

Created 4 tables Customers, Art Gallery, Artworks and Artists.
Each have a relation to at least one other table and all connect to gallery.
Customers, Artworks and Artists all have a zero-or-one relation to Art galleries.
Art Gallery has a zero-or-many relation to Customers, Artworks and Artists.
Artworks also have a one-and-only-one relation to Artists and finally Artists has a zero-or-many relation to Artworks as shown through the crows feet.
Then each table has their specified column entry data, as listed and shown in image and shown throughout models and controllers.
All tables were given a primary key (PK) and a foreign key (FK) when being represented in another table, as a way to show their relations/connections.

**Artwork entries** - PK id, title, creator, dimensions, color_pallet, kilograms, price, medium, created, descriptions, FK  galleries, FK artists.

**Artist entries** - PK id, name, location, phone, FK gallery.

**Customer entries** - PK id, name, phone, address, FK gallery.

**Gallery entries** - PK id, name, location, phone.


These Tables are all listed as Models which are connected to controllers and the controllers are used to make changes to my database and return a view to users.


## R7 Detail any third party services that your app will use

Main libraries and third party services used:

<u>Postman</u> - Used like a google chrome search engine to test routes and check CRUD functionality through GET, POST, DELETE requests.
  
<u>Flask</u> - lightweight WSGI web application framework in Python.

<u>Marshmallow</u> - is an ORM/ODM/framework-agnostic which was used to convert complex datatypes to and from native Python datatypes.

<u>Flask-Marshmallow</u>- added additional features to marshmallow.

<u>SQLAlchemy</u> - toolkit and ORM which used offer powers like SQL.

<u>Flask-SQLAlchemy</u> - added support for SQLAlchemy which simplified using SQLAlchemy + Flask.

<u>marshmallow-sqlalchemy</u> - serialization library.

<u>Werkzeug</u> - a WSGI web application library, which allowed me to see bugs and errors in very comprehensive and useful ways.

<u>pip-review</u> - was used to check update requirements, though decided not to update because last time I did, it broke my app, though it was still useful to check for newer installs which could have been implemented in requirements.txt.

<u>Bcrypt</u> - was used in the process of encryption in order to increase security.

<u>Jinja2</u> - templating engine.

<u>six</u> -  provided utility functions for smoothing over the differences between Python versions.

<u>click</u> - creating beautiful command line interfaces

<u>PyJWT</u> - Python library used to encode and decode JSON Web Tokens (JWT)


## R8 Describe your projects models in terms of the relationships they have with each other
The main relationship my models have with each other are the Foreign Key relationships which they share. They reference each other and can prevent database entries, which share foreign key ids, (parent/child relations) from being deleted.

From what i can deduce, my models use declarative mapping which required me to enter all parameters to be passed into it directly. It doesn’t use imperative mapping and the main collection styles I use are lists and sets. As the relationships I have for all tables are a one to many, the foreign key of the child has been referenced in the parent table as a set. I also use a backref instead of back_populates to make a circular relationship (Bidirectional), as it appears to establish the relationship both ways. For instance, through using this method, my child table (artworks) inherited and automatically established the parent attribute (table artists) with one-to-many semantics. It is really quite nice to be able to create a table name a dunder, in another table, and easily create a relationship.

By establishing this relationship it gave me the option to delete cascade table entries, also know as delete-orphan. In some cases I took advantage of this functionality, as in the case of galleries being deleted I set a cascade delete to remove all associated artists, customers and artworks (which represents a art gallery closing its doors and destroying all associated clients and pieces information, only admin can perform this task). In other cases, I set it up so that it simply leaves the ID of a associated entry blank as to not destroy the piece. This was achieved, in some cases, by having a Nullable Many-to-One relationship (Nullable= either True or False). I also did not implement One-to-One, Many-To-Many relationships between my models.

Side note, my values are mapped into variables which represent columns in my tables.
My marshmallow Schemas are very similar in design to my Table Classes, and mirror them, other than omitting a requirement for ID to be passed, as this is auto generated. They also use marshmallow.validate to required fields which must be entered with sufficient/correct data inputs.

## R9 Discuss the database relations to be implemented in your application
The relations which need to be implemented in my application are Many-to-One (m-1) in all cases. Or in the singular case of Artworks which has a Many-to-Only-One relationship to Atists, as we are assuming in this assignment that Artworks can only be created by one artist. Also, my tables will mostly share similar columns and have a similar number of rows, depending on number of entries, though I plan for Artworks to have the most db entries. Artists will have a Parent relationship to Artworks, which is the Child. Additionally my tables will contain columns and relate to each other through adopting a parent key (PK) and relating it to a child by inserting its PK into the child as a foreign key (FK) and will thus create Many-to-One relationships when entered into numerous table entries.

Thus, the relations which my app will need to create will be m-to-1 relationships (or 1-to-many if looking at it from the opposite direction, m-1 / 1-m). This also means that I plan my database to be a relational database.

## R10 Describe the way tasks are allocated and tracked in your project
Was considering using trello though as it wasn't required I instead felt more comfortable mainly using pen on paper to document timestamps and milestones. When a task was started, I wrote the task description in my book and once it was completed, I wrote an update with any notes or concerns which I had along with time spent on activities, recreation, personal matters and so on. Similar to a reflective journal.
If there were problems with a function, or in general, I wrote it down into a list, as to reflect on it at a later time and give myself a list of tasks I needed to get done in order of priority and logic. It also helped me get a grasp for how big a task might be or how long the task might take by comparing it to previous tasks done either earlier that day or the previous day(s).

**Example images provided below:**

![image](./docs/example_of_notes.jpg)
![image](./docs/example_of_notes_2.jpg)
![image](./docs/example_of_notes_3.jpg)
![image](./docs/example_of_notes_4.jpg)

Something else to mention here is that I also did a quick sketch on pen and paper for my ERD which helped me understand how my database would be constructed, sometimes creating diagrams on diagrams.net can become slower than a pen on paper method which is why found this useful. In other words, instead of being slowed down in the moment, (as I am not a pro at diagrams.net), I was instantly able to map out my ERD freely.