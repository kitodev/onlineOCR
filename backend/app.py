from flask import Flask, render_template, request
import os, pytesseract
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image

project_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_url_path='',static_folder="static", template_folder="templates")

img = UploadSet('photos', IMAGES)

app.config['UPLOAD_FOLDER'] = 'images'

class GetText(object):
    def __init__(self, file):
        self.file = pytesseract.image_to_string(Image.open(project_dir + '/images/' + file))

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'photo' not in request.files:
            return 'There is no image on form'
        img_name = request.form['image-name'] + '.jpg'
        img = request.files['photo']
        texta = request.form['text']
        path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
        img.save(path)

        text = GetText(img_name)
        
        return text.file
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)