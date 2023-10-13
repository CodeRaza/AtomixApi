from atomixapi import AtomixAPI

port = 3001

app = AtomixAPI()

users_data = [
    {"id": 1, "username": "Ali", "email": "coder.raza@gmail.com"},
    {"id": 2, "username": "Asif", "email": "coder.raza@gmail.com"},
    {"id": 3, "username": "Qasim", "email": "coder.raza@gmail.com"},
    {"id": 4, "username": "Hassan", "email": "coder.raza@gmail.com"},
]

def users(req, res):
    print(req)
    res.json(users_data)

def home(req, res):
    res.send("Hello!")

def user(req, res):
    res.json(users_data)
    
app.get('/', home)
app.get('/users', users)
# app.get('/users/:id', user)


app.listen(port)