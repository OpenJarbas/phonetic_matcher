from difflib import SequenceMatcher
from enum import IntEnum, auto
import logging

try:
    from rapidfuzz import fuzz
except ImportError:
    fuzz = None
    logging.warning("rapidfuzz is not installed, falling back to "
                    "SequenceMatcher for all match strategies")


class MatchStrategy(IntEnum):
    SIMPLE_RATIO = auto()
    RATIO = auto()
    PARTIAL_RATIO = auto()
    TOKEN_SORT_RATIO = auto()
    TOKEN_SET_RATIO = auto()
    PARTIAL_TOKEN_RATIO = auto()
    PARTIAL_TOKEN_SORT_RATIO = auto()
    PARTIAL_TOKEN_SET_RATIO = auto()
    QUICK_LEV_RATIO = auto()


def _validate_strategy(strategy):
    if fuzz is None:
        return MatchStrategy.SIMPLE_RATIO
    return strategy


def fuzzy_match(x, against, strategy=MatchStrategy.PARTIAL_TOKEN_RATIO):
    """Perform a 'fuzzy' comparison between two strings.
    Returns:
        float: match percentage -- 1.0 for perfect match,
               down to 0.0 for no match at all.
    """
    strategy = _validate_strategy(strategy)
    if strategy == MatchStrategy.RATIO:
        return fuzz.ratio(x, against) / 100
    elif strategy == MatchStrategy.PARTIAL_RATIO:
        return fuzz.partial_ratio(x, against) / 100
    elif strategy == MatchStrategy.TOKEN_SORT_RATIO:
        return fuzz.token_sort_ratio(x, against) / 100
    elif strategy == MatchStrategy.TOKEN_SET_RATIO:
        return fuzz.token_set_ratio(x, against) / 100
    elif strategy == MatchStrategy.PARTIAL_TOKEN_SORT_RATIO:
        return fuzz.partial_token_sort_ratio(x, against) / 100
    elif strategy == MatchStrategy.PARTIAL_TOKEN_SET_RATIO:
        return fuzz.partial_token_set_ratio(x, against) / 100
    elif strategy == MatchStrategy.PARTIAL_TOKEN_RATIO:
        return fuzz.partial_token_ratio(x, against) / 100
    elif strategy == MatchStrategy.QUICK_LEV_RATIO:
        return fuzz.quick_lev_ratio(x, against) / 100
    return SequenceMatcher(None, x, against).ratio()


def match_one(query, choices, match_func=None,
              strategy=MatchStrategy.PARTIAL_TOKEN_RATIO):
    """
        Find best match from a list or dictionary given an input

        Arguments:
            query:   string to test
            choices: list or dictionary of choices

        Returns: tuple with best match, score
    """
    strategy = _validate_strategy(strategy)
    match_func = match_func or fuzzy_match
    if isinstance(choices, dict):
        _choices = list(choices.keys())
    elif isinstance(choices, list):
        _choices = choices
    else:
        raise ValueError('a list or dict of choices must be provided')

    best = (_choices[0], match_func(query, _choices[0], strategy))
    for c in _choices[1:]:
        score = match_func(query, c, strategy)
        if score > best[1]:
            best = (c, score)

    if isinstance(choices, dict):
        return (choices[best[0]], best[1])
    else:
        return best
