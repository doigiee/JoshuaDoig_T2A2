from flask import Blueprint
from init import db, bcrypt
from models.art import Art
from models.artist import Artist
from models.customer import Customer
from models.gallery import Gallery

#if wanting to drop tables
# drop table customers;
# drop table artworks;
# drop table artists;
# drop table gallerys;

db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
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

    customers = [
        Customer(
            name = 'Disnay Price',
            # password=bcrypt.generate_password_hash('Hello').decode('utf-8'),
            phone = '0436987456',
            address = '47 field Street, Brisbane',
            gallery = gallerys[1]
        ),
        Customer(
            name = 'Donna Monopoly',
            # password=bcrypt.generate_password_hash('Hello').decode('utf-8'),
            phone = '0411224455',
            address = '81 Ashfrank Street, Brisbane',
            gallery = gallerys[2]
        ),
        Customer(
            name = 'Shooter McGavin',
            # password=bcrypt.generate_password_hash('Hello').decode('utf-8'),
            phone = '0411445588',
            address = '13 Kings Drive, Brisbane',
            gallery = gallerys[1]
        ),
        Customer(
            name = 'Bails Onran',
            # password=bcrypt.generate_password_hash('Hello').decode('utf-8'),
            phone = '0477441111',
            address = '14 Kings Drive, Brisbane',
            gallery = gallerys[2]
        )
    ]
    db.session.add_all(customers)
    db.session.commit()

    artists = [
        Artist(
            name = 'John Smithers',
            # password=bcrypt.generate_password_hash('Hello').decode('utf-8'),
            address = '2 Coombayar Street, Adelaide',
            phone = '0411235558',
            gallery = gallerys[1]
        ),
        Artist(
            name = 'Sandra Bullocks',
            # password=bcrypt.generate_password_hash('Hello').decode('utf-8'),
            address = '43 Epistien Road, Cambera',
            phone = '0421555668',
            gallery = gallerys[2]
        ),
        Artist(
            name = 'Jimmy Barnes',
            # password=bcrypt.generate_password_hash('Hello').decode('utf-8'),
            address = '3 Laney Lane, Brisbane',
            phone = '0477889989',
            gallery = gallerys[1]
        ),
        Artist(
            name = 'Matthew Finley',
            # password=bcrypt.generate_password_hash('Hello').decode('utf-8'),
            address = '56 Gumbear Street, Lizbane',
            phone = '0465656567',
            gallery = gallerys[3]
        ),
        Artist(
            name = 'Chris Hemsrunt',
            # password=bcrypt.generate_password_hash('Hello').decode('utf-8'),
            address = '78 Crocodile Road, Brisbane',
            phone = '0412345679',
            gallery = gallerys[1]
        ),
        Artist(
            name = 'Sammy Tammy',
            # password=bcrypt.generate_password_hash('Hello').decode('utf-8'),
            address = '91 Nikey Cresent, Sydney',
            phone = '0455555556',
            gallery = gallerys[3]
        ),
        Artist(
            name = 'Jacob Googels',
            # password=bcrypt.generate_password_hash('Hello').decode('utf-8'),
            address = '41 Crikey Lane, Adelaide',
            phone = '0432546581',
            gallery = gallerys[1]
        )
    ]
    db.session.add_all(artists)
    db.session.commit()

    artworks = [
        Art(
            title = 'Apple & Rock',
            creator = 'John Smithers',
            dimensions = '1m x 1m',
            color_pallet = 'red, grey',
            kilograms = '10kg',
            price = '$150',
            medium = 'Oil on Canvas',
            created = '15/07/1999',
            description = 'A simple painting, done by a minor, which depicts a apple and a rock occupying an empty field',
            gallery = gallerys[1],
            artist = artists[1]
        ),
        Art(
            title = 'Essence of Life',
            creator = 'Sandra Bullocks',
            dimensions = '5m x 10m',
            color_pallet = 'blue, yellow, green, purple',
            kilograms = '20kg',
            price = '$4,555',
            medium = 'Oil on Canvas',
            created = '16/7/1988',
            description = 'A beautiful and lengthy piece which could adorn an open outdoor setting. The colors dance together to create a optical illusion',
            gallery = gallerys[2],
            artist = artists[2]
        ),
        Art(
            title = 'Karma in Spite',
            creator = 'Sandra Bullocks',
            dimensions = '1m x 1m',
            color_pallet = 'grey',
            kilograms = '30kg',
            price = '$2,500',
            medium = 'stone and rock',
            created = '15/06/1984',
            description = 'Stones places and stuck together to create a giant natural stone display, great in a central area either indoors or outside',
            gallery = gallerys[2],
            artist = artists[2]
        ),
        Art(
            title = 'Blue Skies',
            creator = 'Sandra Bullocks',
            dimensions = '5m x 2m',
            color_pallet = 'silver',
            kilograms = '25kg',
            price = '$1,250',
            medium = 'metal',
            created = '24/06/2020',
            description = 'a metal pipe for outdoors settings, paired with the natural blue sky to make an exhibit',
            gallery = gallerys[3],
            artist = artists[2]
        ),
        Art(
            title = 'Open Book',
            creator = 'Sandra Bullocks',
            dimensions = '1m x 1m',
            color_pallet = 'red, blue, green, white',
            kilograms = '10kg',
            price = '$500',
            medium = 'paper',
            created = '23/01/1999',
            description = 'Sandras personal collection of books becomes a masterpiece which draws viewers into the novels on display',
            gallery = gallerys[1],
            artist = artists[2]
        ),
        Art(
            title = 'Golden Guitar',
            creator = 'Jimmy Barnes',
            dimensions = '1m x 1m',
            color_pallet = 'gold',
            kilograms = '200kg',
            price = '$80,000',
            medium = 'gold',
            created = '29/01/2012',
            description = 'a pure gold guitar, our most valuable colection item',
            gallery = gallerys[1],
            artist = artists[3]
        ),
        Art(
            title = 'Heaven',
            creator = 'Jimmy Barnes',
            dimensions = '10m x 10m',
            color_pallet = 'blue, white',
            kilograms = '20kg',
            price = '$500',
            medium = 'wool',
            created = '05/05/2001',
            description = 'rug depicting a beautiful winter mountain surrounded by the cloudy skies',
            gallery = gallerys[3],
            artist = artists[3]
        ),
        Art(
            title = 'Ice Cream Machine',
            creator = 'Jimmy Barnes',
            dimensions = '2m x 2m',
            color_pallet = 'silver, white',
            kilograms = '40kg',
            price = '$500',
            medium = 'metal',
            created = '06/07/2013',
            description = 'an ice cream machine despensing political rhetoric',
            gallery = gallerys[2],
            artist = artists[3]
        ),
        Art(
            title = 'Mountains',
            creator = 'Matthew Finley',
            dimensions = '5m x 5m',
            color_pallet = 'blue, white, green',
            kilograms = '6kg',
            price = '$450',
            medium = 'oil on canvas',
            created = '20/08/2015',
            description = 'mountains and wildlife pictured together',
            gallery = gallerys[2],
            artist = artists[4]
        ),
        Art(
            title = 'Lost and Found',
            creator = 'Matthew Finley',
            dimensions = '1m x 1m',
            color_pallet = 'black',
            kilograms = '1kg',
            price = '$250',
            medium = 'paper and light',
            created = '25/06/2001',
            description = 'paper cut out paired with light source to create imagery on a wall in correct environment',
            gallery = gallerys[2],
            artist = artists[4]
        ),
        Art(
            title = 'Chapter of Me',
            creator = 'Chris Hemsrunt',
            dimensions = '2m x 2m',
            color_pallet = 'black',
            kilograms = '2kg',
            price = '$50',
            medium = 'paper',
            created = '16/04/2019',
            description = 'memoire of last words of famous figures of 1990 actors detailed on a single page',
            gallery = gallerys[1],
            artist = artists[5]
        ),
        Art(
            title = '1990',
            creator = 'Chris Hemsrunt',
            dimensions = '5m x 5m',
            color_pallet = 'black, white',
            kilograms = '4kg',
            price = '$49',
            medium = 'photograph',
            created = '15/08/1995',
            description = '1990 city cars, building, and stop lights take the main focus of this photo',
            gallery = gallerys[3],
            artist = artists[5]
        ),
        Art(
            title = 'WHY?',
            creator = 'Sammy Tammy',
            dimensions = '2m x 2m',
            color_pallet = 'white',
            kilograms = '80kg',
            price = '$999',
            medium = 'marble',
            created = '09/05/2003',
            description = 'a figure begging in agony for release and tears in her eyes, beautiful marksmanship',
            gallery = gallerys[1],
            artist = artists[6]
        ),
        Art(
            title = 'Donnatella',
            creator = 'Jacob Googels',
            dimensions = '2m x 2m',
            color_pallet = 'white',
            kilograms = '80kg',
            price = '$40,000',
            medium = 'marble',
            created = '18/07/2004',
            description = 'marble figure posing confidently',
            gallery = gallerys[1],
            artist = artists[7]
        ),
    ]
    db.session.add_all(artworks)
    db.session.commit()

    print('Tables seeded')