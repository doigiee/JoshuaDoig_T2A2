-- art gallery inserts
insert into gallerys (name, location, phone) 
values 
    ('Brightwaters', '131 Simple Road, Brisbane', '0415566991'),
    ('Schulshetch', '45 Chambers Road, Sydney', '0471717171'),
    ('Artsalive', 'Goombar, Brisbane', '0477889989');

-- insert into galleries (name, location, phone) values (
--     ('Brightwaters Art', '131 Simple Road, Brisbane', '0415566991'),
--     ('Brakenrith Art', '45 Chambers Road, Sydney', '0471717171'), 
--     ('Aligance School of Art', 'Goombar, Brisbane', '0477889989')
-- );

-- customer inserts
insert into customers (name, phone, address, gallery_id) 
values 
    ('Disnay Price', '0436987456', '47 field Street, Brisbane', 1),
    ('Donna Monopoly', '0411224455', '81 Ashfrank Street, Brisbane', 2),
    ('Shooter McGavin', '0411445588', '13 Kings Drive, Brisbane', 1),
    ('Bails Onran', '0477441111', '14 Kings Drive, Brisbane', 2);

-- artists inserts
insert into artists (name, location, phone, gallery_id) 
values 
    ('John Smithers', '2 Coombayar Street, Adelaide', '0411235558', 1),
    ('Sandra Bullocks', '43 Epistien Road, Cambera', '0421555668', 2),
    ('Jimmy Barnes', '3 Laney Lane, Brisbane', '0477889989', 1),
    ('Matthew Finley', '56 Gumbear Street, Lizbane', '0465656567', 3),
    ('Chris Hemsrunt', '78 Crocodile Road, Brisbane', '0412345679', 1),
    ('Sammy Tammy', '91 Nikey Cresent, Sydney', '0455555556', 3),
    ('Jacob Googels', '41 Crikey Lane, Adelaide', '0432546581', 1);

-- artworks inserts
-- SET datestyle = dmy;         ->->->->(used to set the database to the correct datestyle)
insert into artworks (title, creator, dimensions, color_pallet, kilograms, price, medium, created, descriptions, gallery_id, artist_id) 
values
    ('Apple & Rock', 'John Smithers', '1m x 1m', 'red, grey', '10kg', '$150', 'Oil on Canvas', '15/07/1999', 'A simple painting, done by a minor, which depicts a apple and a rock occupying an empty field', 1, 1),
    ('Essence of Life', 'Sandra Bullocks', '5m x 10m', 'blue, yellow, green, purple', '20kg', '$4,555', 'Oil on Canvas', '16/7/1988', 'A beautiful and lengthy piece which could adorn an open outdoor setting. The colors dance together to create a optical illusion', 2, 2),
    ('Karma in Spite', 'Sandra Bullocks', '1m x 1m', 'grey', '30kg', '$2,500', 'stone and rock', '15/06/1984', 'Stones places and stuck together to create a giant natural stone display, great in a central area either indoors or outside', 2, 2),
    ('Blue Skies', 'Sandra Bullocks', '5m x 2m', 'silver', '25kg', '$1,250', 'metal', '24/06/2020', 'a metal pipe for outdoors settings, paired with the natural blue sky to make an exhibit', 3, 2),
    ('Open Book', 'Sandra Bullocks', '1m x 1m', 'red, blue, green, white', '10kg', '$500', 'paper', '23/01/1999', 'Sandras personal collection of books becomes a masterpiece which draws viewers into the novels on display', 1, 2),
    ('Golden Guitar', 'Jimmy Barnes', '1m x 1m', 'gold', '200kg', '$80,000', 'gold', '29/01/2012', 'a pure gold guitar, our most valuable colection item', 1, 3),
    ('Heaven', 'Jimmy Barnes', '10m x 10m', 'blue, white', '20kg', '$500', 'wool', '05/05/2001', 'rug depicting a beautiful winter mountain surrounded by the cloudy skies', 3, 3),
    ('Ice Cream Machine', 'Jimmy Barnes', '2m x 2m', 'silver, white', '40kg', '$500', 'metal', '06/07/2013', 'an ice cream machine despensing political rhetoric', 2, 3),
    ('Mountains', 'Matthew Finley', '5m x 5m', 'blue, white, green', '6kg', '$450', 'oil on canvas', '20/08/2015', 'mountains and wildlife pictured together', 2, 4),
    ('Lost and Found', 'Matthew Finley', '1m x 1m', 'black', '1kg', '$250', 'paper and light', '25/06/2001', 'paper cut out paired with light source to create imagery on a wall in correct environment', 2, 4),
    ('Chapter of Me', 'Chris Hemsrunt', '2m x 2m', 'black', '2kg', '$50', 'paper', '16/04/2019', 'memoire of last words of famous figures of 1990 actors detailed on a single page', 1, 5),
    ('1990', 'Chris Hemsrunt', '5m x 5m', 'black, white', '4kg', '$49', 'photograph', '15/08/1995', '1990 city cars, building, and stop lights take the main focus of this photo', 3, 5),
    ('WHY?', 'Sammy Tammy', '2m x 2m', 'white', '80kg', '$999', 'marble', '09/05/2003', 'a figure begging in agony for release and tears in her eyes, beautiful marksmanship', 1, 6),
    ('Donnatella', 'Jacob Googels', '2m x 2m', 'white', '80kg', '$40,000', 'marble', '18/07/2004', 'marble figure posing confidently', 1, 7);

