from flask_wtf import FlaskForm
from wtforms import SubmitField

class ClearAllFavoritesForm(FlaskForm):
    submit_clear = SubmitField(label='Delete all favorites')

class SelectAllFavoritesForm(FlaskForm):
    submit_select = SubmitField(label='Select all favorites')