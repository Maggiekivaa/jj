from datetime import datetime, timedelta
import re

def start_app():
    print("Welcome user, what's your name?")
    name = input("Enter Name: ")
    print(f"Nice to know you, {name}!")

    hobby = input("Do you like reading books? (yes/no): ")

    if hobby.lower() == "yes":
        book = input("Enter a book you like: ")
        author = input("Who is the author of the book? ")

        print(f"Author of the book: {author}")

        action = input("Would you like to borrow or read the book? (borrow/read): ")
        
        if action.lower() == "borrow":
            borrow_date_str = input("When do you want to borrow the book? (e.g., today, tomorrow): ")
            borrow_date = datetime.today() if borrow_date_str == "today" else datetime.strptime(borrow_date_str, "%Y-%m-%d")

            return_date_str = input("When will you return the book? (e.g., in 1 week, in 2 days): ")

            return_date = parse_relative_date(return_date_str, borrow_date)

            days_borrowed = (return_date - borrow_date).days

            # Assume a borrowing fee of $22 per day
            borrowing_fee = days_borrowed * 22  # $22 per day

            print(f"Great! You've borrowed '{book}' by {author}.")
            print(f"You borrowed it on {borrow_date.strftime('%Y-%m-%d')} and plan to return it by {return_date.strftime('%Y-%m-%d')}.")
            print(f"Total borrowing fee: ${borrowing_fee} for {days_borrowed} day(s).")

            payment_method = input("How would you like to pay? (credit card, M-Pesa, cash): ").lower()
            if payment_method == "credit card":
                card_number = input("Please enter your credit card number: ")
                print(f"Processing payment of ${borrowing_fee} using credit card ending in {card_number[-4:]}")
                print("Payment successful!")
            elif payment_method == "m-pesa":
                phone_number = input("Please enter your M-Pesa phone number: ")
                print(f"Processing payment of ${borrowing_fee} using M-Pesa account linked to {phone_number}")
                print("Payment successful!")
            elif payment_method == "cash":
                print(f"Payment of ${borrowing_fee} accepted in cash.")
                print("Payment successful!")
            else:
                print("Invalid payment method. Please choose 'credit card', 'M-Pesa', or 'cash'.")
            
            print(f"Thank you! See you after {days_borrowed} days.")

        elif action.lower() == "read":
            print(f"Great! You would like to read '{book}' by {author}.")
            # Ask for table selection (tables 1 to 10)
            table_number = get_table_number()
            print(f"You have selected table {table_number} to read your book.")
            print("You may proceed to the table and enjoy your book!")
        
        else:
            print("Invalid input. Please choose either 'borrow' or 'read'.")
    else:
        print("oooops! Why are you even here, Goodbye.")

def get_table_number():
    """ Asks the user to select a table number between 1 and 10 """
    while True:
        try:
        
            table_number = int(input("Please choose a table from 1 to 10 to read: "))
            if 1 <= table_number <= 10:
                return table_number
            
            else:
                print("Invalid table number. Please choose a table between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")

def parse_relative_date(relative_date_str, start_date):
    """ Parses relative date strings like 'in 1 week', 'in 2 days', etc. """
    match = re.match(r'in (\d+) (\w+)', relative_date_str.strip().lower())
    if match:
        num = int(match.group(1))
        unit = match.group(2)

        

        if unit.startswith("week"):
            return start_date + timedelta(weeks=num)
        elif unit.startswith("day"):
            return start_date + timedelta(days=num)
        else:
            raise ValueError("Unsupported time unit. Use 'day' or 'week'.")
    else:
        raise ValueError("Invalid relative date format. Please use 'in X days' or 'in X weeks'.")

# Call the function to run the app
start_app()
