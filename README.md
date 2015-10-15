# Packages to be install

## mpi for mac
brew install openmpi

## mpi for python
pip install mpi4py   
pip install numpy 

# run

## multiple process via mpi
mpiexec -n <no of processes> python multi_proces_multiplier.py   
mpiexec -n 4 python multi_process_multiplier.py

## single process 
python signle_process_multiplier.py
