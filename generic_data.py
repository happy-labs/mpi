from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

num = 5

if rank == 1:
    print('process 1', num)
    comm.send(10, dest=0, tag=1)
    comm.send(20, dest=0, tag=2)
elif rank == 0:
    print('process 0 before', num)
    data = comm.recv(source=1, tag=1)
    print('process 0 after', data)
    data = comm.recv(source=1, tag=2)
    print('process 0 after', data)
