from phonetic_matcher.phonemes import phoneme_fuzzy_match, phoneme_match, phoneme_best_match
from phonetic_matcher.metaphone import metaphone_fuzzy_match, metaphone_match, metaphone_best_match
from phonetic_matcher.string_matching import MatchStrategy, match_one as _m1, match_all as _ma


def fuzzy_match(x, against, lang="en", strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    s1 = metaphone_fuzzy_match(x, against, strategy)
    s2 = phoneme_fuzzy_match(x, against, lang, strategy)
    return (s1 + s2) / 2


def best_match(query, choices, lang="en", strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    def _match(q, c, s):
        return fuzzy_match(q, c, lang, s)
    return _m1(query, choices, _match, strategy)


def match(query, choices, lang="en", strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    def _match(q, c, s):
        return fuzzy_match(q, c, lang, s)
    return _ma(query, choices, _match, strategy)
