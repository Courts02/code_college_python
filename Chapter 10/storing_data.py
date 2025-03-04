from pathlib import Path
import json

number = [1, 2, 3, 4, 5, 6]

json_path = Path("numbers.json")
content = json.dumps(number)

json_path.write_text(content)

content = json_path.read_text()
data = json.loads(content)

print(number)
