import datetime

def week_range():
    """
    Get the RFC 3339 timestamps for the start and end of the week
    :return: lst [start, end] (both ints)
    """
    d = datetime.datetime.today()
    current_weekday = d.weekday()
    start_and_end = []
    days_till_end = 6 - current_weekday
    now = datetime.datetime(d.year(), d.month(), d.day())
    start_time = now.isoformat()
    now_formatted = datetime.datetime.date(d.year(), d.month(), d.day())
    end_time = now_formatted + datetime.datetime.timedelta(days=days_till_end)
    start_and_end.append(start_time)
    start_and_end.append(end_time)
    return start_and_end
