from spack import *


class STK(Package):
    """
    STK is a parallel aware finite element toolkit written by Manoj Bhardwaj.

    """
    homepage = "https://trilinos.org/packages/stk/"
    url = "https://github.com/trilinos/Trilinos"

    # Everything should be compiled with -fpic
    #depends_on('blas')
    #depends_on('lapack')
    depends_on('boost')
    depends_on('netcdf')
    depends_on('mpi')

    def install(self, spec, prefix):

        options = [
#            '-DBLAS_LIBRARY_DIRS:PATH=%s' % spec['blas'].prefix,
#            '-DLAPACK_LIBRARY_DIRS:PATH=%s' % spec['lapack'].prefix
        ]
        if '+mpi' in spec:
            mpi_options = ['-DTPL_ENABLE_MPI:BOOL=ON']
            options.extend(mpi_options)

        # -DCMAKE_INSTALL_PREFIX and all the likes...
        options.extend(std_cmake_args)
        with working_dir('spack-build', create=True):
            cmake('..', *options)
            make()
            make('install')
