import phonetic_matcher

# match scores
score = phonetic_matcher.fuzzy_match("mycroft", "microsoft")  # 0.7400408163265306

score = phonetic_matcher.fuzzy_match("cat", "dog")  # 0.4999999999999999

# best match selection
query = "mycroft"
choices = ["microsoft", "minecraft", "mike roft", "mein kampf", "my raft"]
best, score = phonetic_matcher.best_match(query, choices)  # mike roft 0.9179748822605965

# all matches
matches = phonetic_matcher.match(query, choices)
# [('mike roft', 0.9047095761381476),
#  ('minecraft', 0.7416326530612245),
#  ('microsoft', 0.7387755102040816),
#  ('my raft', 0.7083333333333333),
#  ('mein kampf', 0.48752834467120176)]

query = "cat"
choices = ["fat", "crab", "bat", "crap", "trap", "sat"]
matches = phonetic_matcher.match(query, choices)
# [('fat', 0.6666666666666666),
#  ('bat', 0.6666666666666666),
#  ('sat', 0.6666666666666666),
#  ('crap', 0.6222222222222222),
#  ('crab', 0.5388888888888889),
#  ('trap', 0.5388888888888889)]
