from flask import Blueprint, jsonify, request
from models.administrador import Administrador
from app import db
from flask_cors import CORS, cross_origin
administrador_bp = Blueprint("administrador", __name__)

@administrador_bp.route("/", methods=["POST"])
@cross_origin()
def create_administrador():
    try:
        data = request.get_json()

        usuario = data.get("usuario")
        password = data.get("password")

        new_administrador = Administrador(
            usuario=usuario,
            password=password
        )

        db.session.add(new_administrador)
        db.session.commit()

        return jsonify({"message": "Administrador creado exitosamente"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear el administrador: " + str(e)}), 500


@administrador_bp.route("/", methods=["GET"])
@cross_origin()
def get_administradores():
    try:
        administradores = Administrador.query.all()
        administradores_list = []

        for administrador in administradores:
            administrador_data = {
                "id": administrador.id,
                "usuario": administrador.usuario,
                "password": administrador.password
            }
            administradores_list.append(administrador_data)

        return jsonify(administradores_list)

    except Exception as e:
        return jsonify({"error": "Error al listar los administradores: " + str(e)}), 500


@administrador_bp.route("/<int:id>", methods=["GET"])
@cross_origin()
def get_administrador(id):
    try:
        administrador = Administrador.query.get(id)

        if administrador:
            return jsonify(
                {
                    "usuario": administrador.usuario,
                    "password": administrador.password
                }
            )
        else:
            return jsonify({"message": "Administrador no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": "Error al obtener el administrador: " + str(e)}), 500


@administrador_bp.route("/<int:id>", methods=["PUT"])
@cross_origin()
def update_administrador(id):
    try:
        administrador = Administrador.query.get(id)

        if administrador:
            data = request.get_json()

            administrador.usuario = data.get("usuario")
            administrador.password = data.get("password")

            db.session.commit()

            return jsonify({"message": "Administrador actualizado exitosamente"}), 200
        else:
            return jsonify({"message": "Administrador no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": "Error al actualizar el administrador: " + str(e)}), 500


@administrador_bp.route("/<int:id>", methods=["DELETE"])
@cross_origin()
def delete_administrador(id):
    try:
        administrador = Administrador.query.get(id)

        if administrador:
            db.session.delete(administrador)
            db.session.commit()

            return jsonify({"message": "Administrador eliminado exitosamente"})
        else:
            return jsonify({"message": "Administrador no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": "Error al eliminar el administrador: " + str(e)}), 500
