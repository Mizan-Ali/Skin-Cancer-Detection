import os
from .predict import predict
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, flash


views = Blueprint("views", __name__)
UPLOAD_FOLDER = "./website/static/uploads/"
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])


def allowed_file(image):
    if not image:
        flash("No image uploaded.", category="error")
        return False
    
    if not image.mimetype:
        flash("Bad upload, try again.", category="error")
        return False
    
    if image.mimetype.split('/')[-1] not in ALLOWED_EXTENSIONS:
        flash("Uploaded file is not an image.", category="error")
        return False
    
    return True


def empty_upload():
    for file in os.listdir(path=UPLOAD_FOLDER):
        os.remove(os.path.join(UPLOAD_FOLDER, file))


@views.route("/", methods=["GET", "POST"])
def home():
    empty_upload()
    prediction, filename = None, None
    
    if request.method == "POST":
        image = request.files.get("image")
        
        if allowed_file(image):
            filename = secure_filename(image.filename)
            image.save(os.path.join(UPLOAD_FOLDER, filename))
            flash("Image uploaded successfully.", category="success")
            
            prediction = predict(filename)
            
    return render_template("home.html", predicted=prediction, filename=filename)


@views.route("/about")
def about():
    return render_template("about.html")