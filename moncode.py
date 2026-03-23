try:
    value = int("1000x")
except ValueError as err:
    print("Ce numero est invalide", err)
else:
    ("Converted without issues")
finally:
    print("Execution compiete")

