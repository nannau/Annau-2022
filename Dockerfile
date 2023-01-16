FROM  nvcr.io/nvidia/pytorch:22.01-py3

COPY ./ /workspace/

# Install Annau-2022 paper code
RUN pip3 install -r /workspace/requirements.txt
RUN pip3 install -e /workspace/.

RUN pip3 install jupyter -U && pip3 install jupyterlab
# COPY ./jupyter_notebook_config.py {JUPYTER_PATH}/jupyter_notebook_config.py

RUN apt-get -y update

RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install dvipng texlive-latex-extra texlive-fonts-recommended cm-super

EXPOSE 8888

# CMD ["jupyter", "lab","--ip=0.0.0.0",'--browser="none"',"--allow-root"]
ENTRYPOINT ["jupyter","lab","--ip=0.0.0.0",'--browser="none"',"--allow-root"]
