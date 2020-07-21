


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Car:
    def __init__(self):
        self.pos = Point(0, 0)
        self.rides = []

class Ride:
    def __init__(self, sx, sy, ex, ey, start, finish):
        self.departure = Point(sx, sy)
        self.destination = Point(ex, ey)
        self.earliest_start = start
        self.latest_finish = finish

class App:
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.cars = 0
        self.rides = 0
        self.bonus = 0
        self.steps = 0

    def load(self, filename):
        with open("data/"+filename) as data_file:
            counter = 0
            for line in data_file:
                if counter == 0:
                    self.rows, self.columns, self.cars, self.rides, self.bonus, self.steps = map(int, line.split())
                counter = counter + 1

    def display(self):
        print("Rows:", self.rows, "Columns:", self.columns)
        print("Cars:", self.cars, "Rides:", self.rides)
        print("Bonus:", self.bonus, "Steps:", self.steps)


app = App()
app.load("a_example.in")
app.display()