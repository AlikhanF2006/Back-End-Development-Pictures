"""Pictures REST API, aligned with the IBM capstone endpoints.

This educational implementation keeps pictures in memory. Newly created or
modified records will reset when the process restarts. For production use,
replace the list with persistent storage.
"""

import json
from pathlib import Path

from flask import jsonify, request

from backend import app

_data_path = Path(__file__).resolve().parent / "data" / "pictures.json"
with _data_path.open(encoding="utf-8") as source:
    data = json.load(source)


def _get_by_id(picture_id):
    return next((item for item in data if item["id"] == picture_id), None)


@app.get("/")
def home():
    return jsonify(service="Pictures API", status="OK", endpoints=["/health", "/count", "/picture"]), 200


@app.get("/health")
def health():
    return jsonify(status="OK"), 200


@app.get("/count")
def count():
    return jsonify(length=len(data)), 200


@app.get("/picture")
def get_pictures():
    return jsonify(data), 200


@app.get("/picture/<int:id>")
def get_picture_by_id(id):
    picture = _get_by_id(id)
    if picture is None:
        return jsonify(message="picture not found"), 404
    return jsonify(picture), 200


@app.post("/picture")
def create_picture():
    picture = request.get_json(silent=True)
    if not isinstance(picture, dict) or not isinstance(picture.get("id"), int):
        return jsonify(message="valid JSON picture with an integer id required"), 400
    if _get_by_id(picture["id"]) is not None:
        return jsonify(Message=f"picture with id {picture['id']} already present"), 302
    data.append(picture)
    return jsonify(picture), 201


@app.put("/picture/<int:id>")
def update_picture(id):
    picture = _get_by_id(id)
    if picture is None:
        return jsonify(message="picture not found"), 404
    incoming = request.get_json(silent=True)
    if not isinstance(incoming, dict):
        return jsonify(message="JSON object required"), 400
    if "id" in incoming and incoming["id"] != id:
        return jsonify(message="picture id cannot be changed"), 400
    picture.update(incoming)
    picture["id"] = id
    return jsonify(picture), 200


@app.delete("/picture/<int:id>")
def delete_picture(id):
    picture = _get_by_id(id)
    if picture is None:
        return jsonify(message="picture not found"), 404
    data.remove(picture)
    return "", 204
