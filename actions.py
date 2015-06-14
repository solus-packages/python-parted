#!/usr/bin/python


from pisi.actionsapi import pythonmodules, pisitools


def build():
    pythonmodules.compile()


def install():
    pythonmodules.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "BUGS", "COPYING")
