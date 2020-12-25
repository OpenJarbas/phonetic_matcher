import phonetics
from phonetic_matcher.string_matching import fuzzy_match, MatchStrategy, match_all


def metaphone_fuzzy_match(x, against, strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    return fuzzy_match(phonetics.metaphone(x), phonetics.metaphone(against), strategy)


def metaphone_best_match(query, choices, strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    return metaphone_match(query, choices, strategy)[0]


def metaphone_match(query, choices, strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    return match_all(query, choices, metaphone_fuzzy_match, strategy)


def dmetaphone_fuzzy_match(x, against, strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    d = phonetics.dmetaphone(x)
    d2 = phonetics.dmetaphone(against)
    score = 0
    t = 0
    for x in [d[0], d[1]]:
        if not x:
            continue
        for c in [d2[0], d2[1]]:
            if not c:
                continue
            score += fuzzy_match(x, c, strategy)
            t += 1
    if not t:
        return 0  # should never happen
    return score / t


def dmetaphone_best_match(query, choices, strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    return dmetaphone_match(query, choices, strategy)[0]


def dmetaphone_match(query, choices, strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    return match_all(query, choices, dmetaphone_fuzzy_match, strategy)
