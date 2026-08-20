#import another_module
#print(another_module_varible)

#import turtle 
#timmy = turtle.Turtle()

from turtle import Turtle , Screen
"""The Screen represents a window in which this turle is going to show up"""
timmy=Turtle()
print(timmy)
timmy.foward(100)
timmy.shape("turtle")
timmy.colour("blue")
my_screen=Screen()
print(my_screen.canvheight)

import prettytable  import Prettytable
table= Prettytable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Field Type", ["Electric", "Water", "Fire"])
table.align="l"
print(table)
