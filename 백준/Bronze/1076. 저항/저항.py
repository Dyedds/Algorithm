#1076
resistor_values = {
    "black": (0, 1),
    "brown": (1, 10),
    "red": (2, 100),
    "orange": (3, 1000),
    "yellow": (4, 10000),
    "green": (5, 100000),
    "blue": (6, 1000000),
    "violet": (7, 10000000),
    "grey": (8, 100000000),
    "white": (9, 1000000000)
}

color1 = input()
color2 = input()
color3 = input()

resistance_value = (resistor_values[color1][0] * 10 + resistor_values[color2][0]) * resistor_values[color3][1]

print(resistance_value)
