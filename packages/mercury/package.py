# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.builtin.mercury import Mercury as BuiltinMercury

class Mercury(BuiltinMercury):

    git = 'https://github.com/mercury-hpc/mercury.git'

    # note that these may be duplicated upstream; we repeat them here to
    # make sure that newer versions of Mercury are available for people on
    # older spack releases

    # Note that 2.2.0rc1 is available but we are marking the previous full
    # release (2.1.0) as preferred for now.  2.2.0rc1 is just for testing
    # and development purposes right now.
    version('2.2.0rc1', sha256='a14e4da68828da6b6914471b9775ecbfa33efdfb6923f1e956b17ce8f6ebfedb')
    version('2.1.0', sha256='9a58437161e9273b1b1c484d2f1a477a89eea9afe84575415025d47656f3761b', preferred=True)
    version('2.0.1', sha256='335946d9620ac669643ffd9861a5fb3ee486834bab674b7779eaac9d6662e3fa')
    version('2.0.0',
           sha256='9e80923712e25df56014309df70660e828dbeabbe5fcc82ee024bcc86e7eb6b7')
    version('develop', git='https://github.com/srini009/mercury.git', branch='pvar_interface')
    version('master-ucx', branch='ucx', submodules=True)

    variant('ucx', default=False, description='Use UCX plugin')
    variant('psm2', default=False, description='Use PSM2 plugin')

    depends_on('ucx', when='+ucx')
    depends_on('opa-psm2', when='+psm2')

    def cmake_args(self):
        args = super(Mercury, self).cmake_args()
        spec = self.spec
        variant_bool = lambda feature: str(feature in spec)
        args.append('-DNA_USE_UCX:BOOL=%s' % variant_bool('+ucx'))
        args.append('-DNA_USE_PSM2:BOOL=%s' % variant_bool('+psm2'))
        return args
