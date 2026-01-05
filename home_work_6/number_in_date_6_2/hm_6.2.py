

def number_date():
    input_seconds = int(input("Enter two digits: "))

    if not 0 <= input_seconds < 8640000:
        return "The number must be between 0 and 8640000."

    days, remainder = divmod(input_seconds, (60 * 60 * 24))
    hours, remainder = divmod(remainder, (60 * 60))
    minutes, seconds = divmod(remainder, 60)
    day_word = "днів"

    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and not 12 <= days % 100 <= 14:
        day_word = "дні"

    return f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

print(number_date())