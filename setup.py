#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import os, sys
from setuptools import setup, find_packages
from distutils.extension import Extension
import logging
import subprocess
from distutils.command.install import install
from distutils.command.build import build
from distutils.command.clean import clean

name = find_packages().pop()
NEM_dir_path = name+"/NEM/"

# print(NEM_dir_path)
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == "__main__":

    setup(
        name = name,
        version = read("VERSION").rstrip(),
        author = "Guillaume GAUTREAU",
        author_email = "ggautrea@genoscope.cns.fr",
        description = "Depict microbial diversity via a partitioned pangenome graph",
        license = "CeCILL-2.1",
        keywords = "pangenome comparative-genomics bioinformatics microbiology",
        url = "https://github.com/ggautreau/PPanGGOLiN",
        packages=[name],
        long_description=read('README.rst'),
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)",
            "Natural Language :: English",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Scientific/Engineering :: Bio-Informatics",
       ],
        entry_points={
            'console_scripts': [
            name+' = '+name+'.command_line:__main__'
          ]},
        setup_requires = ['cython'],
        install_requires= ['chart-studio', 'ordered-set', 'bidict', 'networkx >= 2.0' , 'tqdm', 'ascii_graph','scipy','numpy','pandas','fa2','markov_clustering', 'colorlover'],
        ext_modules = [Extension(name = "nem_stats",sources =[NEM_dir_path+'nem_stats.pyx',
                                                                        NEM_dir_path+'nem_exe.c',
                                                                        NEM_dir_path+'nem_alg.c',
                                                                        NEM_dir_path+'nem_nei.c',
                                                                        NEM_dir_path+'nem_mod.c',
                                                                        NEM_dir_path+'nem_rnd.c',
                                                                        NEM_dir_path+'lib_io.c',
                                                                        NEM_dir_path+'nem_hlp.c',
                                                                        NEM_dir_path+'genmemo.c'],
                                                              include_dirs=[NEM_dir_path])]
)
