# Phonetic matcher

match strings based on how they sound

# Install

```bash
pip install phonetic_matcher
```

NOTE: rapidfuzz is optional but strongly recommended

```bash
pip install rapidfuzz
```

# Usage

```python
import phonetic_matcher

# match scores
score = phonetic_matcher.fuzzy_match("mycroft", "microsoft")  # 0.7571428571428571
score = phonetic_matcher.fuzzy_match("cat", "dog")  # 0.4999999999999999

# best match selection
query = "mycroft"
choices = ["microsoft", "minecraft", "mike roft", "mein kampf", "my raft"]
best, score = phonetic_matcher.best_match(query, choices)  # mike roft 0.9047095761381476

# all matches
matches = phonetic_matcher.match(query, choices)
# [('mike roft', 0.9047095761381476),
#  ('minecraft', 0.7416326530612245),
#  ('microsoft', 0.7387755102040816),
#  ('my raft', 0.7083333333333333),
#  ('mein kampf', 0.48752834467120176)]
```