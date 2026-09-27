import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    app_env = os.getenv("APP_ENV", "Development")
    app_version = os.getenv("APP_VERSION", "2.0")

    return render_template(
        "index.html",
        app_env=app_env,
        app_version=app_version
    )


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "cybunny",
        "version": os.getenv("APP_VERSION", "2.0")
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
