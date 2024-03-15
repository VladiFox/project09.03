from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<a href="/random_fact"> Рандомный факт о лисах </a>'
    return '<a href="/imagee"> Лисичка :)</a>'
@app.route("/random_fact")
def randoom_fact():
    spisok = [
        "Лиса – это сравнительно крупное млекопитающее животное, которое относится к семейству псовых."
        "Существует около 12 видов диких лис"
        "Арктические лисы переживают самые суровые зимы на планете. В отличие от большинства лис, их шерсть меняет цвет в зависимости от сезона: она белая зимой для камуфляжа в снегу и серая летом."
    ]
    fact = random.choice(spisok)
    return f'<p>{random.choice(spisok)}</p>'
@app.route("/imagee")
def photo_fox():
    return '<img scr="лисааа.jpg">'
app.run(debug=True)