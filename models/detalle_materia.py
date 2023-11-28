from app import db
from sqlalchemy.orm import relationship

class DetalleMateria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_alumno = db.Column(db.Integer, db.ForeignKey('alumnos.id'))
    id_materia = db.Column(db.Integer, db.ForeignKey('materias.id'))
    calificacion = db.Column(db.DECIMAL(5, 2), default=0)

    alumno = relationship("Alumnos", backref="detalle_materia")
    materia = relationship("Materias", backref="detalle_materia")