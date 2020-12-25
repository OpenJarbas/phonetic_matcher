from phonetic_matcher.string_matching import fuzzy_match, MatchStrategy, match_all
from phoneme_guesser import get_phonemes


def phoneme_fuzzy_match(x, against, lang="en", strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    ph1 = get_phonemes(x, lang=lang)
    ph2 = get_phonemes(against, lang=lang)
    return fuzzy_match(ph1, ph2, strategy)


def phoneme_best_match(query, choices, lang="en", strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    return phoneme_match(query, choices, lang, strategy)[0]


def phoneme_match(query, choices, lang="en", strategy=MatchStrategy.PARTIAL_TOKEN_SORT_RATIO):
    def _match(q, c, s):
        return phoneme_fuzzy_match(q, c, lang, s)
    return match_all(query, choices, _match, strategy)

