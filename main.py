from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def mission():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    lines = (
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!",
    )

    return "<br>".join(lines)


@app.route('/image_mars')
def image_mars():
    return f"<b>Жди нас, Марс!</b><br>" \
           f"<img src={url_for('static', filename='img/MARS.png')}>" \
           f"<p>Вот она какая, красная планета</p>"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
