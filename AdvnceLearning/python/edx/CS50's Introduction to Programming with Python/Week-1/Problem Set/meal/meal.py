def main():
    # Prompt the user for the time
    time = input("What time is it? ").strip()

    # Convert the input time to a float representing the hours
    hours = convert(time)

    # Determine the meal time and print the corresponding message
    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")

def convert(time):
    # Split the time into hours and minutes
    hours, minutes = time.split(":")
    # Convert hours and minutes to float and calculate the total hours
    return float(hours) + float(minutes) / 60

if __name__ == "__main__":
    main()
