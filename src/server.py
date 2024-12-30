from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from router import router

#Loading from .env
load_dotenv()

app = Flask(__name__)

#If loading fails port will be 8000
port = int(os.environ.get('PORT', 8000))

#Start
app.register_blueprint(router)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
