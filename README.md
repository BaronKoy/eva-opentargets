## README ##

[![Build Status](https://travis-ci.org/EBIvariation/eva-cttv-pipeline.svg?branch=master)](https://travis-ci.org/EBIvariation/eva-cttv-pipeline)
[![Coverage Status](https://coveralls.io/repos/github/EBIvariation/eva-cttv-pipeline/badge.svg?branch=master)](https://coveralls.io/github/EBIvariation/eva-cttv-pipeline?branch=master)


Minimum Python version needed: 3.5


Building and (optional) Setting up virtual environment
-------

1. "git clone --recursive git@github.com:EBIvariation/eva-cttv-pipeline.git"
2. "cd eva-cttv-pipeline"
3. [OPTIONAL] "virtualenv -p python3.5 venv"
4. [OPTIONAL] "source venv/bin/activate" ("venv/bin/deactivate" to deactivate virtualenv)
5. pip install -r requirements.txt
6. And then one of:
   * To install: "python3 setup.py install"
   * To install to develop: "python3 setup.py develop"
   * To build a source distribution: "python3 setup.py sdist"

To build the clinvar XML parser:
1. "cd clinvar-xml-parser"
2. "mvn package"
3. Two jar files will be generated in the 'target' directory, one of them including all the dependencies.  

Usage
-------

Please see the [GitHub wiki](https://github.com/EBIvariation/eva-cttv-pipeline/wiki/How-to-submit-an-OpenTargets-batch) for usage
