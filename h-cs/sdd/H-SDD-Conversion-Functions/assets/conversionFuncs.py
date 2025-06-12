def secToMinSec(seconds):
    if seconds < 0:
        mins = -1
        sec = -1
    else:
        mins = int(seconds / 60)
        sec = int(seconds % 60)
    return (mins, sec)


def minToHourMin(minutes):
    if minutes < 0:
        hour = -1
        mins = -1
    else:
        hour = int(minutes / 60)
        mins = int(minutes % 60)
    return (hour, mins)


def hourToDayHour(hours):
    if hours < 0:
        days = -1
        hour = -1
    else:
        days = int(hours / 24)
        hour = int(hours % 24)
    return (days, hour)


def mmToCMmm(milli):
    if milli < 0:
        cm = -1
        mm = -1
    else:
        cm = int(milli / 10)
        mm = int(milli % 10)
    return (cm, mm)


def cmToMcm(centi):
    if centi < 0:
        m = -1
        cm = -1
    else:
        m = int(centi / 100)
        cm = int(centi % 100)
    return (m, cm)


def mToKMm(metres):
    if metres < 0:
        km = -1
        m = -1
    else:
        km = int(metres / 1000)
        m = int(metres % 1000)
    return (km, m)


def inchesToFeetInches(inch):
    if inch < 0:
        feet = -1
        inches = -1
    else:
        feet = int(inch / 12)
        inches = int(inch % 12)
    return (feet, inches)


def feetToYardsFeet(feets):
    if feets < 0:
        yards = -1
        feet = -1
    else:
        yards = int(feets / 3)
        feet = int(feets % 3)
    return (yards, feet)
