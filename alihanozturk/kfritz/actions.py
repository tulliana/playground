#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr")

def build():
    cmaketools.make("LIBS=%s" % get.LDFLAGS())

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
