import phonetics
from phonetic_matcher.utils import match_one, fuzzy_match, MatchStrategy
from phoneme_guesser import get_phonemes


def metaphone_fuzzymatch(x, against, strategy=MatchStrategy.SIMPLE_RATIO):
    return fuzzy_match(phonetics.metaphone(x),
                       phonetics.metaphone(against), strategy)


def phoneme_fuzzymatch(x, against, lang="en",
                       strategy=MatchStrategy.SIMPLE_RATIO):
    ph1 = get_phonemes(x, lang=lang)
    ph2 = get_phonemes(against, lang=lang)
    return fuzzy_match(ph1, ph2, strategy)


def phonetic_fuzzymatch(x, against, lang="en",
                        strategy=MatchStrategy.SIMPLE_RATIO):
    s1 = metaphone_fuzzymatch(x, against, strategy)
    s2 = phoneme_fuzzymatch(x, against, lang, strategy)
    return (s1 + s2) / 2


def metaphone_bestmatch(query, choices, strategy=MatchStrategy.SIMPLE_RATIO):
    return match_one(query, choices, metaphone_fuzzymatch, strategy)


def phoneme_bestmatch(query, choices, lang="en",
                      strategy=MatchStrategy.SIMPLE_RATIO):
    def match(q, c, s):
        return phoneme_fuzzymatch(q, c, lang, s)

    return match_one(query, choices, match, strategy)


def phonetic_bestmatch(query, choices, lang="en",
                       strategy=MatchStrategy.SIMPLE_RATIO):
    def match(q, c, s):
        return phonetic_fuzzymatch(q, c, lang, s)

    return match_one(query, choices, match, strategy)
