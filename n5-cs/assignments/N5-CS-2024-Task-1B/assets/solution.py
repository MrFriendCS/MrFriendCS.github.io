# Title: N5 CS 2024 Part 1 Part B
# Date: 19 Jan 2024
# Author: Mr Friend

# import module
import random

# 1 initialise variables
total = 0
songCounter = 0
durationSession = 0
durationSong = 0
songs = []
counter = 0
foamMachine = 0

# 2 get valid training session duration

# 2.1 ask for duration of training session
durationSession = int(input("Duration of training session: "))

# 2.2 while duration of training session < 10 or > 30
while durationSession < 10 or durationSession > 30:

    # 2.3 display error message to enter valid number
    print("Error: Duration must be between 10 and 30 inclusive")

    # 2.4 ask user to re-enter duration of training session
    durationSession = int(input("Duration of training session: "))

# 2.5 end while loop


# 3 convert duration of training session to seconds

# 3.1 duration of training session = duration of training session * 60
durationSession = durationSession * 60


# 4 calculate total duration of songs

# 4.1 songCounter = 0
songCounter = 0

# 4.2 while total < duration of training session
while total < durationSession:

    # 4.3 get and store duration of next song in seconds
    durationSong = int(input("Song " + str(counter + 1) + ": "))
    songs = songs + [durationSong]

    # 4.4 total = total + duration of next song
    total = total + durationSong

    # 4.5 if total >= duration of training session
    if total >= durationSession:

        # 4.6 display message to inform user that they have entered enough songs
        print("Enough songs have now been entered.")

    # 4.7 end if

    # 4.8 add 1 to songCounter
    songCounter = songCounter + 1

# 4.9 end while loop


# 5 display training session summary

# 5.1  counter = 1
counter = 1


# 5.2  display message stating the number of songs played + songCounter
print("The number of songs played was " + str(songCounter) + ".")

# 5.3  foamMachine = random number between 1 and songCounter
foamMachine = random.randint(1, songCounter)

# 5.4  start fixed loop for each stored song duration
for index in range(len(songs)):

    # 5.5 display counter + “:” + duration of next song
    print(str(counter) + ": " + str(songs[index]))

    # 5.6 if foamMachine = counter
    if foamMachine == counter:

        # 5.7 display message to start foam machine
        print("Start foam machine")

    # 5.8 end if

    # 5.9 counter = counter + 1
    counter = counter + 1

# 5.10 end fixed loop


# 5.11 display total with message
print("The total length of the training session was " + str(total) + ".")
