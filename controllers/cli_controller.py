from flask import Blueprint
from init import db, bcrypt
#model imports
from models.art import Art
from models.artist import Artist
from models.customer import Customer
from models.gallery import Gallery
from models.user import User

db_commands = Blueprint('db', __name__)

#create all tables
@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

#drop all tables
@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

#seed all tables in database with data provided
@db_commands.cli.command('seed')

#seed function
def seed_db():
# gallery inserts into the database
    gallerys = [
        Gallery(
            name = 'Brightwaters',
            location = '131 Simple Road, Brisbane',
            phone = '041556691'
        ),
        Gallery( 
            name = 'Schulshetch',
            location = '45 Chambers Road, Sydney',
            phone = '0471717171'
        ),
        Gallery(    
            name = 'Artsalive',
            location = 'Goombar, Brisbane',
            phone = '0477889989'
        )
    ]
    db.session.add_all(gallerys)
    db.session.commit()
# customer inserts into the database
    customers = [
        Customer(
            name = 'Disnay Price',
            phone = '0436987456',
            address = '47 field Street, Brisbane',
            gallery_id = 1
        ),
        Customer(
            name = 'Donna Monopoly',
            phone = '0411224455',
            address = '81 Ashfrank Street, Brisbane',
            gallery_id = 2
        ),
        Customer(
            name = 'Shooter McGavin',
            phone = '0411445588',
            address = '13 Kings Drive, Brisbane',
            gallery_id = 1
        ),
        Customer(
            name = 'Bails Onran',
            phone = '0477441111',
            address = '14 Kings Drive, Brisbane',
            gallery_id = 2
        )
    ]
# add and commits to database
    db.session.add_all(customers)
    db.session.commit()
# artist inserts into the database
    artists = [
        Artist(
            name = 'John Smithers',
            location = '2 Coombayar Street, Adelaide',
            phone = '0411235558',
            gallery_id = 1
        ),
        Artist(
            name = 'Sandra Bullocks',
            location = '43 Epistien Road, Cambera',
            phone = '0421555668',
            gallery_id = 2
        ),
        Artist(
            name = 'Jimmy Barnes',
            location = '3 Laney Lane, Brisbane',
            phone = '0477889989',
            gallery_id = 1
        ),
        Artist(
            name = 'Matthew Finley',
            location = '56 Gumbear Street, Lizbane',
            phone = '0465656567',
            gallery_id = 3
        ),
        Artist(
            name = 'Chris Hemsrunt',
            location = '78 Crocodile Road, Brisbane',
            phone = '0412345679',
            gallery_id = 1
        ),
        Artist(
            name = 'Sammy Tammy',
            location = '91 Nikey Cresent, Sydney',
            phone = '0455555556',
            gallery_id = 3
        ),
        Artist(
            name = 'Jacob Googels',
            location = '41 Crikey Lane, Adelaide',
            phone = '0432546581',
            gallery_id = 1
        )
    ]
# add and commits to database
    db.session.add_all(artists)
    db.session.commit()
