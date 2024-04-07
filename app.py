from flask import Flask, render_template

app = Flask(__name__)

@app.route('/students')
def students():
    students = [
        {"id": 1, "name": "Іванов Іван", "age": 20},
        {"id": 2, "name": "Петров Петро", "age": 22},
        {"id": 3, "name": "Сидорова Марія", "age": 21}
    ]
    return render_template('students.html', students=students)

@app.route('/about-me')
def about_me():
    personal_info = {
        "name": "Василь",
        "age": 25,
        "occupation": "Студент",
        "interests": ["програмування", "читання", "спорт"]
    }
    return render_template('about_me.html', personal_info=personal_info)


@app.route('/home/')
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/posts')
def posts():
    return render_template('posts.html')


if __name__ == '__main__':
    app.run(debug=True)


app = Flask(__name__)