FROM ubuntu:latest

#Maintainer: Sebastian Schmidt

# Update aptitude with new repo
RUN apt-get update

# Install software 
RUN apt-get install -y git
RUN apt-get install -y python-pip python-dev build-essential

WORKDIR /app

#RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install --upgrade pip
RUN pip install flask psycopg2

RUN git clone https://github.com/mightyMarabu/landbook.git

EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "landbook/app/go.py"]
