FROM  nvcr.io/nvidia/pytorch:22.01-py3

# Set bash as the default shell
ENV SHELL=/bin/bash

# Create a working directory
WORKDIR /workspace/
COPY ./ /workspace/

# Build with some basic utilities
RUN apt-get update && apt-get install -y \
    python3-pip \
    apt-utils \
    git 

# alias python='python3'
RUN ln -s /usr/bin/python3 /usr/bin/python

# Installs requirements
RUN pip install \
    numpy \
    torch \
    jupyterlab

RUN pip install -e /workspace/.
RUN pip install -r /workspace/requirements.txt

# Required for password management and customization
RUN jupyter notebook --generate-config
COPY ./jupyter_notebook_config.py ~/.jupyter/jupyter_notebook_config.py

# Required for LaTeX in plots
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install dvipng texlive-latex-extra texlive-fonts-recommended cm-super

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents
# kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

EXPOSE 8888
CMD ["jupyter", "lab", "--port=8888", "--no-browser", "--ip=0.0.0.0"]