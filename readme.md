# Phonetic matcher

similar sounding words

# Install

```bash
pip install phonetic_matcher
```

# Usage

```python
from phonetic_matcher import phonetic_bestmatch, phonetic_fuzzymatch
# match scores
score = phonetic_fuzzymatch("mycroft", "microsoft")  # 0.8368983957219251
score = phonetic_fuzzymatch("hey", "gay")  # 0.3076923076923077

# best match selection
query = "mycroft"
choices = ["microsoft", "minecraft", "mike roft",
           "mein kampf", "my raft"]
best, score = phonetic_bestmatch(query, choices) # mike roft 0.8823529411764706
```