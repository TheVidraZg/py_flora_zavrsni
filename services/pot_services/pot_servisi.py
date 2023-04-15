class FlowerCup:
    def __init__(self, flower_type, contents, water_level):
        self.flower_type = flower_type
        self.contents = contents
        self.water_level = water_level
        
    def add_water(self):
        if self.water_level < 100:
            self.water_level += 10
            print("Dodali ste vodu.  Trenutna razina vode je :", self.water_level)
        else:
            print("Vasa biljka ima dovoljno vode! .")
    
    def add_additives(self, additives):
        self.contents += additives
        print("Aditivi dodani . Trenutno vasa biljka ima ove aditive:", self.contents)

    def __str__(self):
     return f"Flower Cup: {self.flower_type}, Aditivi: {self.contents}, Razina vode: {self.water_level}"
