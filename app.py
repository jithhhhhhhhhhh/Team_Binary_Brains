
import numpy as np
import os
from flask import Flask, app,request,render_template
from keras import models
from keras.models import load_model
from keras_preprocessing import image
from tensorflow.python.ops.gen_array_ops import concat
from keras.applications.inception_v3 import preprocess_input
import requests
from flask import Flask, request, render_template, redirect, url_for
import cv2



app=Flask(__name__)

#default home page or route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def inde1():
    return render_template('index.html')



@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/nailhome')
def nailhome():
    return render_template('nailhome.html')

@app.route('/nailpred')
def nailpred():
    return render_template('nailpred.html')
@app.route('/description')
def description():
    return render_template('description.html')

@app.route('/dengue')
def dengue():
    return render_template('dengue.html')


@app.route('/stressbuster')
def stressbuster():
    return render_template('stressbuster.html')

@app.route('/tic')
def tic():
    return render_template('tic.html')

@app.route('/finger')
def finger():
    return render_template('finger.html')

@app.route('/gemini')
def gemini():
    return render_template('gemini.html')

@app.route('/llm')
def llm():
    return render_template('llm.html')

@app.route('/carhome')
def carhome():
    return render_template('carhome.html')

@app.route('/map1game')
def map1game():
    return render_template('map1game.html')

@app.route('/map2game')
def map2game():
    return render_template('map2game.html')

@app.route('/selectmode')
def selectmode():
    return render_template('selectmode.html')

@app.route('/qoute')
def qoute():
    return render_template('qoute.html')

@app.route('/guess')
def guess():
    return render_template('guess.html')

@app.route('/two84')
def two84():
    return render_template('two84.html')

@app.route('/brick')
def brick():
    return render_template('brick.html')

@app.route('/test')
def test():
    return render_template('test.html')


""" Running our application """
if __name__ == "__main__":
    app.run(debug =True, port = 8080)