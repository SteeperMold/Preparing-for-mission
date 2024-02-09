from flask import Flask, url_for, request, render_template
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        prof = 'engineering'
    else:
        prof = 'science'
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('prof_list.html', list=list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = {
        'title': 'Ответ',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'Выше среднего',
        'profession': 'Штурман марсохода',
        'sex': 'Male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': True,
    }
    return render_template('auto_answer.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
