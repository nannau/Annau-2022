# Annau-2022
Analysis and plots for Annau 2022 (in prep.)

# Data availability
Data is not stored on GitHub by default. A link to the pre-processed tensor files (~12GB) can be found here: [TO DO]

---

# Getting started

---

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
pip install -e 
.```
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

