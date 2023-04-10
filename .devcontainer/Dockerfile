FROM nvidia/cuda:11.8.0-devel-ubuntu22.04 as llr_base

RUN apt-get update && apt-get -y install cmake git rust-all wget curl

RUN curl micro.mamba.pm/install.sh | bash

COPY scripts /build/legate.core/scripts

WORKDIR /build/legate.core

RUN scripts/generate-conda-envs.py --python 3.10 --ctk 11.8 --os linux --compilers --openmpi

ENV PATH="/root/.local/bin:$PATH"

RUN micromamba env create -n legate -f environment-test-linux-py3.10-cuda11.8-compilers-openmpi.yaml

SHELL ["/bin/bash", "--login", "-c"]

RUN micromamba shell init -s bash -p ~/micromamba

# Make sure pynvml is installed
RUN micromamba run -n legate /bin/bash -c "python -c \"import pynvml\""


