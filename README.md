# Annau-2022
Analysis and plots for Annau 2022 (in prep.)

# Data availability
Data is not stored on GitHub by default. A link to the pre-processed tensor files (~6GB) can be found here: [TO DO]

# A note about GPUs
I've developed this repo using a GPU. The results might work without one, and I've tried to enable this, but if you run into issues and don't have a GPU, please change the source code to meet your needs.

---

# Getting started

---

## Set Jupyter Password
To make accessing Jupyter Lab easier, I've enabled setting a Jupyter password as an environment variable on the host machine. However, please do not use this repo and assume it is secure. I am not a security expert. This repo is just to provide reproducibility to my results. Set a local environment variable as:

```bash
export JUPYTER_PASSWORD=password
```

You have a few options on how to get the repo working on your machine.

## From DockerHub [recommended]

```bash
docker image pull nannau/annau-2022-stable
```

Followed by 

```bash
docker run -p 8888:8888 --gpus all --ipc=host --network host --ulimit memlock=-1 --ulimit stack=67108864 -it -v $(pwd):/workspace/ --rm nannau/annau-2022-stable
```

---

## Docker Locally
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

Or go to `localhost:8888` and enter token from terminal output

