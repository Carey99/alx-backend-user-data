#!/usr/bin/env python3
"""
    basic flask
    returns a jsonify iin the format
    {"status": "OK"}
"""
from flask import Flask, jsonify
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
        returns a jsonify iin the format
        {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """
        register a user
    """
    try:
        user = AUTH.register_user("email", "password")
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
