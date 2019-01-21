#!/usr/bin/env python3

kilometer = [39.2, 35.5, 37.3, 37.8]

# convertendo km em feet
feet = [float(3280.8399) * x for x in kilometer]
print(feet)

print()
# Utilizando uma função lambda
feet = map(lambda x: float(3280.8399) * x, kilometer)
print(list(feet))