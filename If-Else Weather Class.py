#
# practice.py
# flow control for: is raining
#


class Weather:
    def __init__(self, rain, umbrella):
        self.rain = rain
        self.umbrella = umbrella

    def go_outside(self):
        if self.rain is False:
            print("It's not raining, I'm going outside.")
        else:
            print("It's raining, do I have my umbrella?")
            if self.umbrella is False:
                print("It's raining and I don't have my umbrella.")
            else:
                print("It's raining, and I do have my umbrella.")


w = Weather(rain=False, umbrella=True)
w.go_outside()