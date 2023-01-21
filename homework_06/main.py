from os import getenv

from flask import Flask, url_for, render_template, request, redirect

from views import ServiceForm
from models import db, Service

from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest


app = Flask(
    __name__,
)


CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

db.init_app(app)


@app.cli.command("db-create-all")
def db_create_all():
    db.create_all()


@app.route("/")
def get_root():
    return render_template("index.html")

@app.route("/home/", endpoint="home")
def get_root():
    return render_template("index.html")
@app.route("/items/", endpoint="items")
def services_list():
    services = Service.query.all()
    return render_template(
        "items.html",
        services=services,
    )

@app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    form = ServiceForm()

    if request.method == "GET":
        return render_template("services_add.html", form=form)
#    if not form.validate_on_submit():
#        return render_template("services_add.html", form=form), 400

    service_name = form.name.data
    service = Service(name=service_name)
    db.session.add(service)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"Could not create service {service_name!r},"
                         f" probably such service already exists.")

    url = url_for("items")
    return redirect(url)