# Packages to be install

## mpi for mac
brew install openmpi

## mpi for python
pip install mpi4py
pip install numpy 

# run
mpiexec -n 4 python matrix_multiplication.py
