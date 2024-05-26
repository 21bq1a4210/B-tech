import re

def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date_str = input("Date: ").strip()

        # Try numeric format MM/DD/YYYY
        if match := re.match(r'^(\d{1,2})/(\d{1,2})/(\d{4})$', date_str):
            month, day, year = match.groups()
            if valid_date(int(month), int(day)):
                print(f"{year}-{int(month):02}-{int(day):02}")
                break

        # Try textual format Month DD, YYYY
        elif match := re.match(r'^([A-Za-z]+) (\d{1,2}), (\d{4})$', date_str):
            month_str, day, year = match.groups()
            if month_str in months:
                month = months.index(month_str) + 1
                if valid_date(month, int(day)):
                    print(f"{year}-{month:02}-{int(day):02}")
                    break

        # If neither format matched, re-prompt
        print("Invalid date. Please try again.")

def valid_date(month, day):
    return 1 <= month <= 12 and 1 <= day <= 31

if __name__ == "__main__":
    main()