# artwork inserts into the database
    artworks = [
        Art(
            title = 'Apple & Rock',
            creator = 'John Smithers',
            dimensions = '1m x 1m',
            color_pallet = 'red, grey',
            kilograms = '10kg',
            price = '$150',
            medium = 'Oil on Canvas',
            created = '19990715',
            descriptions = 'A simple painting, done by a minor, which depicts a apple and a rock occupying an empty field',
            gallery_id = 1,
            artist_id = 1
        ),
        Art(
            title = 'Essence of Life',
            creator = 'Sandra Bullocks',
            dimensions = '5m x 10m',
            color_pallet = 'blue, yellow, green, purple',
            kilograms = '20kg',
            price = '$4,555',
            medium = 'Oil on Canvas',
            created = '19880716',
            descriptions = 'A beautiful and lengthy piece which could adorn an open outdoor setting. The colors dance together to create a optical illusion',
            gallery_id = 2,
            artist_id = 2
        ),
        Art(
            title = 'Karma in Spite',
            creator = 'Sandra Bullocks',
            dimensions = '1m x 1m',
            color_pallet = 'grey',
            kilograms = '30kg',
            price = '$2,500',
            medium = 'stone and rock',
            created = '19840615',
            descriptions = 'Stones places and stuck together to create a giant natural stone display, great in a central area either indoors or outside',
            gallery_id = 2,
            artist_id = 2
        ),
        Art(
            title = 'Blue Skies',
            creator = 'Sandra Bullocks',
            dimensions = '5m x 2m',
            color_pallet = 'silver',
            kilograms = '25kg',
            price = '$1,250',
            medium = 'metal',
            created = '20200624',
            descriptions = 'a metal pipe for outdoors settings, paired with the natural blue sky to make an exhibit',
            gallery_id = 3,
            artist_id = 2
        ),
        Art(
            title = 'Open Book',
            creator = 'Sandra Bullocks',
            dimensions = '1m x 1m',
            color_pallet = 'red, blue, green, white',
            kilograms = '10kg',
            price = '$500',
            medium = 'paper',
            created = '19990123',
            descriptions = 'Sandras personal collection of books becomes a masterpiece which draws viewers into the novels on display',
            gallery_id = 1,
            artist_id = 2
        ),
        Art(
            title = 'Golden Guitar',
            creator = 'Jimmy Barnes',
            dimensions = '1m x 1m',
            color_pallet = 'gold',
            kilograms = '200kg',
            price = '$80,000',
            medium = 'gold',
            created = '20120129',
            descriptions = 'a pure gold guitar, our most valuable colection item',
            gallery_id = 1,
            artist_id = 3
        ),
        Art(
            title = 'Heaven',
            creator = 'Jimmy Barnes',
            dimensions = '10m x 10m',
            color_pallet = 'blue, white',
            kilograms = '20kg',
            price = '$500',
            medium = 'wool',
            created = '20010505',
            descriptions = 'rug depicting a beautiful winter mountain surrounded by the cloudy skies',
            gallery_id = 3,
            artist_id = 3
        ),
        Art(
            title = 'Ice Cream Machine',
            creator = 'Jimmy Barnes',
            dimensions = '2m x 2m',
            color_pallet = 'silver, white',
            kilograms = '40kg',
            price = '$500',
            medium = 'metal',
            created = '20130706',
            descriptions = 'an ice cream machine despensing political rhetoric',
            gallery_id = 2,
            artist_id = 3
        ),
        Art(
            title = 'Mountains',
            creator = 'Matthew Finley',
            dimensions = '5m x 5m',
            color_pallet = 'blue, white, green',
            kilograms = '6kg',
            price = '$450',
            medium = 'oil on canvas',
            created = '20150820',
            descriptions = 'mountains and wildlife pictured together',
            gallery_id = 2,
            artist_id = 4
        ),
        Art(
            title = 'Lost and Found',
            creator = 'Matthew Finley',
            dimensions = '1m x 1m',
            color_pallet = 'black',
            kilograms = '1kg',
            price = '$250',
            medium = 'paper and light',
            created = '20010625',
            descriptions = 'paper cut out paired with light source to create imagery on a wall in correct environment',
            gallery_id = 2,
            artist_id = 4
        ),
        Art(
            title = 'Chapter of Me',
            creator = 'Chris Hemsrunt',
            dimensions = '2m x 2m',
            color_pallet = 'black',
            kilograms = '2kg',
            price = '$50',
            medium = 'paper',
            created = '20190416',
            descriptions = 'memoire of last words of famous figures of 1990 actors detailed on a single page',
            gallery_id = 1,
            artist_id = 5
        ),
        Art(
            title = '1990',
            creator = 'Chris Hemsrunt',
            dimensions = '5m x 5m',
            color_pallet = 'black, white',
            kilograms = '4kg',
            price = '$49',
            medium = 'photograph',
            created = '19950815',
            descriptions = '1990 city cars, building, and stop lights take the main focus of this photo',
            gallery_id = 3,
            artist_id = 5
        ),
        Art(
            title = 'WHY?',
            creator = 'Sammy Tammy',
            dimensions = '2m x 2m',
            color_pallet = 'white',
            kilograms = '80kg',
            price = '$999',
            medium = 'marble',
            created = '20030509',
            descriptions = 'a figure begging in agony for release and tears in her eyes, beautiful marksmanship',
            gallery_id = 1,
            artist_id = 6
        ),
        Art(
            title = 'Donnatella',
            creator = 'Jacob Googels',
            dimensions = '2m x 2m',
            color_pallet = 'white',
            kilograms = '80kg',
            price = '$40,000',
            medium = 'marble',
            created = '20040718',
            descriptions = 'marble figure posing confidently',
            gallery_id = 1,
            artist_id = 7
        )
    ]
# add and commits to database
    db.session.add_all(artworks)
    db.session.commit()

# adding users
    users = [
        User(
            email = "admin@super.com",
            name = "Bobby Brown",
            password = bcrypt.generate_password_hash("password123").decode("utf-8"),
            is_admin = True
        ),
        User(
            email = "JohnSmithersss@super.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8"),
            name = "John Smithers"
        ),
        User(
            email = "DisneyyPPrice28@super.com",
            password = bcrypt.generate_password_hash("Mickey").decode("utf-8"),
            name = "Disnay Price"
        ),
        User(
            email = "user3@super.com",
            password = bcrypt.generate_password_hash("778899").decode("utf-8"),
            name = "Random Man"
        )
    ]
#add and commits all users including one admin into database
    db.session.add_all(users)
    db.session.commit()
    print("Tables seeded")