my_number = 142

for attempt in range(5):
    user_input = int(input("Enter a number: " ))
    if user_input == my_number:
        print("That's a valid number")
        break
    else:
        print("Not valid, try again")
else:
    print("5 failed attempts.GAME OVER")
        
