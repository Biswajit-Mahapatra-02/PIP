import random

def spin_roulette():
    # Simulate a spin
    result = random.randint(0, 38)
    
    # Display the result
    if result == 0:
        print("The spin resulted in 0...")
        print("Pay 0")
    elif result == 37:
        print("The spin resulted in 00...")
        print("Pay 00")
    else:
        print(f"The spin resulted in {result}...")
        print(f"Pay {result}")
        
        if result == 1 or result == 3 or result in range(5, 11) or result in range(12, 19) or result in range(19, 29) or result in range(30, 37):
            print("Pay Red")
        else:
            print("Pay Black")
            
        if result % 2 == 0 and result != 0:
            print(f"Pay Even")
        elif result % 2 != 0:
            print(f"Pay Odd")
        
        if 1 <= result <= 18:
            print("Pay 1 to 18")
        else:
            print("Pay 19 to 36")

spin_roulette()
