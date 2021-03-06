from package import *

class shiboken(MakePackage):
    #dependencies=['apiextractor','generatorrunner']
    dependencies=['qt','libxml','libxslt','python','cmake']
    fetch="http://qt-project.org/uploads/pyside/shiboken-%(version)s.tar.bz2"
    modify_environ = {'PYSIDESANDBOXPATH':'%(prefix)s'}

    build_reldir = "build"
    config = "cmake .. -DCMAKE_INSTALL_PREFIX=%(prefix)s -DCMAKE_BUILD_TYPE=Release -DENABLE_ICECC=0"

