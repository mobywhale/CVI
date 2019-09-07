from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import DataRequired


class CviForm(FlaskForm):
    contractor = StringField('Contractor', validators=[DataRequired()])
    employer = StringField('Employer', validators=[DataRequired()])
    submit = SubmitField('Add Cvi')
