# Use a lightweight Alpine base image with Python 3.11
FROM ubuntu:22.04 	

# Set the working directory
WORKDIR /app  

RUN set -xe \
    && apt-get update -y \
    && apt-get install python3-pip -y

RUN pip install --upgrade pip

RUN apt-get install -y pkg-config \
    && apt-get install libcairo2-dev libjpeg-dev libgif-dev -y \
    && apt install libsystemd-dev -y \
    && apt install build-essential libpython3-dev libdbus-1-dev libgirepository1.0-dev -y

RUN pip3 install "cython<3.0.0" wheel && pip3 install pyyaml==5.4.1 --no-build-isolation

# Copy requirements file
COPY requirements.txt requirements.txt  
# Install dependencies
RUN pip install -r /app/requirements.txt  

# Copy all other files to the working directory
COPY . . 

# Specify the command to run when the container starts
CMD ["python3", "yahoo_main.py", "https://finance.yahoo.com/quote/AMC?p=AMC&.tsrc=fin-srch"]  