FROM python:3.10.0a4-buster

#Make a directory for the application
WORKDIR /app

#Install depencencies
COPY './requirements.txt' .
RUN pip install -r requirements.txt
#Copy our source code
COPY . .

#Run the application
CMD ["python", "app.py"]

