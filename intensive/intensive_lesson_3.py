def check_input(input: str):
    try:
        number = float(input)
        print("Value: %s Correct." % input)
    except:
        print("Value: %s Wrong."% input)

inp = input("Введите целое или вещественное число:")
check_input(inp)

print("Test:")
check_input("5")
check_input("3.4")
check_input("3.4.1")
check_input("1a")
check_input("a3")
check_input("-123")
check_input("-5.321")


