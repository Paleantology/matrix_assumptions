#!/bin/bash
#ref: http://mlandis.github.io/2016/06/09/bash-scripting-with-revbayes.html
nprocs=$1

strbin="$bin_dir/$2"
strtri="$tri_dir/$2"
procid=$2

# construct the command string
rbc="strbin = \"$strbin\";
     strtri = \"$strtri\";
     procid = \"$procid\";
     source(\"mcmc_arg.Rev\");"

# pipe the command into RevBayes, 
# note the param --bind-to none in order to avoid all mpi processes on the same set of cores
time mpirun -np $nprocs --bind-to none ~/rb-mpi <<< $rbc