-- ### alternative datestyle ### 
-- insert into artworks (title, creator, dimensions, color_pallet, kilograms, price, medium, created, descriptions) 
-- values
--     ('Apple & Rock', 'John Smithers', '1m x 1m', 'red, grey', '10kg', '$150', 'Oil on Canvas', '2020-08-16', 'A simple painting, done by a minor, which depicts a apple and a rock occupying an empty field'),
--     ('Essence of Life', 'Sandra Bullocks', '5m x 10m', 'blue, yellow, green, purple', '20kg', '$4,555', 'Oil on Canvas', '2009-01-15', 'A beautiful and lengthy piece which could adorn an open outdoor setting. The colors dance together to create a optical illusion'),
--     ('Karma in Spite', 'Sandra Bullocks', '1m x 1m', 'grey', '30kg', '$2,500', 'stone and rock', '2000-05-15', 'Stones places and stuck together to create a giant natural stone display, great in a central area either indoors or outside'),
--     ('Blue Skies', 'Sandra Bullocks', '5m x 2m', 'silver', '25kg', '$1,250', 'metal', '1999-01-15', 'a metal pipe for outdoors settings, paired with the natural blue sky to make an exhibit'),
--     ('Open Book', 'Sandra Bullocks', '1m x 1m', 'red, blue, green, white', '10kg', '$500', 'paper', '2022-05-12', 'Sandras personal collection of books becomes a masterpiece which draws viewers into the novels on display'),
--     ('Golden Guitar', 'Jimmy Barnes', '1m x 1m', 'gold', '200kg', '$80,000', 'gold', '2022-10-10', 'a pure gold guitar, our most valuable colection item'),
--     ('Heaven', 'Jimmy Barnes', '10m x 10m', 'blue, white', '20kg', '$500', 'wool', '2010-09-09', 'rug depicting a beautiful winter mountain surrounded by the cloudy skies'),
--     ('Ice Cream Machine', 'Jimmy Barnes', '2m x 2m', 'silver, white', '40kg', '$500', 'metal', '1989-11-11', 'an ice cream machine despensing political rhetoric'),
--     ('Mountains', 'Matthew Finley', '5m x 5m', 'blue, white, green', '6kg', '$450', 'oil on canvas', '1999-05-02', 'mountains and wildlife pictured together'),
--     ('Lost and Found', 'Matthew Finley', '1m x 1m', 'black', '1kg', '$250', 'paper and light', '2012-03-04', 'paper cut out paired with light source to create imagery on a wall in correct environment'),
--     ('Chapter of Me', 'Chris Hemsrunt', '2m x 2m', 'black', '2kg', '$50', 'paper', '2000-05-06', 'memoire of last words of famous figures of 1990 actors detailed on a single page'),
--     ('1990', 'Chris Hemsrunt', '5m x 5m', 'black, white', '4kg', '$49', 'photograph', '2001-18-01', '1990 city cars, building, and stop lights take the main focus of this photo'),
--     ('WHY?', 'Sammy Tammy', '2m x 2m', 'white', '80kg', '$999', 'marble', '2002-06-05', 'a figure begging in agony for release and tears in her eyes, beautiful marksmanship'),
--     ('Donnatella', 'Jacob Googels', '2m x 2m', 'white', '80kg', '$40,000', 'marble', '2003-07-08', 'marble figure posing confidently');

