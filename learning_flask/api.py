from flask import Flask,request,flash,jsonify
import numpy as np
import base64
from function import myfunc

app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome"

@app.route('/hello/',methods=['GET','POST'])
def hello():
    return "hello world"

@app.route('/<string:name>/',methods=['GET','POST'])
def name(name):
    return name

@app.route('/upload/',methods=['GET','POST'])
def upload_file():
    if request.method=='POST':
        f=request.files['file']
        print('fle name'+f.filename)
    else:
        flash('Post Method not selected')
    return 'uploadedd'
@app.route('/resize/',methods=['GET','POST'])
def image_processing():
    size=int(request.form['size'])
    for upload in request.files.getlist("file"):
        image=np.array(bytearray(upload.read()),dtype=np.uint8)
        resized_image=myfunc(image,size)
        encoded_resized_image=base64.b64encode(resized_image)
    return jsonify({"output_size":resized_image.shape,
                    "result_image":str(encoded_resized_image)})

@app.route('/json/',methods=['GET','POST'])
def json_example():
    info={}
    data=request.get_json()
    a=data['first_num']
    b=data['second_num']
    sum=a+b
    #info['first']=a
    #info['second']=b
    info['input']=[a,b]
    info['sum']=sum
    
    '''return jsonify({
        "input":info,
        "sum":sum
        })'''
    return info
    
        
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5050)