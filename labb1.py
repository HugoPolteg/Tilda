import os
import math
pi = math.pi
G = 6.67e-11

class Planet:
    def __init__(self, name, distance, period):
        self.name = name
        self.distance = distance
        self.period = period
    def mass(self):
        distance = float(self.distance)*1e6
        period = float(self.period)
        mass = 4*(pi**2)*(distance**3) / ( (period**2) * G )
        return mass
    def getname(self):
        return self.name
    def __str__(self):
        return f'Planet: {self.name}, Massa: {self.mass()/5.977e24} i jordmassor'



def main():
    with open ('planeter.txt', 'r') as f:
        planeter_lines = f.readlines()
    planet_name = ""
    planets = []
    for line in planeter_lines:
        if any(char.isalpha() for char in line):
            planet_name = line.strip()
        elif '/' in line:
            line = line.split('/')
            distance = line[0].strip()
            period = line[1].strip()
            if planet_name != "" and planets == [] or planet_name != planets[-1].getname():
                planets.append(Planet(planet_name, distance, period))
    for planet in planets:
        print(planet)
main()

