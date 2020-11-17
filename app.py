"""Flask app for Cupcakes"""

from flask import Flask, request, render_template, redirect, flash, jsonify

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret"

connect_db(app)

@app.route("/")
def home():
    """ show cupcake list and the add new cipcake form """

    return render_template("index.html")


@app.route("/api/cupcakes")
def list_cupcakes():
    """ list all cupcakes """

    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]

    return jsonify(cupcakes=cupcakes)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """ get the single cupcake """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes", methods=['POST'])
def create_cupcake():
    """ create cupcake """

    data = request.json

    cupcake = Cupcake(flavor=data["flavor"], 
        size=data["size"], 
        rating=data["rating"], 
        image=data["image"] or None)

    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize()), 201)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=['PATCH'])
def update_cupcake(cupcake_id):
    """ update the cupcake """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    data = request.json

    cupcake.flavor = data["flavor"]
    cupcake.size = data["size"]
    cupcake.rating = data["rating"]
    cupcake.image = data["image"]

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """ delete the cupcake """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")











