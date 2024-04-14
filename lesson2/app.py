from flask import Flask, render_template, url_for, redirect, abort

app = Flask(__name__)

test_name = 'Flask'
max_score = 20
students = [
    {'id': 1, 'name': 'Andriy', 'score': 10},
    {'id': 2, 'name': 'Oleh', 'score': 20},
    {'id': 3, 'name': 'Artem', 'score': 5},
    {'id': 4, 'name': 'Dmytro', 'score': 15},
]


@app.route('/students')
def home():
    context = {
        'title': 'Students',
        'students': students,
        'max_score': max_score,
        'test': test_name
    }
    return render_template('index.html', **context)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/student/<int:id>')
def student(id):
    if id > len(students):
        return redirect(url_for('home'))
    elif id == 4:
        abort(403)
    return render_template('detail.html', student=students[id-1])


@app.errorhandler(404)
def error404(error):
    return render_template('error404.html'),  404



if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('about'))
        print(url_for('home'))
    app.run(debug=True)