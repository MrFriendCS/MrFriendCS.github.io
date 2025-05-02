# Title: N5 SDD Poem Generator
# Date: 
# Author: 

import random

verbs = ["running", "jumping", "flying"]
nouns = ["car", "ship", "dog"]
adjectives = ["happy", "sad", "dull"]

verbNo = random.randint(0, len(verbs) - 1)
nounNo = random.randint(0, len(nouns) - 1)
adjNo = random.randint(0, len(adjectives) - 1)

verb = verbs[verbNo]
noun = nouns[nounNo]
adjective = adjectives[adjNo]

print("The waves are " + verb)
print("The " + noun + " sinks below the waves")
print("The " + adjective + " star shines")