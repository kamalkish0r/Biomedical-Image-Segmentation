from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class ImageUploadForm(FlaskForm):
    model_choices = [('UNet', 'Unet'), ('LinkNet', 'Linknet'), ('SAM', 'SAM')]
    model = SelectField('Select segmentation model: ', choices=model_choices, validators=[DataRequired()])
    image = FileField('Select an Image: ', validators=[DataRequired()])
    submit = SubmitField('Segment Image')

    # def validate_image(self, image):
    #     allowed_extensions = ['jpg', 'jpeg', 'png']
    #     f_ext = image.data.filename.split('.')[-1]
    #     if f_ext not in allowed_extensions:
    #         raise ValidationError(f'Only {", ".join(allowed_extensions)} files are allowed.')
    #     # if not '.' in image.data.filename or image.data.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
    #     #     raise ValidationError(f'Only {", ".join(allowed_extensions)} files are allowed.')
