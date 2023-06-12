from flask_sqlalchemy import SQLAlchemy

db_tableau = SQLAlchemy()

class Tableau(db_tableau.Model):
    id = db_tableau.Column(db_tableau.Integer, primary_key=True)
    url = db_tableau.Column(db_tableau.String(255), unique=True, nullable=False)
    methode_HTTP = db_tableau.Column(db_tableau.String(255), nullable=False)
    redescription = db_tableau.Column(db_tableau.String(255), nullable=False)
    operationel = db_tableau.Column(db_tableau.String(255), nullable=False)
    commentaire = db_tableau.Column(db_tableau.String(255), nullable=False)
    
    def __repr__(self):
        return f'<Tableau {self.question}>'
    