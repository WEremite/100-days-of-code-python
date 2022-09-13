# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
#
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

# table = PrettyTable(["Pokemon Name", "Type"])
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Charmander", "Fire"])
# table.add_row(["Squirtle", "Water"])

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"

print(table)
