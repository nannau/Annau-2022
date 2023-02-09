# Annau, Cannon, and Monahan 2023

## Quick start

Analysis and plots for [the paper]() (in prep.)

[Docker Hub Image](https://hub.docker.com/r/nannau/annau-2023) analysis+data+environment

[![Docker Pulls](https://badgen.net/docker/pulls/trueosiris/godaddypy?icon=docker&label=pulls)](https://hub.docker.com/r/nannau/annau-2023)
[![Docker Stars](https://badgen.net/docker/stars/trueosiris/godaddypy?icon=docker&label=stars)](https://hub.docker.com/r/nannau/annau-2023)
[![Docker Image Size](https://badgen.net/docker/size/trueosiris/godaddypy?icon=docker&label=image%20size)](https://hub.docker.com/r/nannau/annau-2023)

Analysis only

[![DOI](https://zenodo.org/badge/584905308.svg)](https://zenodo.org/badge/latestdoi/584905308)

Data only

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7604278.svg)](https://doi.org/10.5281/zenodo.7604278)

## Data availability
Data is not stored on GitHub because of repo size limits. Therefore, the analysis code and data are hosted separately. However, an image with the analysis code and data is hosted on Docker Hub in an isolated PyTorch environment. Instructions for use are below, and I recommend using the docker image. If you decide you want to build the Docker image yourself, you can find the entire repo plus data hosted by Zenodo with its own DOI (the Data only DOI).
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7604278.svg)](https://doi.org/10.5281/zenodo.7604278)


## Requirements
* [Docker](https://docs.docker.com/engine/install/)
* [NVidia Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

## Getting started

You have a few options on how to get the repo working on your machine. I recommend using the docker image from Docker Hub because it includes the relevant dataset, and requires the least configuration to reproduce our results.


## From Docker Hub [recommended]

The most recent stable version is tagged `latest`.

```bash
docker run -p 8888:8888 --gpus all --ipc=host --network host --ulimit memlock=-1 --ulimit stack=67108864 -it --rm nannau/annau-2023:latest
```

The default password is set to `annau2023`. 

---

## Docker Locally

#### Set Jupyter Password
If building the docker image locally, to make accessing JupyterLab easier, I've enabled setting a Jupyter password as an environment variable on the host machine. Set a local environment variable as:

```bash
export JUPYTER_PASSWORD=password
```

#### Clone this repo and cd into it

Build docker locally using docker compose with:

```bash
docker compose up --build
```
---
## Without Docker Locally
```bash
python3 -m venv myvenv
```
```bash
source myvenv/bin/activate
```
```bash
pip install -e .
```
```bash
pip install -r requirements.txt
```
```bash
jupyter lab
```

## Accessing Jupyter Lab
Each option will run a Jupyter Lab server. The process to connect may change for each:

Using Docker, go to [localhost:8888](http://localhost:8888) and enter `annau2023` as the password. 

## A quick word on security
Please do not use this repo and assume the Jupyter Lab instance running on Docker is secure. I am not a security expert! This repo is intended only to reproduce our results so use it responsibly and don't run it publicly without taking percautions.

## A note about GPUs
I can't guarantee that this code will run on all hardware.

I've developed this repo using a GPU. The results might work without one, and I've tried to enable this, but if you run into issues and don't have a GPU, please change the source code to meet your needs (i.e. make sure the PyTorch tensors are loaded onto the CPU instead of the GPU). CPU will be much slower. 

