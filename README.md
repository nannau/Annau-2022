[![DOI](https://zenodo.org/badge/584905308.svg)](https://zenodo.org/badge/latestdoi/584905308)

# Annau, Cannon, and Monahan 2023

Analysis and plots for [the paper]() (in prep.)

## Data availability
Data is not stored on GitHub because of repo size limits. However, an image with the data is hosted on Dockerhub . If you decide you want to build the Docker image yourself, you can find the entire repo plus data hosted by Zenodo with its own DOI. 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7604278.svg)](https://doi.org/10.5281/zenodo.7604278)


## A note about GPUs
I can't guarantee that this code will run on all hardware.

I've developed this repo using a GPU. The results might work without one, and I've tried to enable this, but if you run into issues and don't have a GPU, please change the source code to meet your needs.

# Getting started

You have a few options on how to get the repo working on your machine. I recommend using the docker image from Dockerhub because it includes the relevant dataset, and requires the least configuration to reproduce our results. Please do not use this repo and assume it is secure. I am not a security expert! This repo is intended only to provide reproducibility to my results so use it responsibly.

## From DockerHub [recommended]

```bash
docker run -p 8888:8888 --gpus all --ipc=host --network host --ulimit memlock=-1 --ulimit stack=67108864 -it --rm nannau/annau-2023:latest
```

The default password is set to `annau2023`. 

---

## Docker Locally

## Set Jupyter Password
If building the docker image locally, to make accessing JupyterLab easier, I've enabled setting a Jupyter password as an environment variable on the host machine. Set a local environment variable as:

```bash
export JUPYTER_PASSWORD=password
```

In GitHub repo main:

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
Each option will run a Jupyter Lab server. The process to connect is the same for each:

Copy the Jupyter Lab URL from the terminal output. Substitute `hostname` for `localhost`. 

Or go to `localhost:8888` and enter the token from the terminal output
