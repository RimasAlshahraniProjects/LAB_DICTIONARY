phone_book_dictionary = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}

# Try to add a new value to the dictionary
phone_book_dictionary.update({"Rimas" : "0506038345"})

# User input
search_number = input("What number are you searching for? ")

def check_number(search_number):

    # Validation
    if len(search_number) != 10 or not search_number.isdigit():
        result = "Invalid number format"
        return result
    
    # Search
    for key, value in phone_book_dictionary.items():
        if value == search_number:
            result = f"The owner is: {key}"
            break

    return result


result = check_number(search_number)
print(f"The search result for the number {search_number} is:\n{result}")