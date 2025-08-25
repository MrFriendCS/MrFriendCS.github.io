# Title: N5 SDD Summer Tasks Part 3
# Author: Mr Friend
# Date: 25 Aug 2025


# Get extra code
import random

# Initilise variables
determiner = ["A", "My", "The"]
adjective = ["blue", "big", "rainbow"]
noun = ["wind", "seagull", "dog"]
verb = ["slept", "ate", "ran"]
adverb = ["playfully", "slowly", "happily"]

ranDet = 0
ranAdj = 0
ranNou = 0
ranVer = 0
ranAdv = 0

# Pick random words
ranDet = random.randint(0, len(determiner)-1)
ranAdj = random.randint(0, len(adjective)-1)
ranNou = random.randint(0, len(noun)-1)
ranVer = random.randint(0, len(verb)-1)
ranAdv = random.randint(0, len(adverb)-1)

# Display a line of poetry
print(determiner[ranDet] + " " +
      adjective[ranAdj] + " " +
      noun[ranNou] + " " +
      verb[ranVer] + " " +
      adverb[ranAdv])
