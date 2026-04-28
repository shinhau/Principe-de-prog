from flask import Flask, jsonify, request
#creer l'application Flask

app = Flask(__name__)

#une liste de student
Students = [{"id":1,"name":"Ilyes","age":23},{"id":2,"name":"Emna","age":23}]
#activer mode debug pour voir les erreurs et recharger automatiquement 
@app.route("/")
def home():
    return "Bienvenue dans l'API de gestion de students en json"
@app.route("/Students", methods=['GET'])
def get_students():
    "jsonify transform la liste students en json"
    return jsonify(Students)
@app.route("/Students", methods=['POST'])
def add_student():
    new_student=request.get_json()
#pour recuperer les donnes par le client 
    new_student["id"]=len(Students)+1
#Attribuer un numero de maniere incrementable 
    Students.append(new_student)
    return jsonify(new_student), 201
#Le code 201 pour dire création réussie

#afficher un étudiant sachant son identifiant

@app.route("/Students/<int:id>", methods=["GET"])
def get_student(id):
    student = next((s for s in Students if s["id"]==id),None)
    if student:
        return jsonify(student)
    return jsonify({"erreur":"l'etudiant n'existe pas !"}),404

#Mettre a jour un etudiant PUT 

@app.route ("/Students/<int:id>", methods=["PUT"])
def update_student(id):
    student =next((s for s in Students if s["id"]==id),None)
    if not student:
        return jsonify({"message":"Etudiant non trouvé!"}),404
    data=request.get_json()
    student.update(data)#mise a jour des données
    return jsonify(student)
@app.route("/Students/<int:id>", methods = ["DELETE"])
def delete_student(id):
    student = next((s for s in Students if s['id'] == id),None)
    if not student :
        return jsonify({"message" : "Impossible de supprimer l'etudiant"}),404
    Students.remove(student)
    return  jsonify({"message" : "Etudiant supprimé a succès"}),200

if __name__ == '__main__':
    app.run(debug=True)