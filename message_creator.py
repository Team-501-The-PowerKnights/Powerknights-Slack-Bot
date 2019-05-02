import utility_functions as UF

def create_message(events, get_info):
    """
    Creates the message that will be posted to slack based of the events from the google calendar
    :param events: from the google calendar
        :type: array
    :param get_info: boolean that will tell the function to return the used emojis and the message
        :type: boolean
    :return message
        :type: string
        :type: array (index 0=messsage and index 1=used_emojis) this is only used if get_info is True
    """
    seperator = "---------------------------------------------"
    starter_string_lst = [
    seperator,
    "*What days will you be coming to this week? Please react with the corresponding emoji:*",
    "Link to calendar: https://bit.ly/2RlxQCu\n"
    ]
    starter_string = "\n".join(starter_string_lst)
    emojis = [
    ":one:",":two:",":three:",
    ":four:",":five:",":six:",
    ":seven:",":eight:",":nine:",
    ":keycap_ten:",":100:",":capital_abcd:",
    ":abcd:",":1234:",":symbols:",
    ':a:', ':ab:', ':b:',
    ':cl:', ':cool:', ':free:',
    ':information_source:', ':id:', ':m:',
    ':new:', ':ng:', ':o2:',
    ':ok:', ':parking:', ':sos:',
    ':up:', ':vs:', ':koko:', ':sa:',
    ':u6708:',
    ]
    used_emojis = []
    if len(events) < 35:
        with open("message.txt", "w") as message_file:
            message_file.write(starter_string)
            message_file.write(seperator + "\n")
        events_str = [starter_string]
        for event in events:
            event_name = event['summary']
            try:
                description = event["description"]
            except KeyError:
                description = "No description"
            location = event['location']
            try:
                start_time_raw = event['start']['dateTime']
            except KeyError:
                start_time_raw = event['start']['date']
            try:
                end_time_raw = event['end']['dateTime']
            except KeyError:
                end_time_raw = event['end']['date']
            if len(start_time_raw) < 25:  # Checking if its an all day event
                all_day_event = True
                start_time = UF.fix_time(start_time_raw)
                end_time = UF.fix_time(end_time_raw)
                multiday = UF.multiday_checker_STRANGE(start_time_raw, end_time_raw)
                if multiday:
                    emoji = emojis.pop(0)
                    used_emojis.append(emoji)
                    strings = [
                    "_*{name}*_ = {sign}".format(name=event_name,sign=emoji),
                    description,
                    "{start} - {end}".format(start=start_time,end=end_time),
                    seperator
                    ]
                    with open("message.txt", "a") as message_file:
                        for line in strings:
                            message_file.write(line + "\n")
                else:
                    day_of_week = UF.STRANGE_string_weekday(start_time)
                    emoji = emojis.pop(0)
                    used_emojis.append(emoji)
                    strings = [
                    "_*{weekday}*_ = {sign}".format(weekday=day_of_week,sign=emoji),
                    event_name,
                    start_time,
                    seperator
                    ]
                    with open("message.txt", "a") as message_file:
                        for line in strings:
                            message_file.write(line + "\n")
            else:
                day_of_week = UF.ISO_string_weekday(start_time_raw)
                emoji = emojis.pop(0)
                used_emojis.append(emoji)
                start_time = UF.iso_format_to_regular(start_time_raw)
                end_time = UF.iso_format_to_regular(end_time_raw)
                strings = [
                "_*{weekday}*_ = {sign}".format(weekday=day_of_week,sign=emoji),
                event_name,
                "{start} - {end}".format(start=start_time,end=end_time),
                seperator
                ]
                with open("message.txt", "a") as message_file:
                    for line in strings:
                        message_file.write(line + "\n")
                    message_file.write("If you have any questions about polls any suggestions feel free to email me at matthewgleich@gmail.com or DM me at @Matthew Gleich",)
    else:
        print("Error:")
        print("This bot currently doesn't support more than 35 events in one week. Please put an issue on github that you would like this to be increased.")
    with open("message.txt") as message_file:
        final_message = message_file.read()
    with open("message.txt", "w") as message_file:
        message_file.write("")
    if get_info:
        return_information = []
        return_information.append(final_message)
        user_emojis_fix = []
        for emoji in used_emojis:
            fixed_emoji = emoji.strip(":")
            user_emojis_fix.append(fixed_emoji)
        return_information.append(user_emojis_fix)
        return return_information
    else:
        return final_message


# Testing:
# print(create_message(""))
