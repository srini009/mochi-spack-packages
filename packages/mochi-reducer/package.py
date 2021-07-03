from spack import *


class MochiReducer(CMakePackage):
    """REDUCER is a Mochi microservice designed to capture and export metrics in 
    time-series data format over RDMA. It is primarily intended for remote-monitoring
    purposes."""

    homepage = "https://github.com/srini009/reducer"
    url = "https://github.com/srini009/reducer"
    git='https://github.com/srini009/reducer.git'

    version('develop', branch='master')

    variant('aggregator', default=True, description='Aggregate time-series data')
    variant('bedrock', default=False, description='Enable building of the bedrock module')
    variant('symbiomon', default=False, description='Enable building of the symbiomon metric instrumentation module')

    depends_on('libuuid')
    depends_on('mochi-margo@develop')
    depends_on('mercury@master')
    #depends_on('argobots@main')
    depends_on('argobots@1.0:')
    depends_on('mochi-sdskv@develop-test', when='+aggregator')
    depends_on('mochi-abt-io@develop')
    depends_on('mochi-bedrock@develop', when='+bedrock')
    depends_on('mochi-symbiomon@develop', when='+symbiomon')

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS:BOOL=ON -DENABLE_EXAMPLES=ON" ]
        if '+aggregator' in self.spec:
            args.append('-DENABLE_AGGREGATOR=ON')
        if '+bedrock' in self.spec:
            args.append('-DENABLE_BEDROCK=ON')
        if '+symbiomon' in self.spec:
            args.append('-DENABLE_SYMBIOMON=ON')
        return args
