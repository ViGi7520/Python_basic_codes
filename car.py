command = ""
print("""
        start: To start the car 
        stop:  To stop the car
        quit:  To exit the car
        help:  For help
        """)
started = False
while True:
    command = input("Choose:-").lower()
    if command == "start":
        if started:
            print("Car already Started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car already Stopped")
        else:
            started = False
            print("Car Stopped...")
    elif command == "help":
        print("""
        start - To start the car 
        stop - To stop the car
        quit - To exit the car
        help - For help
        """)
    elif command == "quit":
        print("Exited out of the car")
        break

