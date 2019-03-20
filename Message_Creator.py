from Google_Cal import event_info

events = event_info

<<<<<<< Updated upstream
print(events)

=======
events_lst = event_info  # Original list of events and dates.
print("Original list of events", events_lst)
event_dates_orig = events_lst[::2]  # In the format of "Year-Month-Day"
print("All of the events in the Year-Month-Day format", event_dates_orig)
event_dates = []  # In the format of "Day-Month-Year"
print("All of the events in the Date-Month-Year format", event_dates)
day_of_week = []  # List of strings
print("All of the days of the weeks", day_of_week)
event_names = events_lst[1::2]  # List of strings that are the name of each event
print("Description for all the events", event_names)

for date in event_dates_orig:
    date_parsed_str = date.split("-")
    date_parsed_int = []
    for string in date_parsed_str:
        characters = list(string)
        if len(characters) > 0:
            if characters[0] == "0":
                characters.pop(0)
                print("Characters line 26:", characters)
                if len(characters) < 2:
                    for c in characters:
                        print("Int checker", int(c))
                        date_parsed_int.append()
                else:
                    zero_rm = characters.join("")
                    print("Zero Rm", zero_rm)
                    date_parsed_int.append(int(zero_rm))
            else:
                date_parsed_int.append(int(string))
                print("Int to string", int(string))
    print("Dates =", date_parsed_int)
    day_num = datetime.date(date_parsed_int[0], date_parsed_int[1], date_parsed_int[2])
    print("Weekday finder numbers:", day_num)
    weekday = ""
    if day_num == 1:
        weekday += "Sunday"
    elif day_num == 2:
        weekday += "Monday"
    elif day_num == 3:
        weekday += "Tuesday"
    elif day_num == 4:
        weekday += "Wednesday"
    elif day_num == 5:
        weekday += "Thursday"
    elif day_num == 6:
        weekday += "Friday"
    elif day_num == 7:
        weekday += "Saturday"
    else:
        print("Error finding weekday")
    day_of_week.append(weekday)


for date in event_dates_orig:
    date_parsed = date.split("-")
    for i in range(len(date_parsed)):
        fixed = []
        fixed.append(date_parsed[i - 1])
        new_string = fixed.join("/")
        event_dates.append(new_string)

events_dict = dict(zip(event_names, zip(event_dates, day_of_week)))

print("Dictionary for all the events", events_dict)
strings = []

strings.append("@allteamgroup")
strings.append("*What days will you be coming to this week? Please react with the following:*")
strings.append("Link to Calendar:  https://bit.ly/2RlxQCu\n")

for name, event_info in events_dict:
    if "week" not in name.lower():
        line_1 = "---------------------------------------------"
        line_2 = "_*" + event_info[0] + "*_"
        line_3 = name
        line_4 = event_info[1]
        strings.append(line_1)
        strings.append(line_2)
        strings.append(line_3)
        strings.append(line_4)


strings.append("---------------------------------------------\n")
strings.append("If you have any questions about polls any suggestions feel free to email me at matthewgleich@gmail.com or DM me at @Matthew Gleich\n")

final_message = strings.join(" | ")

print(final_message)
# with open("message.txt", "a") as message_file:
#     message_file.write(final_message)
>>>>>>> Stashed changes
