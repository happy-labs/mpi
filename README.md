# MPI matrix multiplication
Multiply matrix via mpi, master devide matrix into sub parts and distribute it
slaves, slaves do matrix multiplication and retun the result back to master  

Master finally assemble the returing result from slaves and generates final
matrix 

## Packages to be install

### mpi for mac
```
brew install openmpi
```

### python libraries 
```
pip install mpi4py   
pip install numpy 
```

## How to run

### multiple process via mpi
```
mpiexec -n <no of processes> python multi_proces_multiplier.py   
mpiexec -n 4 python multi_process_multiplier.py
```

### single process 
```
python signle_process_multiplier.py
```
