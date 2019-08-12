# pacman.log-reader-organizer

## What ~~the fuk~~ is this?

Basically, this a python script that takes /var/log/pacman.log and filters the data to show installed, upgraded and removed packages in a json.

## [Organize.py](./Organize.py)

```python
# Command example
import Organize

file = open('/var/log/pacman.log', 'r').read()
jsonlist = Organize.log2json(file)

print(jsonlist)

```

```json
            "JSON output example"
{
    "installed": [
        {
            "Date": "YYY-MM-DD HH:MM",
            "Action": "installed / upgraded / removed",
            "Package": "name",
            "Version": "1.0"
        }
    ],
    "upgraded": [
        {
            "Date": "YYY-MM-DD HH:MM",
            "Action": "installed / upgraded / removed",
            "Package": "name",
            "Version": {
                "older": "1.0",
                "newer": "2.0"
            }
        }
    ],
    "removed": [
        {
            "Date": "YYY-MM-DD HH:MM",
            "Action": "installed / upgraded / removed",
            "Package": "name",
            "Version": "1.0"
        }
    ],
    "full": [ "All the above information in a list" ]
}
```

## [main.py](./main.py)

_(Work In Progress)_

---

`Credits: Google translator`
