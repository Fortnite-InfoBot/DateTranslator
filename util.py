from datetime import datetime

""" Function for Translate date (en -> it) """

def transform_date(day: str, month: str):
    """ 
    Parameters:
            day: the name of the date
            month: the name of the month
    """
    
    new_day = datetime.now().strftime(day) 
    new_month = datetime.now().strftime(month)
    
    if new_day == "Monday":
        day_it = "Lunedì"
    elif new_day == "Tuesday":
        day_it = "Martedì"
    elif new_day == "Wednesday":
        day_it = "Mercoledì"
    elif new_day == "Thursday":
        day_it = "Giovedì"
    elif new_day == "Friday":
        day_it = "Venerdì"
    elif new_day == "Saturday":
        day_it = "Sabato"
    elif new_day == "Sunday":
        day_it = "Domenica"
    else:
        day_it = "Unreconized day name"
    
    if new_month == "January":
        month_it = "Gennaio"
    elif new_month == "February":
        month_it = "Febbraio"
    elif new_month == "March":
        month_it = "Marzo"
    elif new_month == "April":
        month_it = "Aprile"
    elif new_month == "May":
        month_it = "Maggio"
    elif new_month == "June":
        month_it = "Giugno"
    elif new_month == "July":
        month_it = "Luglio"
    elif new_month == "August":
        month_it = "Agosto"
    elif new_month == "September":
        month_it = "Settembre"
    elif new_month == "October":
        month_it = "Ottobre"
    elif new_month == "November":
        month_it = "Novembre"
    elif new_month == "December":
        month_it = "Dicembre"
    else:
        month_it = "Unreconized month name"

    return day_it, month_it  # on success return the day and month translated (en -> it)
