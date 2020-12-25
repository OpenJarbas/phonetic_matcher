import phonetic_matcher

# Match strategies powered by rapidfuzz
# https://github.com/maxbachmann/rapidfuzz

s = phonetic_matcher.fuzzy_match("hey mycroft", "hey microsoft",
                                 strategy=phonetic_matcher.MatchStrategy.RATIO)
print(s)  # 0.8751379985754986
s = phonetic_matcher.fuzzy_match("hey mycroft", "hey microsoft",
                                 strategy=phonetic_matcher.MatchStrategy.PARTIAL_RATIO)
print(s)  # 0.8418402777777777
s = phonetic_matcher.fuzzy_match("hey mycroft", "hey microsoft",
                                 strategy=phonetic_matcher.MatchStrategy.TOKEN_SORT_RATIO)
print(s)  # 0.8492120726495727
s = phonetic_matcher.fuzzy_match("hey mycroft", "hey microsoft",
                                 strategy=phonetic_matcher.MatchStrategy.TOKEN_SET_RATIO)
print(s)  # 0.9492120726495725
s = phonetic_matcher.fuzzy_match("hey mycroft", "hey microsoft",
                                 strategy=phonetic_matcher.MatchStrategy.PARTIAL_TOKEN_RATIO)
print(s)  # 0.9043402777777777
s = phonetic_matcher.fuzzy_match("hey mycroft", "hey microsoft",
                                 strategy=phonetic_matcher.MatchStrategy.PARTIAL_TOKEN_SET_RATIO)
print(s)  # 0.9043402777777777
s = phonetic_matcher.fuzzy_match("hey mycroft", "hey microsoft",
                                 strategy=phonetic_matcher.MatchStrategy.PARTIAL_TOKEN_SORT_RATIO)
print(s)  # 0.7679766414141413
s = phonetic_matcher.fuzzy_match("hey mycroft", "hey microsoft",
                                 strategy=phonetic_matcher.MatchStrategy.QUICK_LEV_RATIO)
print(s)  # 0.8751379985754986
