import phonetics
from phonetic_matcher.utils import match_one, fuzzy_match
from phoneme_guesser import get_phonemes


def metaphone_fuzzymatch(x, against):
    return fuzzy_match(phonetics.metaphone(x),
                       phonetics.metaphone(against))


def phoneme_fuzzymatch(x, against, lang="en"):
    ph1 = get_phonemes(x, lang=lang)
    ph2 = get_phonemes(against, lang=lang)
    return fuzzy_match(ph1, ph2)


def phonetic_fuzzymatch(x, against, lang="en"):
    s1 = metaphone_fuzzymatch(x, against)
    s2 = phoneme_fuzzymatch(x, against, lang)
    return (s1 + s2) / 2


def metaphone_bestmatch(query, choices):
    return match_one(query, choices, metaphone_fuzzymatch)


def phoneme_bestmatch(query, choices, lang="en"):
    def match(q, c):
        return phoneme_fuzzymatch(q, c, lang)
    return match_one(query, choices, match)


def phonetic_bestmatch(query, choices, lang="en"):
    def match(q, c):
        return phonetic_fuzzymatch(q, c, lang)
    return match_one(query, choices, match)

