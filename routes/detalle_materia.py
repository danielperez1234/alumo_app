from flask import Blueprint, jsonify, request
from app import db
from models.detalle_materia import DetalleMateria
from models.alumos import Alumnos
from models.materias import Materias

detalle_materia_bp = Blueprint("detalle_materia", __name__)

@detalle_materia_bp.route("/", methods=["POST"])
def create_detalle_materia():
    try:
        data = request.get_json()

        id_alumno = data.get("id_alumno")
        id_materia = data.get("id_materia")
        #calificacion = data.get("calificacion")

        new_detalle_materia = DetalleMateria(
            id_alumno=id_alumno,
            id_materia=id_materia,
            #calificacion=calificacion
        )

        db.session.add(new_detalle_materia)
        db.session.commit()

        return jsonify({"message": "Detalle de materia creado exitosamente"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear el detalle de materia: " + str(e)}), 500


@detalle_materia_bp.route("/", methods=["GET"])
def get_detalles_materia():
    try:
        detalles_materia = DetalleMateria.query.all()
        detalles_materia_list = []

        for detalle_materia in detalles_materia:
            detalle_materia_data = {
                "id": detalle_materia.id,
                "id_alumno": detalle_materia.id_alumno,
                "id_materia": detalle_materia.id_materia,
                "calificacion": float(detalle_materia.calificacion)
            }
            detalles_materia_list.append(detalle_materia_data)

        return jsonify(detalles_materia_list)

    except Exception as e:
        return jsonify({"error": "Error al listar los detalles de materia: " + str(e)}), 500


@detalle_materia_bp.route("/<int:id>", methods=["GET"])
def get_detalle_materia(id):
    try:
        detalle_materia = DetalleMateria.query.get(id)

        if detalle_materia:
            return jsonify(
                {
                    "id_alumno": detalle_materia.id_alumno,
                    "id_materia": detalle_materia.id_materia,
                    "calificacion": float(detalle_materia.calificacion)
                }
            )
        else:
            return jsonify({"message": "Detalle de materia no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": "Error al obtener el detalle de materia: " + str(e)}), 500


@detalle_materia_bp.route("/<int:id>", methods=["PUT"])
def update_detalle_materia(id):
    try:
        detalle_materia = DetalleMateria.query.get(id)

        if detalle_materia:
            data = request.get_json()

            detalle_materia.calificacion = data.get("calificacion")

            db.session.commit()

            return jsonify({"message": "Detalle de materia actualizado exitosamente"}), 200
        else:
            return jsonify({"message": "Detalle de materia no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": "Error al actualizar el detalle de materia: " + str(e)}), 500


@detalle_materia_bp.route("/<int:id>", methods=["DELETE"])
def delete_detalle_materia(id):
    try:
        detalle_materia = DetalleMateria.query.get(id)

        if detalle_materia:
            db.session.delete(detalle_materia)
            db.session.commit()

            return jsonify({"message": "Detalle de materia eliminado exitosamente"})
        else:
            return jsonify({"message": "Detalle de materia no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": "Error al eliminar el detalle de materia: " + str(e)}), 500
