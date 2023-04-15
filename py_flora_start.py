from services import FlowerCup
import os


os.system('cls' if os.name == 'nt' else 'clear')

my_flower_cup = FlowerCup("Ruza","", 50)
my_flower_cup.add_water()
my_flower_cup.add_additives("gnojivo-zxy")

print(my_flower_cup)