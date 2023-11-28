from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from decouple import config# Agrega la importación de Flasgger
# import os

app = Flask(__name__)

app.json.sort_keys = False
app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_DATABASE_URI')
# SECRET_KEY = config('SECRET_KEY')
db = SQLAlchemy(app)


from routes.alumnos import alumnos_bp
from routes.materias import materias_bp
from routes.detalle_materia import detalle_materia_bp
from routes.administrador import administrador_bp
from routes.others import materiasuser_bp
app.register_blueprint(alumnos_bp, url_prefix='/alumnos')
app.register_blueprint(materias_bp, url_prefix='/materias')
app.register_blueprint(detalle_materia_bp, url_prefix='/detallemateria')
app.register_blueprint(administrador_bp, url_prefix='/administrador')
app.register_blueprint(materiasuser_bp, url_prefix='/materiasuser')