from flask import Blueprint, jsonify, request
from models.alumos import Alumnos
from flask_cors import CORS, cross_origin
from app import db

alumnos_bp = Blueprint("alumnos", __name__)

@alumnos_bp.route("/", methods=["POST"])
@cross_origin()
def create_alumno():
    try:
        data = request.get_json()

        nombre = data.get("nombre")
        apellidos = data.get("apellidos")
        carrera = data.get("carrera")

        new_alumno = Alumnos(
            nombre=nombre,
            apellidos=apellidos,
            carrera=carrera
        )

        db.session.add(new_alumno)
        db.session.commit()

        return jsonify({"message": "Alumno creado exitosamente"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear el alumno: " + str(e)}), 500


@alumnos_bp.route("/", methods=["GET"])
@cross_origin()
def get_alumnos():
    try:
        alumnos = Alumnos.query.all()
        alumnos_list = []

        for alumno in alumnos:
            alumno_data = {
                "id": alumno.id,
                "nombre": alumno.nombre,
                "apellidos": alumno.apellidos,
                "carrera": alumno.carrera
            }
            alumnos_list.append(alumno_data)

        return jsonify(alumnos_list)

    except Exception as e:
        return jsonify({"error": "Error al listar los alumnos: " + str(e)}), 500


@alumnos_bp.route("/<int:id>", methods=["GET"])
@cross_origin()
def get_alumno(id):
    try:
        alumno = Alumnos.query.get(id)

        if alumno:
            return jsonify(
                {
                    "nombre": alumno.nombre,
                    "apellidos": alumno.apellidos,
                    "carrera": alumno.carrera
                }
            )
        else:
            return jsonify({"message": "Alumno no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": "Error al obtener el alumno: " + str(e)}), 500


@alumnos_bp.route("/<int:id>", methods=["PUT"])
@cross_origin()
def update_alumno(id):
    try:
        alumno = Alumnos.query.get(id)

        if alumno:
            data = request.get_json()

            alumno.nombre = data.get("nombre")
            alumno.apellidos = data.get("apellidos")
            alumno.carrera = data.get("carrera")

            db.session.commit()

            return jsonify({"message": "Alumno actualizado exitosamente"}), 200
        else:
            return jsonify({"message": "Alumno no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": "Error al actualizar el alumno: " + str(e)}), 500


@alumnos_bp.route("/<int:id>", methods=["DELETE"])
@cross_origin()
def delete_alumno(id):
    try:
        alumno = Alumnos.query.get(id)

        if alumno:
            db.session.delete(alumno)
            db.session.commit()

            return jsonify({"message": "Alumno eliminado exitosamente"})
        else:
            return jsonify({"message": "Alumno no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": "Error al eliminar el alumno: " + str(e)}), 500
