from flask import Flask, jsonify, request
import repository

#Créer l'application
app = Flask(__name__)

#Definir les routes
@app.route('/')
def home():
    return "C'est cool REST"
@app.route('/students',methods=['GET'])
def get_student():
    students = repository.get_all_student()
    return jsonify(students), 200

@app.route('/students/<int:student_id>',methods=['GET'])
def get_student_by_id(student_id):
    student = repository.get_student_by_id(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}),404
    return jsonify(student),200

@app.route('/students/',methods=['POST'])
def add_student():
    new_student = request.get_json()
    student = repository.add_student(new_student)
    return jsonify(student),201

@app.route('/students/<int:id>',methods=['PUT'])
def update_student(id):
    new_data = request.get_json()
    modif = repository.update_student(id,new_data)
    if modif <= 0 :
        return jsonify({"erreur" : "Erreur de modification"})
    return jsonify(modif),200

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    supprimer = repository.delete_student(id)
    if supprimer <= 0 :
        return jsonify({"erreur" : "Erreur de suppression"})
    return jsonify(supprimer),200

#Lancer le serveur
#Force Flask à écouter sur toutes les interfaces (IPv4 - IPv6) :
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)