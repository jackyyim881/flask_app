from flask import render_template, flash, redirect, url_for, request
from ..database.db import get_all_users, create_user, set_user_profile_picture_file_names
from .Create_Collection import create, list_collections, delete
from ..uploads.file_handler import is_file_type_allowed, upload_file_to_s3
from werkzeug.utils import secure_filename
import os
from config import Config
import io
from PIL import Image, ImageDraw, ExifTags, ImageColor, ImageFont
from .Register_Faces import add_face_to_collection 
from .Face_recognize import face_recognition_saving_image
from app.aws import aws
from app import app
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

@aws.route("/s3", methods=['GET'])
def home():    
    users = get_all_users()
    return render_template('aws/s3page.html', users=users)


@aws.route("/sign-up-new-user", methods=['POST'])
def sign_up_new_user():
    name = request.form['name']
    create_user(name)
    return redirect(url_for('aws/s3page.html'))


@aws.route("/upload-image/<user_id>", methods=['POST'])
def upload_image(user_id):
    if 'file' not in request.files:
        flash('No file uploaded', 'danger')
        return redirect(url_for('aws/s3page.html'))
    
    file_to_upload = request.files['file']

    if file_to_upload.filename == '':
        flash('No file uploaded', 'danger')
        return redirect(url_for('aws/s3page.html'))
    
    if file_to_upload and is_file_type_allowed(file_to_upload.filename):
        provided_file_name = secure_filename(file_to_upload.filename)
        stored_file_name = upload_file_to_s3(file_to_upload, provided_file_name)
        set_user_profile_picture_file_names(user_id, stored_file_name, provided_file_name)
        flash(f'{provided_file_name} was successfully uploaded', 'success')
    
    return redirect(url_for('aws/s3page.html'))

### 
@aws.route('/reko1')
def start_page():
    return render_template('aws/reko_index.html')

@aws.route('/collection')
def collection_page():
    count,lst=list_collections()
    return render_template(('aws/collection.html'), count=count, lst=lst)


@aws.route('/create_page', methods=['POST'])
def create_page():
    COLLECTION_NAME = str(request.form['collection-name'])
    COLLECTION_NAME=COLLECTION_NAME.strip()
    print(COLLECTION_NAME)
    statement=create(COLLECTION_NAME)
    print(statement)
    count,lst=list_collections()
    return render_template('aws/collection.html', count=count, lst=lst, statement=statement)


@aws.route('/delete_page')
def delete_page():
    COLLECTION_NAME=request.args.get('name')
    statement=delete(COLLECTION_NAME)
    count,lst=list_collections()
    return render_template('aws/collection.html', count=count, lst=lst, statement=statement)


@aws.route('/register_faces')
def register_page_reko():
    count,lst=list_collections()
    return render_template('aws/reko_register.html', lst=lst)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@aws.route('/register_faces', methods=['POST'])
def register_faces():
    if 'file' not in request.files:
        statement='No file part'
        count, lst = list_collections()
        return render_template('aws/reko_register.html', lst=lst,statement=statement)
    file = request.files['file']
    if file.filename == '':
        statement='No image selected for uploading'
        count, lst = list_collections()
        return render_template('aws/reko_register.html', lst=lst, statement=statement)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        Register_image = Image.open('static/uploads/' + filename)
        print(Register_image)
        bytes_array = io.BytesIO()
        Register_image.save(bytes_array, format="PNG")
        source_image_bytes = bytes_array.getvalue()
        name = str(request.form['person-name'])
        name = name.strip()
        COLLECTION_NAME=request.form['collection']
        print(name)
        print(COLLECTION_NAME)
        count, lst = list_collections()
        registration_result = add_face_to_collection(source_image_bytes, name, COLLECTION_NAME)
        #print('upload_image filename: ' + filename)
        # flash('Image successfully uploaded and displayed below')
        return render_template('aws/reko_register.html', lst=lst, reg_lst=registration_result, filename=filename)
    else:
        statement='Allowed image types are -> png, jpg, jpeg, gif'
        count, lst = list_collections()
        return render_template('aws/reko_register.html', lst=lst, statement=statement)

@aws.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@aws.route('/display/<filename>')
def display_image_recognition(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='result/' + filename), code=301)

@aws.route('/recognize_page')
def recognize_page():
    count,lst=list_collections()
    return render_template('aws/recognize.html', lst=lst)

@aws.route('/recognize_faces', methods=['POST'])
def recognize_faces():
    if 'file' not in request.files:
        statement='No file part'
        count, lst = list_collections()
        return render_template('aws/recognize.html', lst=lst,statement=statement)
    file = request.files['file']
    if file.filename == '':
        statement='No image selected for uploading'
        count, lst = list_collections()
        return render_template('recognize.html', lst=lst, statement=statement)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        Register_image = Image.open('static/uploads/' + filename)
        print(Register_image)

        COLLECTION_NAME=request.form['collection']
        print(COLLECTION_NAME)
        count, lst = list_collections()

        path="result/"+filename
        result_img,res_lst = face_recognition_saving_image(Register_image, COLLECTION_NAME)
        result_img.save('static/'+path)

        #print('upload_image filename: ' + filename)
        # flash('Image successfully uploaded and displayed below')
        return render_template('aws/recognize.html', lst=lst, filename=path,res_lst=res_lst)
    else:
        statement='Allowed image types are -> png, jpg, jpeg, gif'
        count, lst = list_collections()
        return render_template('aws/recognize.html', lst=lst, statement=statement)

@aws.after_request
def add_header(response):
    response.headers['Pragma'] = 'no-cache'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Expires'] = '0'
    return response
