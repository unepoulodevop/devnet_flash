from flask import Flask, render_template, request, redirect, url_for
from models import db, Etudiant
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

@app.route('/')
def index():
    etudiants = Etudiant.query.all()
    return render_template('index.html', etudiants=etudiants)

@app.route('/add', methods=['POST'])
def add():
    nom = request.form['nom']
    email = request.form['email']
    etudiant = Etudiant(nom=nom, email=email)
    db.session.add(etudiant)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    etudiant = Etudiant.query.get_or_404(id)
    db.session.delete(etudiant)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
