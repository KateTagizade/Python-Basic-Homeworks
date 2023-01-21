from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class ServiceForm(FlaskForm):
    name = StringField(
        label="Service name",
        name="service-name",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )

