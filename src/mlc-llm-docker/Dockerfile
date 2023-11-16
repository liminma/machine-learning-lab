FROM nvidia/cuda:12.2.2-devel-ubuntu22.04

SHELL ["/bin/bash", "-ec"]

RUN apt-get update && apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    less \
    tree \
    vim \
    wget

ARG miniconda_installer=Miniconda3-py311_23.9.0-0-Linux-x86_64.sh

ENV PATH=/opt/miniconda3/bin:$PATH

RUN wget https://repo.anaconda.com/miniconda/$miniconda_installer && \
    bash ./$miniconda_installer -p /opt/miniconda3 -s -b && \
    conda install pytorch-cpu==2.1.0 git-lfs==3.4.0 safetensors==0.4.0 -n base -c conda-forge && \
    rm -f ./$miniconda_installer

RUN pip install --pre -f https://mlc.ai/wheels \
    mlc-ai-nightly-cu122 \
    mlc-chat-nightly-cu122

RUN git clone https://github.com/mlc-ai/mlc-llm.git /mlc-llm

WORkDIR /mlc-llm
