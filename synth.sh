#!/bin/bash

step=$1
cubeDir=${2:-.}
waveLength=${3:-6302}
model=$4
batchTemplate=$5

if test -z "$model"
then
  cubePath=$cubeDir
else
  cubePath=$cubeDir/$model/3D
fi

if test ! -e ${cubePath}/subdomain_0.${step}
then
  echo Cube step $step not found at in ${cubePath}
  exit 1
fi

sirPath=`dirname $cubePath`/SIR
mkdir -p $sirPath
echo Path   $cubePath
echo Step   $step
echo Output $sirPath
ls $cubePath/*.$step

sed -e "s@##STEP##@$step@g" -e "s@##PATH##@$cubePath@g" -e "s@##WL##@$waveLength@g" -e "s@##$waveLength##@@g" -e "/##[0-9]*##/d" <synth.ini >$sirPath/synth-$step-$waveLength.ini
echo "3D SIR Configuration"
cat $sirPath/synth-$step-$waveLength.ini
echo

if test ! -z "$batchTemplate" && test ! -z "$model"
then
  batchPath=`dirname $batchTemplate`
  batchFile=$(basename -- "$batchTemplate")
  batchSuffix="${batchFile##*.}"
  batchPrefix="${batchFile%.*}"
  sed -e "s@##MODEL##@$model@g" -e "s@##STEP##@$step@g" -e "s@##PATH##@$cubePath@g" -e "s@##WL##@$waveLength@g" <$batchTemplate >$batchPath/$batchPrefix-$step-$waveLength.$batchSuffix
  echo "Batch Submission"
  cat $batchPath/$batchPrefix-$step-$waveLength.$batchSuffix
  echo
fi

cat <<EOF

To synthesize the entire cube run the following commands:

cd $sirPath
mpiexec -n 36 python `pwd`/synth.py --init=synth-$step-$waveLength.ini
EOF

