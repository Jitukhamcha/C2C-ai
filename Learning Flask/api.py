from flask import Flask, request, flash, jsonify
import base64
import numpy as np
from function import myfunc
app = Flask (__name__)

@app.route('/')

def home():
    return "Welcome"

@app.route('/hello/', methods = ['GET', 'POST'])
def hello():
    return "Hello World!"

@app.route('/<string:name>/', methods=['GET', 'POST'])
def name(name):
    return name

@app.route('/upload/', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
            f = request.files['file']
            print("file name:::", f.filename)
            f.save(f.filename)
            return "uploaded"
    else:
            flash("POST method required!")
            return "not uploaded"
        
@app.route('/resize/', methods = ['GET', 'POST'])
def image_preprocessor():
    size=int(request.form['size'])
    for upload in request.files.getlist("file"):
        image = np.array(bytearray(upload.read()), dtype = np.unit8)
        resized_img = function.myfunc(image, size)
        print(resized_img.shape)
        encoded_img = base64.b64encode(resized_img)
        print(type(encoded_img))
        return jsonify({
            "output_size": resized_img.shape,
            "result_image": str(encoded_img)
            })
@app.route('/json-example', methods = ['GET', 'POST'])
def json_example():
    info={}
    data = request.get_json()
    a = data['firstnumber']
    b = data['secondnumber']
    info['input'] = [a,b]
            # info['first'] = a
            # info['second'] = b
    result = a+b
    info['result'] = result
    return info
'''return jsonify({
    "result" : result
                })'''
                    
if __name__ == '__main__':
    
    app.run(host = '0.0.0.0', port=5050, debug=True)