from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
num_workers = comm.Get_size() - 1

#arr = numpy.array([[1,2,3,4],[5,6,7,8]])
data = numpy.arange(12, dtype=int)
arr_size = data.size/num_workers


if rank == 0:
    arr = numpy.array_split(data, num_workers)
    i = 1
    for a in arr:
        comm.Send(a, dest=i)
        i = i + 1

    l = 1
    for n in range(num_workers):
        data = numpy.empty(arr_size, dtype=int)
        comm.Recv(data, source=l)
        print(data)
        l = l + 1

    '''
    data = numpy.empty(4, dtype=int)
    comm.Recv(data, source=1)
    print(data)
    comm.Recv(data, source=2)
    print(data)
    '''
else:
    data = numpy.empty(arr_size, dtype=int)
    comm.Recv(data, source=0)
    print(data)
    print('-----------')
    comm.Send(data*2, dest=0)
