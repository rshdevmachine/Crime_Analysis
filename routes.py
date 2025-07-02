from app import app
from flask import jsonify, request, abort,render_template, url_for,json
import flask
from flask import make_response
import os
import re
import json
from time import time


@app.route('/crime-charts.html')
def crime_charts():
    return render_template('crime-charts.html')


@app.route('/crime-locator.html')
def crime_locator():
    return render_template('crime-locator.html')



from prediction import *
from werkzeug.utils import secure_filename
# @app.route('/crime-predictor.html', methods = ['GET', 'POST'])
# def crime_predictor():
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save(secure_filename(f.filename))
#         print('file uploaded successfully')
#     return render_template('crime-predictor.html')

@app.route('/crime-predictor.html', methods=['GET', 'POST'])
def crime_predictor():
    response = make_response(render_template('crime-predictor.html'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
      print(request)
      f = request.files['file']
      f.save(secure_filename(f.filename))
      print('file uploaded successfully11111111111111', f.filename)
      #return 'file uploaded successfully'
      predictfun(f.filename)
    return render_template('crime-predictor.html', cache_buster=int(time()))
      

@app.route('/feed.html')
def feed():
    return render_template('feed.html')


@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/help-page.html')
def helppage():
    return render_template('help-page.html')


from webscapper import *
@app.route('/',methods=['GET','POST'])

@app.route('/index.html')
def index():
    request_method=request.method
    if request.method=='POST':
        webscrappingfun()
    return render_template('index.html')

    