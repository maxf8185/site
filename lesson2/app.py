from flask import Flask, render_template, url_for, redirect, abort

app = Flask(__name__)

test_name = 'Flask'
max_score = 10
students = [
    {'id': 1, 'name': 'Cars', 'score': 10},
    {'id': 2, 'name': 'Fishes', 'score': 8},
    {'id': 3, 'name': 'Racing_at_night', 'score': 6},
    {'id': 4, 'name': 'Ladies', 'score': 5},
]


@app.route('/films')
def home():
    context = {
        'title': 'Films',
        'films': students,
        'viewers': max_score,
        'test': test_name
    }
    return render_template('index.html', **context)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/film/<int:id>')
def film(id):
    if id > len(students):
        return redirect(url_for('home'))
    elif id == 4:
        abort(403)
    return render_template('detail.html', films=students[id-1])


@app.errorhandler(404)
def error404(error):
    return render_template('error404.html'),  404



if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('about'))
        print(url_for('home'))
    app.run(debug=True)