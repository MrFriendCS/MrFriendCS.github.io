def secToMinSec(seconds):
    if seconds < 0:
        mins = -1
        sec = -1
    else:
        mins = int(int(seconds) / 60)
        sec = seconds % 60
    return (mins, sec)


def minToHourMin(minutes):
    if minutes < 0:
        hour = -1
        mins = -1
    else:
        hour = int(int(minutes) / 60)
        mins = minutes % 60
    return (hour, mins)


def hourToDayHour(hours):
    if hours < 0:
        days = -1
        hour = -1
    else:
        day = int(int(hours) / 24)
        hour = hours % 24
    return (days, hour)


def mmToCMmm(milli):
    if milli < 0:
        cm = -1
        mm = -1
    else:
        cm = int(int(milli) / 10)
        mm = milli % 10
    return (days, hour)


def cmToMcm(centi):
    if centi < 0:
        m = -1
        cm = -1
    else:
        m = int(int(centi) / 100)
        cm = centi % 100
    return (m, cm)


def mToKMm(metres):
    if metres < 0:
        km = -1
        m = -1
    else:
        km = int(int(metres) / 1000)
        m = metres % 1000
    return (km, m)


def inchesToFeetInches(inch):
    if inch < 0:
        feet = -1
        inches = -1
    else:
        feet = int(int(inch) / 12)
        inches = inch % 12
    return (feet, inches)


def feetToYardsInches(feets):
    if feets < 0:
        yards = -1
        feet = -1
    else:
        yards = int(int(feets) / 12)
        feet = feets % 12
    return (yards, feet)
