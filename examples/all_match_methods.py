import phonetic_matcher


# match scores

s = phonetic_matcher.metaphone_fuzzy_match("mycroft", "microsoft")
print(s)  # 0.776
s = phonetic_matcher.dmetaphone_fuzzy_match("mycroft", "microsoft")
print(s)  # 0.776
s = phonetic_matcher.phoneme_fuzzy_match("mycroft", "microsoft")
print(s)  # 0.7040816326530612
s = phonetic_matcher.fuzzy_match("mycroft", "microsoft")
print(s)  # 0.7400408163265306

s = phonetic_matcher.metaphone_fuzzy_match("cat", "dog")
print(s)  # 0.6666666666666665
s = phonetic_matcher.dmetaphone_fuzzy_match("cat", "dog")
print(s)  # 0.6666666666666665
s = phonetic_matcher.phoneme_fuzzy_match("cat", "dog")
print(s)  # 0.33333333333333326
s = phonetic_matcher.fuzzy_match("cat", "dog")
print(s)  # 0.4999999999999999

# best match selection
query = "mycroft"
choices = ["microsoft", "minecraft", "mike roft", "mein kampf", "my raft"]

best, score = phonetic_matcher.phoneme_best_match(query, choices)
# mike roft 0.8359497645211931
print(best, score)

best, score = phonetic_matcher.metaphone_best_match(query, choices)
# mike roft 1.0
print(best, score)

best, score = phonetic_matcher.dmetaphone_best_match(query, choices)
# mike roft 1.0
print(best, score)

best, score = phonetic_matcher.best_match(query, choices)
# mike roft 0.9179748822605965
print(best, score)
