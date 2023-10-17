db = int(input("Enter the noise level: "))
if db <= 40:
    print("Quite room")
elif db <= 70:
    print("Louder than a quiet room, quieter than an alarm clock")
elif db <= 106:
    print("Louder than an alarm clock, quieter than a gas lawnmower")
elif db <= 130:
    print("Louder than a gas lawnmower, quieter than a jackhammer")
else:
    print("Louder than a jackhammer")
