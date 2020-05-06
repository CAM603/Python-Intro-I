# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return f'Name: {self.name}, Lat: {self.lat}, Lon: {self.lon}'
    def __repr__(self):
        return f'Waypoint(name={self.name}, lat={self.lat}, lon={self.lon})'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return f'Name: {self.name}, Difficulty: {self.difficulty}, Size: {self.size}, Lat: {self.lat}, Lon: {self.lon}'
    def __repr__(self):
        return f'Geocache(Name={self.name}, Difficulty={self.difficulty}, Size={self.size}, Lat={self.lat}, Lon={self.lon})'
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint(41.70505, -121.51521, "Catacombs")
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)
print(waypoint.lat)
print(waypoint.lon)
print(waypoint.name)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(44.052137, -121.41556, "Newberry Views", 1.5, 2)
# Print it--also make this print more nicely
print(geocache)
print(geocache.lat)
print(geocache.lon)
print(geocache.name)
print(geocache.size)
print(geocache.difficulty)

class Planet:

    shape = 'round'

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system
    
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'
    
    @staticmethod
    def spin(speed = '2000 miles per hour'):
        return f'The planet spins and spins at {speed}'

hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
naboo = Planet('Naboo', 30000, 8, "Naboo System")

print(f'Name is {hoth.name}')
print(hoth.orbit())
print(f'Name is {naboo.name}')
print(naboo.orbit())
print(hoth.commons())
print(Planet.spin('a super fast speed'))