from flask import Flask, jsonify, request
#creer l'application Flask

app = Flask(__name__)

Persos = [{"id":1,"name":"viego","ability":"ad","classe":"combattant"},{"id":2,"name":"azir","ability":"ap","classe":"mage"}]

def home():
    return "Bienvenu dans cette page ici on parle de Lol et leur champions"
@app.route("/Persos", methods=["GET"])
def get_persos():
        "jsonify transforme la liste des perso en json"
        return jsonify(Persos)

@app.route("/Perso", methods=["POST"])
def add_perso():
      new_perso=request.get_json()

      new_perso["id"]=len(Persos)+1

      Persos.append(new_perso)
      return jsonify(new_perso), 201

@app.route("/Persos/<int:id>", methods=["GET"])
def get_perso(id):
      perso = next((p for p in Persos if p["id"]==id),None)
      if perso:
            return jsonify(perso)
      return jsonify({"erreur":"aucun perso trouvé"}),404

@app.route("/Persos/<int:id>", methods=["PUT"])
def update_perso(id):
      perso = next((p for p in Persos if p["id"]==id),None)
      if not perso:
        return jsonify({"message":"Perso non trouvé"}),404
      data=request.get_json()
      perso.update(data)
      return jsonify(perso)

if __name__ == "__main__":
    app.run(debug=True)
      
      
