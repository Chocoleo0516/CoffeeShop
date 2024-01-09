class Barista:
    #Store the barista's name
    def __init__(self, name, specialty = None):
        self.name = name
        self.specialty = specialty

    def get_name(self):
        return self.name
    
    def get_specialty(self):
        return self.specialty

