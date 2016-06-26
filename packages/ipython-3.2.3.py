from package import *

class ipython(EasyInstallPackage):
    dependencies = ["readline","nose", "pexpect", "pyzmq", "pygments"]

    install="""
            easy_install http://archive.ipython.org/release/3.2.3/ipython-3.2.3.tar.gz
            """
