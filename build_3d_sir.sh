#!/bin/bash

echo "Copying files from mods to 3d_sir ..."
(cd mods; tar cf - .)|(cd 3d_sir; tar xvf -)
echo "Building 3d_sir"
cd 3d_sir
python setup.py install
echo Done
