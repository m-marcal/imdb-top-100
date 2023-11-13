import os
import requests
import random

API_KEY = os.environ.get('TIMDb_API_KEY')

def get_random_imdb_movie():
    BASE_URL = 'https://api.themoviedb.org/3/movie/top_rated?language=en-US&page='

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    page = 2
    movies = list()
    while page > 0:

        url = f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={page}"
        response = requests.get(url, headers=headers).json()
        
        movies.extend(response['results'])
        page -= 1

    if len(movies) > 0:
        #return random.choice(movies) # IDK, this seems to be vicious
        return movies[random.randint(0,len(movies) -1)]
    else:
        return movies

def get_ec2_instance_details():
    METADATA_BASE_URL = 'http://169.254.169.254/latest/meta-data'
    try:
        instance_id_url = f"{METADATA_BASE_URL}/instance-id"
        instance_id = requests.get(instance_id_url, timeout=2).text

        instance_type_url = f"{METADATA_BASE_URL}/instance-type"
        instance_type = requests.get(instance_type_url, timeout=2).text

        private_ip_url = f"{METADATA_BASE_URL}/local-ipv4"
        private_ip = requests.get(private_ip_url, timeout=2).text

        subnet_id_url = f"{METADATA_BASE_URL}/network/interfaces/macs/INSTANCE_MAC/subnet-id"
        subnet_id = requests.get(subnet_id_url, timeout=2).text

        az_url = f"{METADATA_BASE_URL}/placement/availability-zone"
        availability_zone = requests.get(az_url, timeout=2).text

        ec2_instance_details = {
            "InstanceID": instance_id,
            "InstanceType": instance_type,
            "PrivateIP": private_ip,
            "SubnetID": subnet_id,
            "AvailabilityZone": availability_zone,
        }

        return ec2_instance_details
    except Exception as e:
        print(f"Error retrieving EC2 instance details: {str(e)}")
        return None