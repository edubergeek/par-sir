#!/bin/bash

# add optarg code for
# number of worker threads *note add 1 for the master
# cubePath
# sirPath
# step include filter regex
# step exclude filter regex
# file prefix *default stokes-
# x and y range limits
# force flag to force preprocessing and synthesis

export NTHREAD=18

cubePath=./3D
ls $cubePath/subdomain_0.* | while read t
do
  step=${t##*.}
  echo $step
  sirPath=./3D-$step
  mkdir -p $sirPath
  for f in $cubePath/subdomain_*.$step
  do
    fname=`basename $f`
    ln -s $f $sirPath/$fname
  done
  #if [ ! -e $sirPath/rho.float ]
  #then
  #  echo "Preprocessing cube $step ..."
  #  python cube2sir.py $step --sirpath=$sirPath
  #fi

  if [ ! -e $sirPath/stokes-*.h5 ]
  then
    sed -e "s/##STEP##/$step/g" <synth.ini >$sirPath/synth.ini
    #echo "Synthesizing $step ..."
    #mpiexec -n 9 python synth.py --path=$sirPath -X 512 -W 256 -Y 512 -H 256
    #mpiexec -n $NTHREAD python synth.py --path=$sirPath
  fi
done
