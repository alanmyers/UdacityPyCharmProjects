import parent


class Child(parent.Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor: ", last_name, " ", eye_color, number_of_toys)
        parent.Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Number of Toys: ", self.number_of_toys)
