import datetime
<<<<<<< HEAD

def solution_station_2(date_str):
    # Parse the input date string into a datetime object
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d')

    # Define a list of Japanese kanji for days of the week
    days_of_week = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]

    # Get the day of the week as an integer (0 for Monday, 6 for Sunday)
    day_of_week_int = date.weekday()

    # Get the Japanese kanji for the corresponding day of the week
    kanji_day = days_of_week[day_of_week_int]
    
    return kanji_day


# Example usage:
date_str = "2023-06-12"
print(solution_station_2(date_str))

    
    

    
=======
import locale

def solution_station_2(date_str):
    # Set the locale to Japanese
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    
    # Parse the input date string
    input_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    
    # Format the date in Japanese without numeric values
    formatted_date = input_date.strftime('%Y年%m月%d日')
    
    # Create a mapping of numeric characters to empty strings
    numeric_to_empty = str.maketrans('0123456789', ' '*10)
    
    # Remove numeric values from the formatted date
    formatted_date = formatted_date.translate(numeric_to_empty)
    
    return formatted_date

# Test cases
date_str = "2023-03-16"
print(solution_station_2(date_str))  # Output: "年月日"
>>>>>>> 351f00fcef6b59dfc75608bfca376b7c42926435

