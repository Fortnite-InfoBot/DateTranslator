# Date Translator 

A repostory of [FortniteInfo Bot](https://t.me/FortniteDataBot) which contains an <b>English to Italian date converter.</b>

## Usage

<b>Sync Function</b>

``` python
from util import transform_date
from datetime import datetime

def my_function():
    day, month = transform_date('%A', '%B') # pass the arguments 
    current_date = "{} {} {}".format(day, datetime.now().strftime('%d'), month)
    print(current_date) # print the date

my_function() # run synchronously
```
<b>Async Function</b>

``` python
import asyncio

from util import transform_date
from datetime import datetime

async def my_function():
    day, month = transform_date('%A', '%B') # pass the arguments 
    current_date = "{} {} {}".format(day, datetime.now().strftime('%d'), month)
    print(current_date) # print the date

asyncio.run(my_function()) # run asynchronously
```

