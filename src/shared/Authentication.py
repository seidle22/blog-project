from functools import wraps
import jwt
import os
import datetime
from flask import Response, g, json, request
from src.models.UserModels import UserModel


class Auth:
    """
    Auth Class
    """

    # @staticmethod
    # def generate_token(user_id):
    #     """
    #     Generate Token Method
    #     """
    #     try:
    #         payload = {
    #             "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
    #             "iat": datetime.datetime.utcnow(),
    #             "sub": user_id,
    #         }
    #         return jwt.encode(payload, "xyxyxyx", "HS256").decode("utf-8")
    #     except Exception as e:
    #         return Response(
    #             mimetype="application/json",
    #             response=json.dumps({"error": "error in generating user token"}),
    #             status=400,
    #         )
    @staticmethod
    def generate_token(user_id):
        """
        Generate Token Method
        """
        try:
            payload = {
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
                "iat": datetime.datetime.utcnow(),
                "sub": user_id,
            }
            return jwt.encode(payload, "xyxyxyx", "HS256")
        except Exception as e:
            raise RuntimeError("Error in generating user token")

    @staticmethod
    def decode_token(token):
        """
        Decode token method
        """

        re = {"data": {}, "error": {}}
        try:
            payload = jwt.decode(token, "xyxyxyx", algorithms=["HS256"])
            re["data"] = {"user_id": payload["sub"]}
            return re
        except jwt.ExpiredSignatureError as e:
            re["error"] = {"message": "token expired, please login again"}
            return re
        except jwt.InvalidTokenError:
            re["error"] = {
                "message": "Invalid token, please try again with a new token"
            }
            return re

    @staticmethod
    def auth_required(func):

        @wraps(func)
        def decorated_auth(*args, **kwargs):
            if "api-token" not in request.headers:
                return Response(
                    mimetype="application/json",
                    response=json.dumps(
                        {
                            "error": "Authentication token is not available, please login to get one"
                        }
                    ),
                    status=403,
                )
            token = request.headers.get("api-token")
            data = Auth.decode_token(token)
            if data["error"]:
                return Response(
                    mimetype="application/json",
                    response=json.dumps(data["error"]),
                    status=403,
                )

            user_id = data["data"]["user_id"]
            check_user = UserModel.get_one_user(user_id)
            if not check_user:
                return Response(
                    mimetype="application/json",
                    response=json.dumps(
                        {"error": "user does not exist, invalid token"}
                    ),
                    status=403,
                )
            g.user = {"id": user_id}
            return func(*args, **kwargs)

        return decorated_auth
