from phonetic_matcher import *

# Match strategies powered by rapidfuzz

s = phonetic_fuzzymatch("hey mycroft", "hey microsoft", strategy=MatchStrategy.RATIO)
print(s)  # 0.8874643874643875
s = phonetic_fuzzymatch("hey mycroft", "hey microsoft", strategy=MatchStrategy.PARTIAL_RATIO)
print(s)  # 0.8541666666666666
s = phonetic_fuzzymatch("hey mycroft", "hey microsoft", strategy=MatchStrategy.TOKEN_SORT_RATIO)
print(s)  # 0.8615384615384616
s = phonetic_fuzzymatch("hey mycroft", "hey microsoft", strategy=MatchStrategy.TOKEN_SET_RATIO)
print(s)  # 0.9615384615384615
s = phonetic_fuzzymatch("hey mycroft", "hey microsoft", strategy=MatchStrategy.PARTIAL_TOKEN_RATIO)
print(s)  # 0.9166666666666666
s = phonetic_fuzzymatch("hey mycroft", "hey microsoft", strategy=MatchStrategy.PARTIAL_TOKEN_SET_RATIO)
print(s)  # 0.9166666666666666
s = phonetic_fuzzymatch("hey mycroft", "hey microsoft", strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO)
print(s)  # 0.7803030303030303
s = phonetic_fuzzymatch("hey mycroft", "hey microsoft",  strategy=MatchStrategy.QUICK_LEV_RATIO)
print(s)  # 0.8874643874643875
