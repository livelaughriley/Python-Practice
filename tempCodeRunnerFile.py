#
# practice.py
# flow control for: is raining
#


class Weather(object):
    def __init__(self, rain, umbrella):
        self.rain = rain
        self.umbrella = umbrella

    def is_raining(self, raining):
        if self.rain is True:
            return (self.rain.raining)

    def has_umbrella(self, have_umbrella):
        self.umbrella.have_umbrella = have_umbrella


myweather = Weather(rain=True, umbrella=False)

print(myweather.is_raining)

print(myweather.has_umbrella)