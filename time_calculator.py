def time_to_minutes(time, start_meridiem = ""):
    t = time.split(":")
    hour = int(t[0])
    minutes = int(t[1])

    if start_meridiem == "PM":
        hour += 12
    
    return (hour * 60) + minutes

def get_meridiem(x):
    if x % 1440 == 0 or x % 1440 <= 720:
        return "AM"
    else:
        return "PM"

def get_day(day, days_later):
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    index = week.index(day.capitalize())
    return week[(index + days_later) % 7]

def minutes_to_time(minutes):
    time = ""
    military_hour = int(minutes / 60)
    converted_minutes = minutes - (military_hour * 60)

    if military_hour % 12 == 0:
        time += "12:"
    else:
        time += str(military_hour % 12) + ":"

    if converted_minutes < 10:
        time += "0"
  
    time += str(converted_minutes)
    return time

def add_time(start, duration, starting_day=""):
    start_minutes = time_to_minutes(start[:-2], start[-2:])
    duration_minutes = time_to_minutes(duration)
    end_minutes = start_minutes + duration_minutes

    minutes_prior_daychange = 1440 - start_minutes
    x = duration_minutes - minutes_prior_daychange

    meridiem = get_meridiem(x)
    end_time = minutes_to_time(end_minutes)
    days_to_add = int(end_minutes / 1440)

    result = end_time + " " + meridiem
    day_info = ""
    
    if starting_day != "":
        end_day = get_day(starting_day, days_to_add)
        day_info += ", " + str(end_day)

    if days_to_add == 1:
        day_info += " (next day)"
    elif days_to_add > 1:
        day_info += " (" + str(days_to_add) + " days later)"

    result += day_info

    return result
