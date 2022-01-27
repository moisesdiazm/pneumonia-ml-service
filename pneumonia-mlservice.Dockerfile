FROM python:3.7.3

#RUN apt-get update && apt-get install build-essential libjpeg62 -y
RUN apt-get update && apt-get install -y pkg-config libhdf5-100 libhdf5-dev
RUN pip install --upgrade pip setuptools wheel
RUN pip install pycocotools --no-binary pycocotools
ADD requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt
RUN python -m pip install https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0-rc2/tensorflow-2.4.0rc2-cp37-none-linux_armv7l.whl
RUN python -m pip install keras
RUN python -m pip uninstall -y numpy
RUN python -m pip install numpy

ADD . . 
RUN mkdir temporal

ENTRYPOINT [ "python", "server.py" ]
