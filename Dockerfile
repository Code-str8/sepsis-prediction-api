# the build 
FROM python:3.9.13    
#make folder in the container
WORKDIR /sepssis-api
#copy file to temp folder in container
COPY requirements.txt /tmp/requirements.txt
#run to install copied file in container
RUN python -m pip install -r /tmp/requirements.txt 
#copy all to the folder created in workdir
COPY . /sepssis-api
#expose port 80 outside of the container
EXPOSE 80
#command to run the app 
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
