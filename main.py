import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import cv2
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def processImage(file,operation):
  print(f"filename is {file} and the Operation is :{operation}")
  img = cv2.imread(f"uploads/{file}")
  match operation:
    case "cgrey":
      newFile = f"static/{file}"
      imgProcessed = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
      cv2.imwrite(newFile,imgProcessed)
      return newFile
    case "cpng":
      newFile = f"static/{file.split('.')[0]}.png"
      cv2.imwrite(newFile,img)
      return newFile
    case "cjpg":
      newFile = f"static/{file.split('.')[0]}.jpg"
      cv2.imwrite(newFile,img)
      return newFile
    case "cwebp":
      newFile = f"static/{file.split('.')[0]}.webp"
      cv2.imwrite(newFile,img)
      return newFile
  pass


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/edit", methods=["GET","POST"])
def edit():
    if request.method == 'POST':
        op = request.form.get('Operation')
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "Error : No file Selected"
        file = request.files['file']
        
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return "Error: Please Select the file"
          
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            newFilename = processImage(filename,op)
            flash(f"Your file has been Processed and availble here <a href='/{newFilename}' target='_blank'>here</a>")
            return redirect(url_for('home'))
          
    return render_template("index.html")

app.run(host="127.0.0.1", port=5000, debug=True)