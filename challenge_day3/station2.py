import datetime
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

