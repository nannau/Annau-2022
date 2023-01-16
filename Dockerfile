FROM  nvcr.io/nvidia/pytorch:22.01-py3

# COPY ./ /workspace/

# # Install Annau-2022 paper code
# RUN pip install -r /workspace/requirements.txt
# RUN pip install -e /workspace/.

# RUN pip install jupyter -U && pip3 install jupyterlab
# # COPY ./jupyter_notebook_config.py {JUPYTER_PATH}/jupyter_notebook_config.py

# RUN apt-get -y update

# RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install dvipng texlive-latex-extra texlive-fonts-recommended cm-super

# EXPOSE 8888

# ENTRYPOINT ["jupyter","lab","--ip=0.0.0.0",'--browser="none"',"--allow-root"]


# FROM nvidia/cuda:11.8.0-base-ubuntu20.04

# Set bash as the default shell
ENV SHELL=/bin/bash

# Create a working directory
WORKDIR /workspace/
COPY ./ /workspace/

# Build with some basic utilities
RUN apt-get update && apt-get install -y \
    python3-pip \
    apt-utils \
    vim \
    git 

# alias python='python3'
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip install \
    numpy \
    torch \
    torchvision \
    torchaudio \
    jupyterlab

RUN pip install -e /workspace/.
RUN pip install -r /workspace/requirements.txt

RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install dvipng texlive-latex-extra texlive-fonts-recommended cm-super

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]
EXPOSE 8888