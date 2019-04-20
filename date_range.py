import datetime

def str_lst_num(string, seperator_key, int_bool):
    """
    Turns a string into a list of integers
    :param string that is going to be parsed
    :param what the paraser is gonna parse by
    :param boolean that will tell if the numbers want to be an int or a float
    :return lst
    """
    if int_bool:
        nums = []
        lst_strs = string.split(seperator_key)
        for string in lst_strs:
            integer_form = int(string)
            nums.append(integer_form)
        return nums
    else:
        nums = []
        lst_strs = string.split(seperator_key)
        for string in lst_strs:
            integer_form = float(string)
            nums.append(integer_form)
        return nums


def week_range():  # Currently working version (Missing start)
    """
    Get the RFC 3339 timestamps for the start and end of the week
    :return: lst
    """
    dates = []
    current_day = datetime.date.today()
    current_weekday = current_day.weekday()
    # Finding start of the week:
    start_delta = datetime.timedelta(days=current_weekday)
    start_date_str = str(current_day - start_delta)
    start_date_lst = str_lst_num(start_date_str, "-", True)
    start_date = datetime.datetime(start_date_lst[0], start_date_lst[1], start_date_lst[2]).isoformat()
    dates.append(start_date)
    # Finding end of the week:
    days_till_end = 6 - current_weekday
    end_delta = datetime.timedelta(days=days_till_end)
    end_date_str = str(current_day + end_delta)
    end_date_lst = str_lst_num(end_date_str, "-", True)
    end_date = datetime.datetime(end_date_lst[0], end_date_lst[1], end_date_lst[2]).isoformat()
    dates.append(end_date)
    return dates


# Testing:
print(week_range())
