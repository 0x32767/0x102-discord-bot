# The assets folder

The purpose of the `assets` folder is to contain large json file, these files can be accessed by the code through the json module.
The assets' folder also makes the code cleaner, because instead of having a file with a massive array of maybe 800 yo mama jokes:

```py
import random

yo_mama_jokes = ["...", "...", ...]

await ctx.response.send_message(random.choice(yo_mama_jokes))
```

Instead, the code would be much cleaner by accessing the file with the json library which would return a python object,
respective of the file content.

```py
import random
import json

with open("yo_mama_jokes.json", "r") as f:
    data: any = json.load(f)

await ctx.response.send_message(random.choice(data))
```

This would make the code much more organized and less intimidating.

> tip:
> If an array has more than 15 elements then put it in a json file in the `assets` folder.
