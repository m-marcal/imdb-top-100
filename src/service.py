import os
import requests
import random

from movie import Movie
from ec2 import EC2

API_KEY = os.environ.get('TIMDb_API_KEY')

def get_random_imdb_movie():
    BASE_URL = 'https://api.themoviedb.org/3/movie/top_rated?language=en-US&page='

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    movie = Movie()

    try:

        page = random.randint(0, 40)
        url = f"{BASE_URL}{page}"
        response = requests.get(url, headers=headers).json()
        
        if 'results' in response:
            recomend = response['results'][random.randint(0, len(response['results']) - 1)]
            movie.title = recomend['title']
            movie.poster_path = recomend['poster_path']
            movie.overview = recomend['overview']
    except Exception as e:
        print(e)
    
    return movie

def get_ec2_instance_details():
    METADATA_BASE_URL = 'http://169.254.169.254/latest/meta-data'
    ec2 = EC2()
    try:
        ec2.id = requests.get(f"{METADATA_BASE_URL}/instance-id", timeout=1).text
        ec2.type = requests.get( f"{METADATA_BASE_URL}/instance-type", timeout=1).text
        ec2.private_ip = requests.get(f"{METADATA_BASE_URL}/local-ipv4", timeout=1).text
        
        instance_mac = requests.get(f"{METADATA_BASE_URL}/network/interfaces/macs", timeout=1).text.replace('/', '')
        ec2.subnet_id = requests.get(f"{METADATA_BASE_URL}/network/interfaces/macs/{instance_mac}/subnet-id", timeout=1).text

        ec2.av_zone = requests.get(f"{METADATA_BASE_URL}/placement/availability-zone", timeout=1).text
    except Exception as e:
        print(f"Error retrieving EC2 instance details: {str(e)}")
        
    return ec2