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


if __name__ == "__main__":

    # match scores

    s = metaphone_fuzzymatch("mycroft", "microsoft")
    print(s)  # 0.9090
    s = phoneme_fuzzymatch("mycroft", "microsoft")
    print(s)  # 0.7647
    s = phonetic_fuzzymatch("mycroft", "microsoft")
    print(s)  # 0.8368983957219251

    s = metaphone_fuzzymatch("hey", "gay")
    print(s)  # 0.0
    s = phoneme_fuzzymatch("hey", "gay")
    print(s)  # 0.6153
    s = phonetic_fuzzymatch("hey", "gay")
    print(s)  # 0.3076923076923077

    # best match selection
    query = "mycroft"
    choices = ["microsoft", "minecraft", "mike roft",
               "mein kampf", "my raft"]
    best, score = phoneme_bestmatch(query, choices)

    # my raft 0.7857142857142857
    print(best, score)

    best, score = metaphone_bestmatch(query, choices)
    # mike roft 1.0
    print(best, score)

    best, score = phonetic_bestmatch(query, choices)
    # mike roft 0.8823529411764706
    print(best, score)
