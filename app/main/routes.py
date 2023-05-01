from flask import render_template, Blueprint, request, jsonify, redirect, current_app as app
import os
from app import db
from PIL import Image
from werkzeug.utils import secure_filename
import secrets
# from seg_models.SAM import run_sam
from ..seg_models.LinkNet import run_linknet
from ..seg_models.Unet import run_unet

main = Blueprint('main', __name__)



ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.files['img'] == None : 
            return render_template('home.html')

        file = request.files['img']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            random_hex = secrets.token_hex(8)
            _, f_ext = os.path.splitext(filename)
            filename = random_hex + f_ext


            if not os.path.exists(os.path.join('app', app.config['UPLOAD_FOLDER'])):
                os.makedirs(app.config['UPLOAD_FOLDER'])

            image_path = os.path.join('app', app.config['UPLOAD_FOLDER'], filename)

            file.save(image_path)
            model_choice = request.form['model']
            print(model_choice)
            if model_choice == 'Linknet':
                run_linknet.segment_image(filename=filename)
            elif model_choice == 'Unet':
                run_unet.segment_image(filename=filename)

            seg_filename = 'seg_' + filename
            
            return render_template('home.html', input_img = filename, seg_img = seg_filename)
       

    return render_template('home.html')
