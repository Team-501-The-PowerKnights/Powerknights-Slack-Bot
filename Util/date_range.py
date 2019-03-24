import datetime

def week_range():
    """
    Get the RFC 3339 timestamps for the start and end of the week
    :return: lst [start, end] (both strings)
    """
    d = datetime.datetime.today()
    current_weekday = d.weekday()
    start_and_end_dates = []
    days_till_end = 6 - current_weekday
    now = datetime.date(d.year, d.month, d.day).isoformat()
    now_formatted = datetime.date(d.year, d.month, d.day)
    end_time = now_formatted + datetime.timedelta(days=days_till_end)
    start_and_end_dates.append(str(now) + "Z")
    start_and_end_dates.append(str(end_time) + "Z")
    return start_and_end_dates

print(week_range())