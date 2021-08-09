#!/bin/bash

step=$1
cubePath=${2:-.}

if test ! -e ${cubePath}/subdomain_0.${step}
then
  echo Cube step $step not found at in ${cubePath}
  exit 1
fi

echo Path $cubePath
echo Step $step
ls $cubePath/*.$step

sed -e "s@##STEP##@$step@g" -e "s@##PATH##@$cubePath@g" <synth.ini >$cubePath/synth-$step.ini
cat $cubePath/synth-$step.ini

cat <<EOF

To synthesize the entire cube run the following commands:

cd $cubePath
mpiexec -n 18 python `pwd`/synth.py --init=synth-$step.ini
EOF

