from spack import *


class MochiSymbiomon(CMakePackage):
    """SYMBIOMON is a Mochi microservice designed to capture and export metrics in 
    time-series data format over RDMA. It is primarily intended for remote-monitoring
    purposes."""

    homepage = "https://github.com/srini009/symbiomon"
    url = "https://github.com/srini009/symbiomon"
    git='https://github.com/srini009/symbiomon.git'

    version('develop', branch='master')

    variant('aggregator', default=False, description='Aggregate time-series data')
    variant('reducer', default=False, description='Reduce time-series data')
    variant('bedrock', default=False, description='Enable building of the bedrock module')

    depends_on('libuuid')
    depends_on('mochi-margo@0.9.5')
    #depends_on('argobots@main')
    depends_on('argobots@1.0:')
    depends_on('mochi-sdskv@develop-test', when='+aggregator')
    depends_on('mochi-abt-io@develop')
    depends_on('mochi-bedrock@0.3:', when='+bedrock')
    depends_on('mochi-reducer@develop', when='+reducer')

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS:BOOL=ON -DENABLE_EXAMPLES=ON" ]
        if '+aggregator' in self.spec:
            args.append('-DENABLE_AGGREGATOR=ON')
        if '+reducer' in self.spec:
            args.append('-DENABLE_REDUCER=ON')
        if '+bedrock' in self.spec:
            args.append('-DENABLE_BEDROCK=ON')
        return args
