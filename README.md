# T2A2

1. Once cloning the repo, you will need to create your own virtual environment and own .env (sample provided).
2. install requirements.txt while in your .venv environment
- python -m venv .venv
- source .venv/bin/activate
- pip install -r requirements.txt
3. create a user either admin (preferably) with priveleges on the database.
4. in psql when signed in create a database called art_gallery.
5. now in your virtual environment run the commands ```flask db create``` then ```flask db seed```.
Or if they don't work go into 'extra folder' and find the file 'create_tables.sql' to use to create the tables and 'inserts.sql' (making sure to first set the datestyle ```SET datestyle = dmy;``` to insert the data into the tables.
6.



## R1 Identification of the problem you are trying to solve by building this particular app

With this app I'm trying to create a user-friendly experience for viewing and purchasing Artworks by taking a Art Gallery and representing it in the virtual world. The problem I'm solving is the difficulty art lovers face when having to look for a specific artworks. This API app shortens the amount of time it would normally take for a client to narrow down and find the type of work they want and gives them the exact updated listing ranges of the location, size, material, name. Users will be able to easily login as base users and be granted the ability to search for this a ever expanding list of artworks and pieces through queries. The end result will hopefully be a happy user finding the perfect piece for their collection.


## R2 Why is it a problem that needs solving?
It's a necessary problem that needs solving as im sure recording clients, artist, artworks would be a lot of work. additionally having to delete an artwork or artist would become cluttered if in the form of paperwork. Having a database to represent clients and artists which can be easily manipulated and deleted makes the whole process more simple and more usable.


## R3 Why have you chosen this database system. What are the drawbacks compared to others?
I have chosen PostgresQL as its a relational database which makes it easier to catalogue and and organise the logic of my app. It becomes easier to debug and visual see the app broken into separate components rather than a single file containing all the information. It also allows myself and other developers a quick and easy way to find specific portions of code and zone in on those specific sections. MVC also allows for scalability in an industrial setting so it is good for me to learn this popular style of writing an API. MVC has various other benefits though these are the main benefits to be highlighted.

Whens comparing MVC to other API models like NoSQL there are some drawbacks which can be addressed which include: it being a very strict data language, tables in our database must have sort of relations, we must follow a set of requirements of data inputs and same goes for Schemas, data entries cannot exceed column points/fields defined by the table. In addition, If I wanted to add a field to just one entry item in my table all tables are then required to have that field (empty or filled) in their rows.
MOreover, with other databases like NoSQL or MongoDB, which store their data as documents, there is not fixed Schema. Lastly, PostgreSQL tends to perform slower than other databases, especially as the size of said database increases.


## R4 Identify and discuss the key functionalities and benefits of an ORM



## R5 Document all endpoints for your API



## R6 An ERD for your app

![imgage](../JoshuaDoig_T2A2/docs/ERD%20image.jpg)

find in docs folder titled 'ERD image.jpg'


## R7 Detail any third party services that your app will use
pip review was used
Bcrypt was implemented


## R8 Describe your projects models in terms of the relationships they have with each other



## R9 Discuss the database relations to be implemented in your application



## R10 Describe the way tasks are allocated and tracked in your project
