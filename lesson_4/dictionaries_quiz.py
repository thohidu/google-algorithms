"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

location = {'North America': {'USA': ['Mountain View']}}

location['Asia'] = {'India': ['Bangalore']}
location['North America']['USA'].append('Atlanta')
location['Africa'] = {'Egypt': ['Cairo']}
location['Asia']['China'] = ['Shanghai']

if __name__ == "__main__":
    location['North America']['USA'].sort()
    print(1)
    for idx, city in enumerate(location['North America']['USA']):
        #print(idx+1)
        print(city)
    
    print(2)
    city_asia = []
    country_asia = []
    for idx, country in enumerate(location['Asia'], 3):
        #print(idx)
        city_asia.append(location['Asia'][country][0])
        country_asia.append(country)
        #print(location['Asia'][country][0], country)
    if city_asia[0] < city_asia[1]:
        for i in range(len(city_asia)):
            print(city_asia[i], country_asia[i], sep='-')
    else:
        for i in range(len(city_aisa)-1, -1, -1):
            print(city_asia[i], country_asia[i], sep='-')

 

# location['Asia'] = {'India': ['Bangalore']}
# location['North America']['USA'].append('Atlanta')
# location['Africa'] = {'Egypt': ['Cairo']}
# location['Asia']['China'] = ['Shanghai']

# location['North America']['USA'].sort()
# print(1)
# for idx, city in enumerate(location['North America']['USA']):
#         #print(idx+1)
#     print(city)
    
# print(2)
# city_asia = []
# country_asia = []
# for idx, country in enumerate(location['Asia'], 3):
#     #print(idx)
#     city_asia.append(location['Asia'][country][0])
#     country_asia.append(country)
#     #print(location['Asia'][country][0], country)
# if city_asia[0] < city_asia[1]:
#     for i in range(len(city_asia)):
#         print(city_asia[i], country_asia[i], sep='-')
# else:
#     for i in range(len(city_aisa)-1, -1, -1):
#         print(city_asia[i], country_asia[i], sep='-')