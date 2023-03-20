 # Our base image
 FROM alpine:3.12
 # Install python and pip
RUN apk update && \
        apk add py3-pip
 # install Python modules needed by the Python app
 COPY requirements.txt /usr/src/app/
 RUN pip install -r /usr/src/app/requirements.txt
 # copy files required for the app to run
 COPY app.py /usr/src/app/
 COPY templates/index.html /usr/src/app/templates/
 # tell the port number the container should expose
 EXPOSE 5000
 # run the application
 CMD python3 /usr/src/app/app.py
