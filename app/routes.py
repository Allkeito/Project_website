from flask import render_template, jsonify, request
from app import app
import json

# Главная страница
@app.route("/")
def index():
    return render_template("index.html")

# Получение всех продуктов
@app.route("/products", methods=["GET"])
def get_products():
    with open("products.json", "r") as file:
        products = json.load(file)
    return jsonify(products)

# Добавление нового продукта
@app.route("/products", methods=["POST"])
def add_product():
    new_product = request.json
    with open("products.json", "r") as file:
        products = json.load(file)
    products.append(new_product)
    with open("products.json", "w") as file:
        json.dump(products, file, indent=4)
    return jsonify(new_product), 201