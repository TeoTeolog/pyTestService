from flask import Flask, request
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 8080))


@app.route("/")
def hello():
    name = request.args.get("name", "Recruto")
    message = request.args.get("message", "Let's be friends")

    response_message = f"Hello {name}! {message}."

    link_to_service = (
        f"{request.host_url}?name=(place name here)&message=(place message here)"
    )

    final_response = (
        f"{response_message}\n\nTry another link to service: {link_to_service}"
    )

    return final_response


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=port)
