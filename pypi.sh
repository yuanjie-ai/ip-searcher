#!/usr/bin/env bash
python setup.py sdist bdist_wheel && twine upload ./dist/* # 2FA

pip install ./dist/*.whl -U
rm -rf ./build ./dist ./*.egg* ./.eggs
exit

#pip cache purge

# twine upload -r pypi dist/*
# twine upload -r pypitest dist/*

# vim ~/.pypirc
#[distutils] # this tells distutils what package indexes you can push to
#index-servers =
#  pypi
#  pypitest
#
#[pypi]
#repository: https://pypi.python.org/pypi
#username: myuser
#password: mypwd
#
#[pypitest]
#repository: https://testpypi.python.org/pypi
#username: myuser
#password: mypwd
