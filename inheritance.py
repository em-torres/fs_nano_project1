class Parent:
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

billy_cyrus = Parent("Cyrus", "blue")
miley_cyrus = Parent("Cyrus", "blue", 5)
