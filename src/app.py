from flask import Flask, render_template
import service

app = Flask(__name__)

@app.route('/')
def index():

    return render_template(
        'index.html', 
        ec2_instance_details=service.get_ec2_instance_details(), 
        imdb_movie=service.get_random_imdb_movie()
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0")

