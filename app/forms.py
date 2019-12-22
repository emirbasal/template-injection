from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, InputRequired
from wtforms.widgets import TextArea


class RequestFeatureForm(FlaskForm):
    title = StringField('Feature', validators=[Length(max=20), InputRequired()])
    description = StringField('Description', widget=TextArea())
    submit = SubmitField('Submit')
