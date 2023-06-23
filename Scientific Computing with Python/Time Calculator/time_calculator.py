def add_time(start, duration, dayoftheweek=""):
    new_time = ""
    new_day = 0
    new_day_text = ""

    print("start time:", start, "duration", duration, dayoftheweek)

    txt = start.split(" ")
    old_time = txt[0].split(":")
    old_hour = int(old_time[0])
    old_minute = int(old_time[1])
    ampm = txt[1]
    if ampm == "PM":
        old_hour += 12
    print("old time:", old_hour, old_minute)

    txt = duration.split(":")
    dur_hour = int(txt[0])
    dur_minute = int(txt[1])
    print("duration: ", dur_hour, dur_minute)

    new_minute = old_minute + dur_minute
    new_hour = old_hour + dur_hour
    print("add time: ", new_hour, new_minute)

    if new_minute >= 60:
        new_hour += 1
        new_minute -= 60

    if new_hour >= 24:
        new_day = new_hour // 24
        if new_day == 1:
            new_day_text = "(next day)"
        elif new_day > 1:
            new_day_text = "(" + str(new_day) + " days later)"

        new_hour %= 24
        if new_hour == 0:
            new_hour = 12
            ampm = "AM"
        elif new_hour >= 12:
            new_hour -= 12
            ampm = "PM"
        else:
            ampm = "AM"

    elif ampm == "AM" and old_hour < 12:
        if new_hour == 12:
            ampm = "PM"
        elif new_hour > 12:
            new_hour -= 12
            ampm = "PM"
    elif ampm == "PM":
        new_hour -= 12

    if new_minute < 10:
        new_minute = "0" + str(new_minute)
    else:
        new_minute = str(new_minute)

    new_time = str(new_hour) + ":" + new_minute + " " + ampm
    if dayoftheweek:
        dayoftheweek = getDayOfTheWeek(dayoftheweek, new_day)
        new_time += ", " + dayoftheweek
    if new_day_text:
        new_time += " " + new_day_text
    # print("new time: ", new_hour, new_minute, ampm, dayoftheweek, new_day_text)
    return new_time


def getDayOfTheWeek(dayoftheweek, new_day):
    num_dow = 0
    dayoftheweek = dayoftheweek[0].upper() + dayoftheweek[1:].lower()

    if new_day < 1:
        return dayoftheweek
    if dayoftheweek == "Monday":
        num_dow = 1
    elif dayoftheweek == "Tuesday":
        num_dow = 2
    elif dayoftheweek == "Wednesday":
        num_dow = 3
    elif dayoftheweek == "Thursday":
        num_dow = 4
    elif dayoftheweek == "Friday":
        num_dow = 5
    elif dayoftheweek == "Saturday":
        num_dow = 6
    elif dayoftheweek == "Sunday":
        num_dow = 7

    num_dow += new_day
    num_dow %= 7
    if num_dow == 1:
        dayoftheweek = "Monday"
    elif num_dow == 2:
        dayoftheweek = "Tuesday"
    elif num_dow == 3:
        dayoftheweek = "Wednesday"
    elif num_dow == 4:
        dayoftheweek = "Thursday"
    elif num_dow == 5:
        dayoftheweek = "Friday"
    elif num_dow == 6:
        dayoftheweek = "Saturday"
    elif num_dow == 0:
        dayoftheweek = "Sunday"

    return dayoftheweek


print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:40 AM", "0:25"))
print(add_time("5:01 AM", "0:00"))

print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02", "tuesday"))