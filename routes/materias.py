from flask import Blueprint, jsonify, request
from app import db
from models.materias import Materias

materias_bp = Blueprint("materias", __name__)

@materias_bp.route("/", methods=["POST"])
def create_materia():
    try:
        data = request.get_json()

        nombre = data.get("nombre")
        descripcion = data.get("descripcion")

        new_materia = Materias(
            nombre=nombre,
            descripcion=descripcion
        )

        db.session.add(new_materia)
        db.session.commit()

        return jsonify({"message": "Materia creada exitosamente"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear la materia: " + str(e)}), 500


@materias_bp.route("/", methods=["GET"])
def get_materias():
    try:
        materias = Materias.query.all()
        materias_list = []

        for materia in materias:
            materia_data = {
                "id": materia.id,
                "nombre": materia.nombre,
                "descripcion": materia.descripcion
            }
            materias_list.append(materia_data)

        return jsonify(materias_list)

    except Exception as e:
        return jsonify({"error": "Error al listar las materias: " + str(e)}), 500


@materias_bp.route("/<int:id>", methods=["GET"])
def get_materia(id):
    try:
        materia = Materias.query.get(id)

        if materia:
            return jsonify(
                {
                    "nombre": materia.nombre,
                    "descripcion": materia.descripcion
                }
            )
        else:
            return jsonify({"message": "Materia no encontrada"}), 404

    except Exception as e:
        return jsonify({"error": "Error al obtener la materia: " + str(e)}), 500


@materias_bp.route("/<int:id>", methods=["PUT"])
def update_materia(id):
    try:
        materia = Materias.query.get(id)

        if materia:
            data = request.get_json()

            materia.nombre = data.get("nombre")
            materia.descripcion = data.get("descripcion")

            db.session.commit()

            return jsonify({"message": "Materia actualizada exitosamente"}), 200
        else:
            return jsonify({"message": "Materia no encontrada"}), 404

    except Exception as e:
        return jsonify({"error": "Error al actualizar la materia: " + str(e)}), 500


@materias_bp.route("/<int:id>", methods=["DELETE"])
def delete_materia(id):
    try:
        materia = Materias.query.get(id)

        if materia:
            db.session.delete(materia)
            db.session.commit()

            return jsonify({"message": "Materia eliminada exitosamente"})
        else:
            return jsonify({"message": "Materia no encontrada"}), 404

    except Exception as e:
        return jsonify({"error": "Error al eliminar la materia: " + str(e)}), 500
