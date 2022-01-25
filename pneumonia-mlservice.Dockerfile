FROM tensorflow/tensorflow

ADD requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

ADD . . 

ENTRYPOINT [ "python", "server.py" ]