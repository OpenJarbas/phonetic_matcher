import phonetic_matcher


# match scores

s = phonetic_matcher.metaphone_fuzzy_match("mycroft", "microsoft")
print(s)  # 0.8
s = phonetic_matcher.phoneme_fuzzy_match("mycroft", "microsoft")
print(s)  # 0.7142857142857143
s = phonetic_matcher.fuzzy_match("mycroft", "microsoft")
print(s)  # 0.7571428571428571

s = phonetic_matcher.metaphone_fuzzy_match("cat", "dog")
print(s)  # 0.6666666666666665
s = phonetic_matcher.phoneme_fuzzy_match("cat", "dog")
print(s)  # 0.33333333333333326
s = phonetic_matcher.fuzzy_match("cat", "dog")
print(s)  # 0.4999999999999999

# best match selection
query = "mycroft"
choices = ["microsoft", "minecraft", "mike roft", "mein kampf", "my raft"]

best, score = phonetic_matcher.phoneme_best_match(query, choices)
# mike roft 0.8277864992150706
print(best, score)

best, score = phonetic_matcher.metaphone_best_match(query, choices)
# mike roft 0.9816326530612245
print(best, score)

best, score = phonetic_matcher.best_match(query, choices)
# mike roft 0.9047095761381476
print(best, score)
