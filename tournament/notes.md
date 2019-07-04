Solution by Exercism user `yawpitch`:

```Python
"""
Exercism solution for "tournament"
"""
from operator import itemgetter
from typing import Counter, DefaultDict, List, Sequence

ROW_FORMAT = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
OUTCOME_MAP = {"win": "loss", "loss": "win", "draw": "draw"}


def tally(results: Sequence[str]) -> List[str]:
    """
    Tally a football tournament.
    """
    teams = DefaultDict(Counter)
    for result in results:
        home, away, outcome = result.split(";")
        teams[home][outcome] += 1
        teams[away][OUTCOME_MAP[outcome]] += 1

    records = []
    for team, record in sorted(teams.items()):
        wins, draws, losses = record["win"], record["draw"], record["loss"]
        matches, points = wins + draws + losses, 3 * wins + draws
        records.append((team, matches, wins, draws, losses, points))
    records.sort(key=itemgetter(-1), reverse=True)

    table = [("Team", "MP", "W", "D", "L", "P")] + records
    return [ROW_FORMAT.format(*row) for row in table]
```

I've attempted and failed to capture the symmetry of win-loss and went for a more  
descriptive solution. It's a useful trick to remember for the future:

```python
OUTCOME_MAP = {"win": "loss", "loss": "win", "draw": "draw"}
...
teams[home][outcome] += 1
teams[away][OUTCOME_MAP[outcome]] += 1
```

### Lessons:

**Strings**

• `str.ljust(width)` is the equivalent of `zfill` for padding string with spaces

• it's not possible to use f-strings as templates (`f'{} something {}'`) - this will throw an error.  
The alternative is to use `string.Template`, and then call `.substitute()` on it

• another, more elegant solution is the following:

```python
ROW_FORMAT = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
...
ROW_FORMAT.format(*row) for row in table
```

Also, note how a list can be unpacked into a formatted string with a `*`.

**Dictionaries**

• the `key` keyword argument of `sorted()` needs to be a function. This can be a lambda, e.g.:

```python
sorted(dictionaries.items(), key=lambda k: k[1]['pts'])  
```

for sorting a list of dictionaries by values in a nested dictionary.

**Reinventing the wheel**

• instead of handcrafting a DefaultDict for counting things with a lambda, you can pass a Counter to it:

```Python
teams = defaultdict(lambda: dict(pld=0, w=0, l=0, d=0, pts=0))`
# vs:
teams = DefaultDict(Counter)
```

It will work to the same nesting level as the lambda above:  
`teams["something"]["something"] += 1` will work.  
`teams["something"]["something"]["something"] += 1` will not.
