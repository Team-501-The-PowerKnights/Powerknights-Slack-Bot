import datetime

def iso_extract_info(string):
    """
    Will get all of the info and return it as an array
    :param string: ISO formatted string that will be used for extraction
    :return: array [year, month, day, military_time_hour, hour, minutes, seconds] (do note that all are ints except for the minutes and seconds.)
    """
    elements = []
    characters = list(string)
    year_int = int("".join(characters[0:4]))
    month_int = int("".join(characters[5:7]))
    day_int = int("".join(characters[8:10]))
    military_time_hours_int = int("".join(characters[11:13]))
    minutes_int = "".join(characters[14:16])
    hours = 0
    if military_time_hours_int > 12:
        hours += military_time_hours_int - 12
    elements.append(year_int)
    elements.append(month_int)
    elements.append(day_int)
    elements.append(h)


def iso_format_to_regular(string):
    """
    Will take a string that is an iso formatted string and make it look readable
    :param string: the iso formatted string
    :return: str
    """
    characters = list(string)
    year_int = int("".join(characters[0:4]))
    month_int = int("".join(characters[5:7]))
    day_int = int("".join(characters[8:10]))
    military_time_hours_int = int("".join(characters[11:13]))
    minutes_int = "".join(characters[14:16])
    if military_time_hours_int > 12:
        hours = military_time_hours_int - 12
        final_string = "{month}/{day}/{year} {hour}:{minute}PM".format(month=month_int, day=day_int, year=year_int, hour=hours, minute=minutes_int)
        return final_string
    else:
        final_string = "{month}/{day}/{year} {hour}:{minute}AM".format(month=month_int, day=day_int, year=year_int, hour=military_time_hours_int, minute=minutes_int)
        return final_string


# Testing:
# print(iso_format_to_regular('2019-04-27T16:00:00-04:00'))


def multiday_checker_ISO(start_date, end_date):
    """
    Will check if an event is more than one day long
    :param start_date: ISO formatted start of event
    :param end_date: ISO formatted end of event
    :return: Boolean
    """
    start_characters = list(start_date)
    start_month_int = int("".join(characters[5:7]))
    start_day_int = int("".join(characters[8:10]))
    end_characters = list(start_date)
    end_month_int = int("".join(characters[5:7]))
    end_day_int = int("".join(characters[8:10]))
    if start_month_int != end_month_int or start_day_int != end_day_int:
        return False
    else:
        return True


def fix_time(strange_date):
    """
    Will rearrange the strange date that Google gives and repalce it with the normal string.
    :param strange_date: strange time that google gives when an event is marked as "all day"
    :return: str
    """
    items = strange_date.split("-")
    year_int = int(items[0])
    month_int = int(items[1])
    day_int = int(items[2])
    new_str = "{month}/{day}/{year}".format(month=month_int, day=day_int,year=year_int)
    return new_str


def multiday_checker_STRANGE(start_date, end_date):
    """
    Will check if an event is more than day long
    :param start_date: Strange Google formatted date of the start of the event
    :param end_date: Strange Google formatted date of the end of the event
    :return: Boolean
    """
    start_date_items = start_date.split("-")
    end_date_items = end_date.split("-")
    start_date_sum = 0
    end_date_sum = 0
    for string in start_date_items:
        number = int(string)
        start_date_sum += number
    for string in end_date_items:
        number = int(string)
        end_date_sum += number
    date_dif = start_date_sum - end_date_sum
    if date_dif > 2:
        return True
    else:
        return False


# Testing:
# print(multiday_checker_STRANGE('2019-04-21', '2019-04-22'))


def STRANGE_string_weekday(string):
    """
    Will take a string that is a date formatted in the Google format and find what day of the week it is
    :param string: Google formatted string for the date
    :return: string
    """
    items = string.split("-")
    year_int = int(items[0])
    month_int = int(items[1])
    day_int = int(items[2])
    datetime_instance = datetime.date(year_int,month_int,day_int)
    week_day_number = datetime_instance.weekday()
    if week_day_number == 0:
        return "Monday"
    elif week_day_number == 1:
        return "Tuesday"
    elif week_day_number == 2:
        return "Wendsday"
    elif week_day_number == 3:
        return "Thursday"
    elif week_day_number == 4:
        return "Friday"
    elif week_day_number == 5:
        return "Saturday"
    elif week_day_number == 6:
        return "Sunday"
    else:
        return "Error"


# Testing:
# print(STRANGE_string_weekday("2019-04-27"))


def ISO_string_weekday(string):
    """
    Will take a string that is a date formatted in the ISO format and find what day of the week it is
    :param string: ISO formatted string for the date
    :return: string
    """
    characters = list(string)
    year_int = int("".join(characters[0:4]))
    month_int = int("".join(characters[5:7]))
    day_int = int("".join(characters[8:10]))
    datetime_instance = datetime.date(year_int,month_int,day_int)
    week_day_number = datetime_instance.weekday()
    if week_day_number == 0:
        return "Monday"
    elif week_day_number == 1:
        return "Tuesday"
    elif week_day_number == 2:
        return "Wendsday"
    elif week_day_number == 3:
        return "Thursday"
    elif week_day_number == 4:
        return "Friday"
    elif week_day_number == 5:
        return "Saturday"
    elif week_day_number == 6:
        return "Sunday"
    else:
        return "Error"


# Testing:
# print(ISO_string_weekday('2019-06-28T16:00:00-04:00'))
