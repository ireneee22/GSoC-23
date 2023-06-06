# ** Errors I ran into while running multicore simulations ** 


- `mpiexec -n 4 nrniv -python -mpi init.py`

** Error message #1: **
     ~~~~
    (no such file, not in dyld cache), 'libmpi.dylib' (no such file), '/usr/local/lib/libmpi.dylib' (no such file), '/usr/lib/libmpi.dylib' (no such file, not in dyld cache)
    Is openmpi or mpich installed? If not in default location, need a LD_LIBRARY_PATH on Linux or DYLD_LIBRARY_PATH on Mac OS. On Mac OS, full path to a MPI library can be provided via environmental variable MPI_LIB_NRN_PATH
    could not dynamically load libmpi.so or libmpich.so
     ~~~~

To fix:
 *  not just activating env using its name, but also specifying path `source /path/bin/activate`
 * if MPI lib is in a non-default location: `export DYLD_LIBRARY_PATH="//path/to/mpi/lib:$DYLD_LIBRARY_PATH"`


** Error message #2: **
`FileNotFoundError: [Errno 2] No such file or directory: '/path/index.npjson'`

In this case I was trying to run the CA3 init.py from https://github.com/suny-downstate-medical-center/netpyne/tree/development/examples/CA3model_3pops/src folder. As `index.npjson` was not in this folder, moving it from `CA3model_3pops` to `src` fixed the error. 