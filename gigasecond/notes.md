My initial solution:  

```Python
import time
from datetime import datetime, timedelta

def add(moment: datetime):
    return datetime.fromtimestamp(time.mktime(moment.utctimetuple()) + 10**9)
```

My ultimate solution:  

```Python
from datetime import datetime, timedelta

def add(moment: datetime):
    return moment + timedelta(seconds=10**9)
```

### Lessons  

• `datetime` => `time`  - use `timetuple` on datetime and then `time.mktime`  

• `time` => `datetime`  - use `datetime.fromtimestamp` on timestamp  

• however, the `datetime` module is generally more robust when working with both dates and time,
so it's worth using it exclusively  

• a supporting example here would be the fact that, if we used `moment.timetuple()` for converting  
the datetime into a `time`-module-friendly format, we'd see 3 test cases fail, due to Daylight Saving Time being ignored.  
Staying within the `datetime` module minimizes the risk of such accidental (and potentially devastating) errors.  
