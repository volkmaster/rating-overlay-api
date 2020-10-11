from flask import Flask
from flask_cors import CORS

from helpers.json_encoder import CustomJSONEncoder
from views import match, player

app = Flask(__name__)
CORS(app, allow_headers="*", origins="*", methods="*")
app.json_encoder = CustomJSONEncoder  # type: ignore
app.url_map.strict_slashes = False

app.register_blueprint(match.bp)
app.register_blueprint(player.bp)


@app.route("/")
def root():
    return "Hello!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec
