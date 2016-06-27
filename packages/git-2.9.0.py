from package import *

class git(Package):
    dependencies = ["perl","python",'openssl','zlib','curl']

    fetch="https://www.kernel.org/pub/software/scm/git/git-2.9.0.tar.gz"

    install="make PYTHON_PATH=%(prefix)s/bin/python NO_EXPAT=YesPlease NO_TCLTK=YesPlease PERL_PATH=%(prefix)s/bin/perl prefix=%(prefix)s all install"

