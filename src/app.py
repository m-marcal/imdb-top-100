from flask import Flask
from flask import render_template

import service

app = Flask(__name__)

@app.route('/')
def index():

    return render_template(
        'index.html', 
        ec2_instance_details=service.get_ec2_instance_details(), 
        imdb_movie=service.get_random_imdb_movie()
    )




