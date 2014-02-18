#!/usr/bin/env python

from distutils.core import setup


setup (name="pynolh",
       version="0.1",
       author="Francois-Michel De Rainville",
       author_email="f.derainville@gmail.com",
       license="LICENSE.txt",
       description="Nearly Orthogonal Latin Hypercube Generator",
       long_description=open("README.md").read(),
       url='https://github.com/fmder/pynolh',
       download_url="https://github.com/fmder/pynolh/downloads",
       classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Topic :: Scientific/Engineering',
        ],
       install_requires=["numpy",],
       py_modules=["pynolh"],
       )
