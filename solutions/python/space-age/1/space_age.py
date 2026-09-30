'''
Given an age in seconds, calculate how old someone would be on a planet in our Solar System.
One Earth year equals 365.25 Earth days, or 31,557,600 seconds.
For the other planets, you have to account for their orbital period in Earth Years:

Planet	Orbital period in Earth Years
Mercury	0.2408467
Venus	0.61519726
Earth	1.0
Mars	1.8808158
Jupiter	11.862615
Saturn	29.447498
Uranus	84.016846
Neptune	164.79132
'''

class SpaceAge:
    
    EARTH_SECONDS = 31557600
    ORBITAL_PERIODS = {
        "earth": 1.0,
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }
    
    def __init__(self, seconds):
        self.seconds = seconds

    def _age_on(self, planet):
        '''Calculate age on different planets'''
        
        return round(
            self.seconds/
            (self.EARTH_SECONDS * self.ORBITAL_PERIODS[planet]),
            2)

    def on_earth(self):
        '''Return age on Earth'''
        
        return self._age_on("earth")

    def on_mercury(self):
        '''Return age on Mercury'''
        
        return self._age_on("mercury")

    def on_venus(self):
        '''Return age on Venus'''
        
        return self._age_on("venus")

    def on_mars(self):
        '''Return age on Mars'''
        
        return self._age_on("mars")

    def on_jupiter(self):
        '''Return age on Jupiter'''
        
        return self._age_on("jupiter")

    def on_saturn(self):
        '''Return age on Saturn'''
        
        return self._age_on("saturn")

    def on_uranus(self):
        '''Return age on Uranus'''
        
        return self._age_on("uranus")

    def on_neptune(self):
        '''Return age on Neptune'''
        
        return self._age_on("neptune")
    
