#!/usr/bin/env bash -l

source $CONDA_PREFIX/bin/activate
conda activate spark

export SPARK_HOME=${HOME}/spark
export PATH=$SPARK_HOME/bin:$PATH
