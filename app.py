from flask import Flask, render_template, request, redirect, url_for

# initialize flask app
app = Flask(__name__)

# list to store to-do items 
todos = []

@app.route('/')
def home():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form['task']
    todos.append({'title': task, 'completed': False, 'editing': False})
    return redirect(url_for('home'))

@app.route('/clear', methods=['POST'])
def clear_todos():
    todos.clear()
    return redirect(url_for('home'))

@app.route('/edit/<int:index>', methods=['POST'])
def edit_task(index):
    action = request.form.get('action')
    if action == 'update':
        updated_task = request.form['task']
        todos[index]['title'] = updated_task
        todos[index]['editing'] = False 
    elif action == 'edit':
        todos[index]['editing'] = True
    else:
        pass
    return redirect(url_for('home'))
@app.route('/toggle_completed/<int:index>', methods=['POST'])
def toggle_completed(index):
    todos[index]['completed'] = 'completed' in request.form
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

    