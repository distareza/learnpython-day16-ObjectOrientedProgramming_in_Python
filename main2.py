"""
following package need to installed
how to install in PyCharm :
    1. Open File > Settings
    2. Under "Project : <Project Name>" Path, Click "Python Interpreter" and click "+" to install
        search available python library ( https://pypi.org/ ) type "prettytable" and install

    https://pypi.org/project/prettytable/
"""
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])

print(table)

pokemon = PrettyTable()
pokemon.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
pokemon.add_column("Type",["Electric", "Water", "Fire"])

print(pokemon.align)
print(pokemon)

pokemon.align = "l"
print(pokemon)

pokemon.align["Type"] = "r"
print(pokemon)