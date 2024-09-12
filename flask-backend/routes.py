from flask import Blueprint, request, jsonify
from app import db
from models import User

main = Blueprint('main', __name__)

@main.route('/api/v1/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'correo': user.correo, 'nombre': user.nombre, 'edad': user.edad} for user in users]
    return jsonify({'payload': user_list})

@main.route('/api/v1/user/add', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(correo=data['correo'], nombre=data['nombre'], edad=data['edad'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuario agregado satisfactoriamente!'})

@main.route('/api/v1/user/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'Usuario eliminado correctamente!'})
    return jsonify({'message': 'Usuario no encontrado!'})

@main.route('/api/v1/user/update/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    if user:
        user.correo = data['correo']
        user.nombre = data['nombre']
        user.edad = data['edad']
        db.session.commit()
        return jsonify({'message': 'Usuario actualizado correctamente!'})
    return jsonify({'message': 'Usuario no encontrado!'})
