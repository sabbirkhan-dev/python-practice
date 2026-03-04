def d():
    animal = "Elephant"    # local variable
    def e():
        nonlocal animal
        animal = "giraffe"          # change animal name to giraffe
        print(f"Inside nested function {animal}")

    print(f"Before calling function {animal}")

    # nested function e() call
    e() 

    print(f"After nested function {animal}")

animal = "Camel"  # Global variable change
d()
print(f"Global Animal {animal}")


