import random

# lists containing all the options the user can choose from
destinations = ['Istanbul, Turkey', 'Machu Picchu, Peru', 'South Island, New Zealand', 'London, England', 'Tokyo, Japan']

restaurants_istanbul = ['Olive', 'Gulhane Sark Sofrasi', 'Bitlisli', 'Garden Mezze', 'Neolokal']
restaurants_machu_picchu = ['Chullpi', 'Tree House', 'Cala Tratoria', 'Apu Inti', 'Toto\'s House']
restaurants_south_island = ['Ortolana', 'The Sugar Club', 'The French Cafe', 'SidArt', 'Poderi Crisci']
restaurants_london = ['Kitchen Table', 'Bob Bob Richard Soho', 'Kiln', 'Padella', 'The Clove Club']
restaurants_tokyo = ['Narisawa', 'Ise Sueyoshi', 'Sushi Saito', 'Den', 'Hinokizaka']

transportation = ['train', 'bus', 'ship', 'plane', 'tram']

entertainment_istanbul = ['visit the Hagia Sophia', 'check out the Suleymaniye Mosque', 'tour the Topkapi Palace', 'visit the Dolmabahce Palace', 'admire the Beylerbeyi Palace']
entertainment_machu_picchu = ['see the Temple of the Sun', 'climb Huayna Picchu', 'climb up to the Sun Gate', 'visit the Temple of the Moon and the Great Cavern', 'find the Intihuatana']
entertainment_south_island = ['visit Queenstown, New Zealand', 'explore Milford Sound', 'walk the Kepler Track', 'explore Mount Cook National Park', 'hike Roy\'s Peak']
entertainment_london = ['go on the Harry Potter walking tour', 'tresure hunt in HiddenCity', 'visit the Tower of London', 'go on a Ghost Bus Tour', 'visit Borough Market']
entertainment_tokyo = ['rent a go-cart and drive around Tokyo', 'shop at Kappabashi', 'visit the Senso-Ji Buddhist Temple', 'go to The National Art Center', 'see sumo wrestling at Ryogoku Kokugikan Sumo Stadium']

# while loop to pick destination
user_input = ''

while user_input != 'y':
    user_destination = destinations[random.randint(0, 4)]
    user_input = input(f'We have selected {user_destination} for your destination. Does this sound good? Enter y/n: ')

# while loop to pick restaurant
user_input1 = ''

while user_input1 != 'y':
    if user_destination == 'Istanbul, Turkey':
        user_restaurant_istanbul = restaurants_istanbul[random.randint(0, 4)]
        user_input1 = input(f'We have selected {user_restaurant_istanbul} for your restaurant. Does this sound good? Enter y/n: ')
        print(user_restaurant_istanbul)
    elif user_destination == 'Machu Picchu, Peru':
        user_restaurant_machu_picchu = restaurants_machu_picchu[random.randint(0, 4)]
        user_input1 = input(f'We have selected {user_restaurant_machu_picchu} for your restaurant. Does this sound good? Enter y/n: ')
    elif user_destination == 'South Island, New Zealand':
        user_restaurant_south_island = restaurants_south_island[random.randint(0, 4)]
        user_input1 = input(f'We have selected {user_restaurant_south_island} for your restaurant. Does this sound good? Enter y/n: ')
    elif user_destination == 'London, England':
        user_restaurant_london = restaurants_london[random.randint(0, 4)]
        user_input1 = input(f'We have selected {user_restaurant_london} for your restaurant. Does this sound good? Enter y/n: ')
    elif user_destination == 'Tokyo, Japan':
        user_restaurant_tokyo = restaurants_tokyo[random.randint(0, 4)]
        user_input1 = input(f'We have selected {user_restaurant_tokyo} for your restaurant. Does this sound good? Enter y/n: ')
