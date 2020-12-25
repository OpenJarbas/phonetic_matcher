import phonetics
from phonetic_matcher.string_matching import fuzzy_match, MatchStrategy, match_all


def metaphone_fuzzy_match(x, against, strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    return fuzzy_match(phonetics.metaphone(x), phonetics.metaphone(against), strategy)


def metaphone_best_match(query, choices, strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    return metaphone_match(query, choices, strategy)[0]


def metaphone_match(query, choices, strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    return match_all(query, choices, metaphone_fuzzy_match, strategy)
