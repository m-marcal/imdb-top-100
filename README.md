# EC2 details (and IMDb movie recommendation)

This web app serves as a simple web application that displays information about an EC2 instance running on AWS and provides a random recommendation for a top-rated movie from "The Movie Database" (TMDb).

## Features

- Displays EC2 instance details, including:
  - Instance ID
  - Instance Type
  - Private IP Address
  - Subnet ID
  - Availability Zone

- Provides a random recommendation for a top-rated movie from TMDb, including:
  - Movie Title
  - Movie Poster
  - Movie Summary

## Usage

Follow these instructions to set up and run the Flask web app:

### Prerequisites

- Python 3.x installed on your system.
- [Optional] Docker

### Setup

#### Local Development:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/your-flask-web-app.git

2. Create virtual environment:
   ```bash
   python3 -m venv venv

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate

4. Install dependecies:

   ```bash
   pip install -r requirements.txt

5. Export TMDb read API key:

   ```bash
   export TIMDb_API_KEY={YOUR_API_KEY}

5. Run:
    ```bash
    python3 src/app.py

#### Docker:
1. Build image:
    ```bash
    docker build -t local/imdb-top-100:latest .

2. Run:
    ```bash
    docker run -e TIMDb_API_KEY=API_KEY -p80:5000 local/imdb-top-100:latest