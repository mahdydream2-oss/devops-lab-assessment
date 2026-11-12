"""خدمة المفقودات - تطبيق اختبار عملي لبرنامج أساسيات هندسة DevOps.

Lost and found items service used for the hands-on assessment lab.
"""
from datetime import datetime, timezone

from flask import Flask, jsonify, render_template, request

APP_VERSION = "1.1.0"
CATEGORIES = {"wallet", "phone", "keys", "documents", "other"}

app = Flask(__name__)
_items = []


def validate_item(data):
    """Return a list of validation errors (empty list means valid)."""
    errors = []
    if not isinstance(data, dict):
        return ["body must be a JSON object"]
    found_at = str(data.get("found_at", "")).strip()
    if len(found_at) < 3:
        errors.append("found_at is required (3 characters or more)")
    if data.get("category") not in CATEGORIES:
        errors.append("category must be one of: " + ", ".join(sorted(CATEGORIES)))
    notes = str(data.get("notes", ""))
    if len(notes) > 300:
        errors.append("notes must be 300 characters or less")
    phone = str(data.get("contact_phone", "")).strip()
    if phone and not (len(phone) == 10 and phone.isdigit() and phone.startswith("05")):
        errors.append("contact_phone must be 10 digits starting with 05")
    return errors


def create_item(data):
    item = {
        "id": len(_items) + 1,
        "found_at": data["found_at"].strip(),
        "category": data["category"],
        "notes": data.get("notes", "").strip(),
        "contact_phone": data.get("contact_phone", "").strip(),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _items.append(item)
    return item


@app.get("/")
def index():
    return render_template("index.html", version=APP_VERSION, items=list(reversed(_items)))


@app.get("/health")
def health():
    return jsonify(status="ok", version=APP_VERSION)


@app.get("/api/items")
def list_items():
    return jsonify(_items)


@app.post("/api/items")
def add_item():
    data = request.get_json(silent=True)
    errors = validate_item(data)
    if errors:
        return jsonify(errors=errors), 400
    return jsonify(create_item(data)), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
