#!/usr/bin/env python3
"""
    basic flask
    returns a jsonify iin the format
    {"status": "OK"}
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
        returns a jsonify iin the format
        {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
