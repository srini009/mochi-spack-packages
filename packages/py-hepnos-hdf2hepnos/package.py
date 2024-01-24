##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack.package import *
from spack import *


class PyHepnosHdf2hepnos(PythonPackage):
    """HDF2HEPnOS utility for HEPnOS"""

    homepage = "https://xgitlab.cels.anl.gov/sds/hep/hepnos-hdf2hepnos"
    url      = "https://xgitlab.cels.anl.gov/sds/hep/hepnos-hdf2hepnos.git"
    git      = "https://xgitlab.cels.anl.gov/sds/hep/hepnos-hdf2hepnos.git"

    version('develop', branch="master")
    version('master', branch="master")
    version('0.1', tag='v0.1')

    depends_on('python')
    depends_on('py-jinja2')
    depends_on('py-h5py')
