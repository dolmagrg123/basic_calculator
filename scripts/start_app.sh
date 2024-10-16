#! /bin/bash

sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt install -y python3.9 python3.9-venv python3-pip nginx git
# Clone the GitHub repository if it doesn't already exist
if [ ! -d "basic_calculator" ]; then
  git clone https://github.com/dolmagrg123/basic_calculator.git
fi
cd basic_calculator
git pull
python3.9 -m venv venv
echo "Activating vitual env"
source venv/bin/activate
echo "Installing Requirements of the application"
pip install -r requirements.txt
pip install gunicorn pymysql cryptography
export FLASK_APP=app.py
flask translate compile
flask db upgrade
echo "Starting Gunicorn..."
gunicorn -b :5000 -w 4 microblog:app --daemon
