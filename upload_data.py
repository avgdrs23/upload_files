#!/usr/local/bin/python3
import flask
from flask import request
import os.path

UPLOAD_FOLDER = "/data"

upload_html="""
<html> <body> <title>Upload new File</title> <h1>Upload new File</h1>
		<form method="post" enctype="multipart/form-data" action="/upload">
		   <input type="file" name="file"> <input type="submit" value="Upload"></form>
                   <br><br>
                <form method="get" enctype="multipart/form-data" action="/list">
                   <h2> Press the List button for show your LIST files that you uploaded</h2> 
                        <input type="submit" value="LIST">
	        	</form></body> </html>

"""

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def show_file_upload():
    return upload_html

@app.route("/upload", methods=["POST"])
def upload():
    f = request.files["file"]
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
    return "<html><body>Your File was uploaded succesfully</body></html>"



@app.route("/list", methods=["GET"])
def show_files():
   files = os.listdir(app.config['UPLOAD_FOLDER'])
   f_names = '\n'.join(files)
   print(f_names, '\n')
   return f"<html><body><ul><h2> The Uploaded Files:</h2><li>{f_names}</li></ul></body></html>"


app.run(host="localhost", port="8080", debug=True)
