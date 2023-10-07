# AtomixAPI

AtomixAPI is a lightweight micro framework for building web applications and RestFull API's in Python. It provides a simple and intuitive interface for defining routes and handling HTTP requests. Whether you're creating a small web service or experimenting with web development, AtomixAPI is designed to be quick and easy to use.

### Starter Template

```python
from atomixapi import AtomixAPI

app = AtomixAPI()

def home():
    return "Hello!"

app.get('/', home)

app.listen(4000)
