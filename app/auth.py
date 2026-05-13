from functools import wraps
from datetime import datetime, timedelta
from flask import request, jsonify
from jose import jwt, JWTError

SECRET_KEY = "mechanic-shop-secret-key"

def encode_token(customer_id):
    payload = {
        "sub": str(customer_id),
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"message": "Token is missing"}), 401

        try:
            token = auth_header.split(" ")[1]
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            customer_id = int(decoded_token["sub"])
        except (JWTError, IndexError, KeyError):
            return jsonify({"message": "Invalid token"}), 401

        return func(customer_id, *args, **kwargs)

    return wrapper