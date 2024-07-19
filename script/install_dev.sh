#!/bin/bash
#开发环境一键搭建安装脚本

conda create -n LAMC python=3.11 -y
conda activate LAMC
pip install -r requirements.txt
