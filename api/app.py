import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

@app.route('/user/new', methods=['POST'])
def create_user():
    data = request.json
    name = data['name']
    age = data['age']

    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'uid': new_user.uid}), 201

@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'uid': user.uid, 'name': user.name, 'age': user.age} for user in users]
    return jsonify({'users': user_list})

@app.route('/user/<string:uid>', methods=['GET'])
def get_user(uid):
    user = User.query.get(uid)
    if user:
        user_data = {'uid': user.uid, 'name': user.name, 'age': user.age}
        return jsonify(user_data)
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/user/<string:uid>', methods=['PUT'])
def update_user(uid):
    data = request.json
    name = data['name']
    age = data['age']

    user = User.query.get(uid)
    if user:
        user.name = name
        user.age = age
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/user/<string:uid>', methods=['DELETE'])
def delete_user(uid):
    user = User.query.get(uid)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
