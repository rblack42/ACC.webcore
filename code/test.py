import json

data = u"""{
  "nav": [
    {"name":"a",
     "link":"b"
    },
    {"name":"c",
     "link":"d"
    }
  ]
}"""

nav = json.loads(data)['nav']
print nav
