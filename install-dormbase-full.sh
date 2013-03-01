#!/bin/bash
git clone https://github.com/tboning/dormbase.git
cd /dormbase
git submodule init
git submodule update
# Initialize the database. This should be cleaned up.
cd dormbase
manage.py syncdb --migrate
manage.py plinit
100
100
yes
no
no
no
yes
130
175
yes
yes
no
0
0
no
yes
yes
no
cd ..
# Initialize the vEnv
sudo pip virtualenv
virtualenv  --prompt='(Dormbase) ' --python=python2.7 dormbase-env
source dormbase-env/bin/activate
# Needs requirement.txt in the dormbase github.
pip install -r requirement.txt
deactivate
