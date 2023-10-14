# start by pulling the python image
FROM python:3.11


# copy the requirements file into the image
COPY ./web_app/app/requirements.txt /web_app/requirements.txt

# switch working directory
WORKDIR /web_app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image

COPY . /web_app

# switch to the www-data user
USER www-data

WORKDIR /web_app/app
# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]
