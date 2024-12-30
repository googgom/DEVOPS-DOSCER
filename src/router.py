from flask import Blueprint, request, jsonify, render_template_string
from db import get_db_connection

router = Blueprint("router", __name__)

# HTML-шаблон с формой для отправки POST-запроса
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Create User</title>
</head>
<body>
    <h1>Create a New User</h1>
    <form method="POST" action="/submit">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Create User</button>
    </form>
</body>
</html>
"""

@router.route("/", methods=["GET"])
def home():
    return get_users()

@router.route("/users", methods=["GET"])
def get_users():
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM users")
            rows = cur.fetchall()
        return jsonify([{"name": row[0]} for row in rows])
    except Exception as e:
        return f"Error: cannot get users list: {e}", 500

@router.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.json
        name = data.get("name")
        if not name:
            return "User name is necessary.", 400

        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id, name", (name,))
            new_user = cur.fetchone()
        conn.commit()
        if new_user:
            return jsonify({"id": new_user[0], "name": new_user[1]}), 201
        else:
            return "User creation ERROR.", 500
    except Exception as e:
        return f"User creation ERROR: {e}", 500

@router.route("/submit", methods=["GET", "POST"])
def submit_user_form():
    if request.method == "GET":
        return render_template_string(HTML_FORM)
    elif request.method == "POST":
        try:
            name = request.form.get("name")
            if not name:
                return "User name is necessary.", 400

            conn = get_db_connection()
            with conn.cursor() as cur:
                cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id, name", (name,))
                new_user = cur.fetchone()
            conn.commit()
            if new_user:
                return f"User created successfully: {new_user[1]} (ID: {new_user[0]})", 201
            else:
                return "User creation ERROR.", 500
        except Exception as e:
            return f"User creation ERROR: {e}", 500
