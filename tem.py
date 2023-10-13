import re
with open('index.html', 'rb') as file:
    context = {"user": "ali"}
    tags = []
    for key in context:
        print(f"${key}")
        data = re.findall(f"${key}", file.read().decode('utf-8'))
        print(data)
        tags.append(data)
