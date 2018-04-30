class Parent:
    def __init__(self, last_name, eye_color):
        print("Parent Constructor: ", last_name, " ", eye_color)
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name: ", self.last_name)
        print("Eye Color: ", self.eye_color)
