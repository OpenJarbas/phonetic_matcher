from phonetic_matcher import *


# match scores

s = metaphone_fuzzymatch("mycroft", "microsoft")
print(s)  # 0.9090
s = phoneme_fuzzymatch("mycroft", "microsoft")
print(s)  # 0.7647
s = phonetic_fuzzymatch("mycroft", "microsoft")
print(s)  # 0.8368983957219251

s = metaphone_fuzzymatch("hey", "gay")
print(s)  # 0.0
s = phoneme_fuzzymatch("hey", "gay")
print(s)  # 0.6153
s = phonetic_fuzzymatch("hey", "gay")
print(s)  # 0.3076923076923077

# best match selection
query = "mycroft"
choices = ["microsoft", "minecraft", "mike roft",
           "mein kampf", "my raft"]
best, score = phoneme_bestmatch(query, choices)

# my raft 0.7857142857142857
print(best, score)

best, score = metaphone_bestmatch(query, choices)
# mike roft 1.0
print(best, score)

best, score = phonetic_bestmatch(query, choices)
# mike roft 0.8823529411764706
print(best, score)