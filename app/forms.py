from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms.validators import DataRequired
from flask.helpers import send_from_directory
class UploadForm(FlaskForm):
    image= FileField('Image',validators=[FileRequired(), FileAllowed(['jpg','png'])])