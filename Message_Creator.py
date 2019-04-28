import utility_functions as UF

"""
Week day key
"""

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
    starter_string = \
    """
    @everyone
    *What days wil you be coming to this week? Please react with the corresponding emoji:*
    Link to calendar = PUT LINK HERE
    """
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
    if events < 35:
        seperator = "---------------------------------------------"
        events_str = [starter_string]
        number_of_events = 0
        for event in events:
            number_of_events += 1
            event_name = event['summary']
            description = event['description']
            location = event['location']
            start_time_raw = event['start']['datetime']
            end_time_raw = event['end']['datetime']
            if len(start_time_raw) < 25:
                all_day_event = True
                start_time = UF.fix_time(len(start_time_raw))
                end_time = UF.fix_time(len(end_time_raw))
                multiday = UF.multiday_checker_STRANGE(start_time_raw, end_time_raw)
                if multiday:
                    emoji = emojis.pop(0)
                    used_emojis.append(emoji)
                    strings = [
                    seperator,
                    "_*{name}*_ = {sign}".format(name=event_name,sign=emoji),
                    description,
                    "{start} - {end}".format(start=start_time,end=end_time)
                    seperator
                    ]
                    with open("message.txt") as message_file:
                        for line in strings:
                            message_file.write(line,"\n")
                else:
                    day_of_week =
                    emoji = emojis.pop(0)
                    used_emojis.append(emoji)
                    strings = [
                    seperator,
                    "_*{name}*_ = {sign}".format(name=event_name,sign=emoji),
                    description,
                    "{start} - {end}".format(start=start_time,end=end_time)
                    seperator
                    ]
                    with open("message.txt") as message_file:
                        for line in strings:
                            message_file.write(line,"\n")
            else:
                start_time = UF.iso_format_to_regular(start_time_raw)
                end_time = UF.iso_format_to_regular(end_time_raw)
                multiday = UF.multiday_checker_ISO(start_time_raw, end_time_raw)
                strings = [
                seperator,

                ]
        if get_info:
            return_information = []
            return_information.append(final_message)
            return_information.append(used_emojis)
            return return_information
        else:
            return final_message
    else:
        print("Error:")
        print("This bot currently doesn't support more than 35 events. Please put an issue on github that you would like this to be increased.")
