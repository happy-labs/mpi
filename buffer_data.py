from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
num_workers = comm.Get_size()

arr = numpy.array([[1,2,3,4],[5,6,7,8]])


if rank == 0:
    '''
    data = numpy.arange(10, dtype=int)
    arr = numpy.array_split(data, 3)
    comm.Send(arr[0], dest=1)
    comm.Send(arr[1], dest=2)
    comm.Send(arr[2], dest=3)
    '''
    comm.Send(arr[0], dest=1)
    comm.Send(arr[1], dest=2)

    data = numpy.empty(4, dtype=int)
    comm.Recv(data, source=1)
    print(data)
    comm.Recv(data, source=2)
    print(data)
else:
    data = numpy.empty(4, dtype=int)
    comm.Recv(data, source=0)
    print(data)
    print('-----------')
    comm.Send(data*2, dest=0)
