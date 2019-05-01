# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM ubuntu:xenial-20181113

RUN apt -qqy update \
  && apt -qqy --no-install-recommends install \
    python3 \
    python3-pip \
    python3-dev \
    python3-openssl \
    libssl-dev libffi-dev \
  && pip3 install --no-cache --upgrade pip==9.0.3 \
  && pip3 install --no-cache setuptools \
  && pip3 install --no-cache numpy \
  && rm -rf /var/lib/apt/lists/* \
  && apt -qyy clean
RUN cd /usr/local/bin \
  && { [ -e easy_install ] || ln -s easy_install-* easy_install; } \
  && ln -s idle3 idle \
  && ln -s pydoc3 pydoc \
  && ln -s python3 python \
  && ln -s python3-config python-config \
  && ln -s /usr/bin/python3 /usr/bin/python \
  && python --version \
  && pip --version

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz \
    && tar -xvzf geckodriver-v0.23.0-linux64.tar.gz \
    && chmod +x geckodriver \
    && sudo mv geckodriver /usr/local/bin/



#RUN apt-get update && apt-get install build-essential

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=cybercolecatchingsystem Version=0.0.1
EXPOSE 3000
WORKDIR /app
ADD . /app

# Using pip:


RUN python3 -m pip install -r requirements.txt
CMD ["python3", "-m", "main.py"]

# Using pipenvv:
#RUN python3 -m pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "cybercolecatchingsystem"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m cybercolecatchingsystem"
