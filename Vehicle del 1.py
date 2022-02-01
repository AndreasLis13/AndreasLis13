#Vehicle del 1 

class Vehicle:

    def __init__(self, model, model_year, kilometer):
        self.model = model 
        self.model_year = model_year 
        self.kilometer = kilometer
    
    def get_model(self):
        return self.model
    
    def get_modelyear(self):
        return self.model_year
    
    def get_kilometer(self):
        return self.kilometer
    
    def set_model(self, model):
        self.model = model 
    
    def set_model(self, model_year):
        self.modelyear = model_year
    
    def set_kilometer(self, kilometer):
        self.kilometer = kilometer
    
    def __str__(self):
        return f'Vechile Type={self.model}, Model Year = {self.model_year}, Kilometer = {self.kilometer}'


class Car(Vehicle):

    def __init__(self, doors):
        super().__init__(Vehicle)
        self.doors = doors 
    
    def get_doors(self):
        return self.doors 
    
    def set_doors(self, doors):
        self.doors = doors 
    
    def set_all(self, model, model_year, kilometer):
        self.model = model 
        self.model_year = model_year 
        self.kilometer = kilometer
    
    def __str__(self):
        return super().__str__(Vehicle)


