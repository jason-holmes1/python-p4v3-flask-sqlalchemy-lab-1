from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model, SerializerMixin): 
    _tablename_ = 'earthquakes'
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String(255))
    year = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f'<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>'
