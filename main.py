from app import create_app
from app.migrate import init_db

app = create_app()

@app.route("/database")
def database():
    init_db()
    return "base de datos creada"


if __name__ == "__main__":
    app.run(debug = True)