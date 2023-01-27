FROM ubuntu:18.04


RUN apt-get update
RUN apt-get install -y libpq-dev 
RUN apt-get install -y python3-dev 
RUN apt-get install -y python3-pip 
RUN apt-get install -y git 
RUN apt-get clean
RUN cd /opt && git clone https://github.com/Pavithratrdev/bst-visualizer.git
RUN cd /opt/bst-visualizer && git pull

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r /opt/bst-visualizer/requirements.txt

WORKDIR /opt/bst-visualizer

EXPOSE 5002
ENTRYPOINT [ "python3" ]
CMD [ "run.py" ]