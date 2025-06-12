def secToMinSec(seconds):
    if seconds < 0:
        mins = -1
        sec= -1
    else:
        mins = int(seconds/60)
        sec = seconds % 60
    return (mins, sec)

def minToHourMin(minutes):
    if seconds < 0:
        mins = -1
        sec= -1
    else:
        hour = int(minutes/60)
        mins = minutes % 60
    return (hour, mins)

def hourToDayHour(hours):
    if seconds < 0:
        mins = -1
        sec= -1
    else:
        day = int((hours)/24)
        hour = hours % 24
    return (days, hour)


    