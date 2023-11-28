from flask import Blueprint, jsonify
from routes.detalle_materia import DetalleMateria
from routes.materias import Materias

materiasuser_bp = Blueprint("materiasuser", __name__)

@materiasuser_bp.route("/<int:alumno_id>", methods=["GET"])
def obtener_materias_por_alumno(alumno_id):
    try:
        detalle_materias = DetalleMateria.query.filter_by(id_alumno=alumno_id).all()

        materias_list = []
        for detalle_materia in detalle_materias:
            materia = Materias.query.get(detalle_materia.id_materia)
            if materia:
                materia_data = {
                    "nombre": materia.nombre,
                    "descripcion": materia.descripcion,
                    "calificacion": float(detalle_materia.calificacion)
                }
                materias_list.append(materia_data)

        return jsonify(materias_list)

    except Exception as e:
        return jsonify({"error": "Error al obtener las materias del alumno: " + str(e)}), 500
