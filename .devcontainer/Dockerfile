FROM nvidia/cuda:11.8.0-devel-ubuntu22.04 as llr_base

RUN apt-get update && apt-get -y install cmake git rust-all wget
WORKDIR /app

ENV PATH="/root/miniconda3/bin:$PATH"

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    chmod +x Miniconda3-latest-Linux-x86_64.sh && \
    ./Miniconda3-latest-Linux-x86_64.sh -bf && \
    conda init bash

# FROM llr_base as llr_conda_env

# WORKDIR /app/legate.core

# COPY ../scripts ./scripts

# RUN ./scripts/generate-conda-envs.py --python 3.10 --ctk 11.8 --os linux --compilers --openmpi && \
#     conda env create -n legate -f environment-test-linux-py3.10-cuda11.8-compilers-openmpi.yaml
    
# RUN echo "conda activate legate" >> ~/.bashrc

# SHELL ["conda", "run", "-n", "legate", "/bin/bash", "-c"]

# # Demonstrate the environment is activated:
# RUN conda env list && \
#     echo "Make sure pynvml is installed:" && \
#     python -c "import pynvml"

# FROM llr_conda_env as legate.core

# WORKDIR /app
# COPY legate.core/ legate.core/

# WORKDIR /app/legate.core
# RUN ./install.py --cuda --march=nocona
