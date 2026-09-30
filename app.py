import os
from urllib.parse import quote_plus

from flask import Flask
from dotenv import load_dotenv

from models import db
from controllers.main_controller import main
from controllers.db_controller import db_bp
from controllers.auth_controller import auth
from controllers.dashboard_controller import dashboard_bp

load_dotenv()

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "your-secret-key")

mysql_host = os.getenv("MYSQL_HOST", "localhost")
mysql_port = os.getenv("MYSQL_PORT", "3306")
mysql_user = quote_plus(os.getenv("MYSQL_USER", "root"))
mysql_password = quote_plus(os.getenv("MYSQL_PASSWORD", ""))
mysql_db = os.getenv("MYSQL_DB", "scholarship_db")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{mysql_user}:{mysql_password}"
    f"@{mysql_host}:{mysql_port}/{mysql_db}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(main)

app.register_blueprint(db_bp)

app.register_blueprint(auth)

app.register_blueprint(dashboard_bp)


if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", "5001")))