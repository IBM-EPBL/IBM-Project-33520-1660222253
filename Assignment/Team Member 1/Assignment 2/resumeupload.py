from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')

def upload_file():
        return render_template("resumeUp.html")


@app.route('/uploader' , methods = ['GET','POST'])
def flask_upload():
        if request.method == 'POST' :
                f = request.files['file']
                f.save(secure_filename(f.filename))
                return "File uploaded successfully"
        
        
if __name__ == "__main__":
    app.run(debug = True)