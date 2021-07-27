from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/yarim/PycharmProjects/pythonProject/todo.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos = todos)

@app.route('/add', methods = ["POST"]) #GET alınamaz, More safe...
def addTodo():
    baslik = request.form.get("title")
    icerik = request.form.get("content")
    newToda = Todo(title=baslik,content = icerik, complete = False)
    db.session.add(newToda)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/complete/<string:id>')
def completeTodo(id):
    todos2 = Todo.query.filter_by(id = id).first()
    if todos2.complete == False:
        todos2.complete = True
    else:
        todos2.complete = False
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<string:id>')
def deleteTodo(id):
    todos3 = Todo.query.filter_by(id = id).first()
    db.session.delete(todos3)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/detail/<string:id>')
def detailTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    return render_template("detail.html",todo=todo)
class Todo(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    complete = db.Column(db.Boolean)
if __name__ == "__main__":
    app.run(debug=True)

