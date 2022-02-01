#Vehicle del 1 

class Vehicle:

    def __init__(self, model=0, model_year=0, kilometer=0, pris=0):
        self.model = model 
        self.model_year = model_year 
        self.kilometer = kilometer
        self.pris = pris 
    
    def get_model(self):
        return self.model
    
    def get_modelyear(self):
        return self.model_year
    
    def get_kilometer(self):
        return self.kilometer
    
    def get_price(self):
        return self.pris
    
    def set_model(self, model):
        self.model = model 
    
    def set_model(self, model_year):
        self.modelyear = model_year
    
    def set_kilometer(self, kilometer):
        self.kilometer = kilometer
    
    def set_price(self, pris):
        self.pris = pris 
    
    def __str__(self):
        return (f'Vechile Type = {self.model}, Model Year = {self.model_year}, Kilometer = {self.kilometer}')


class Car(Vehicle):

    def __init__(self, model=0, model_year=0, kilometer=0, pris=0, doors=0):
        super().__init__(Vehicle)
        self.doors = doors 
        self.model = model 
        self.model_year = model_year 
        self.kilometer = kilometer
        self.pris = pris 
    
    def get_doors(self):
        return self.doors 
    
    def get_model(self):
        return self.model
    
    def get_modelyear(self):
        return self.model_year
    
    def get_kilometer(self):
        return self.kilometer
    
    def get_price(self):
        return self.pris 
    
    def set_model(self, model):
        self.model = model 
    
    def set_model_year(self, model_year):
        self.modelyear = model_year
    
    def set_kilometer(self, kilometer):
        self.kilometer = kilometer
    
    def set_price(self, pris):
        self.pris = pris
    
    def set_doors(self, doors):
        self.doors = doors 
    
    def __str__(self):
        return (f'Vechile Type = {self.model}, Model Year = {self.model_year}, Kilometer = {self.kilometer}, Doors = {self.doors}')


class Truck(Vehicle):

    def __init__(self, model, model_year, kilometer, pris, wheeldrive):
        super().__init__(Vehicle)
        self.wheeldrive = wheeldrive 
        self.model = model 
        self.model_year = model_year
        self.kilometer = kilometer
        self.pris = pris 

    def get_wheeldrive(self):
        return self.wheeldrive 
    
    def get_model(self):
        return self.model
    
    def get_modelyear(self):
        return self.model_year
    
    def get_kilometer(self):
        return self.kilometer
    
    def set_model(self, model):
        self.model = model 
    
    def set_modelyear(self, model_year):
        self.modelyear = model_year
    
    def set_kilometer(self, kilometer):
        self.kilometer = kilometer
    
    def set_wheeldrive(self, wheeldrive):
        self.wheeldrive = wheeldrive
    
    def __str__(self):
        return (f'Vechile Type = {self.model}, Model Year = {self.model_year}, Kilometer = {self.kilometer}, Wheeldrive = {self.wheeldrive}')
    

class SUV(Vehicle):

    def __init__(self, model, model_year, kilometer, pris, passangers):
        super().__init__(Vehicle)
        self.passangers = passangers 
        self.model = model 
        self.model_year = model_year
        self.kilometer = kilometer
        self.pris = pris 
    
    def get_passangers(self):
        return self.passangers
    
    def get_model(self):
        return self.model
    
    def get_modelyear(self):
        return self.model_year
    
    def get_kilometer(self):
        return self.kilometer
    
    def set_model(self, model):
        self.model = model 
    
    def set_modelyear(self, model_year):
        self.modelyear = model_year
    
    def set_kilometer(self, kilometer):
        self.kilometer = kilometer
    
    def set_passangers(self, passangers):
        self.passangers = passangers
    
    def __str__(self):
        return (f'Vechile Type = {self.model}, Model Year = {self.model_year}, Kilometer = {self.kilometer}, passangers = {self.passangers}')
    


    




