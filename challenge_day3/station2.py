import datetime

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




    
    

    

