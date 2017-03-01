# nanotest
Testing nanomsg


First install nanomsg:
https://github.com/nanomsg/nanomsg

Then continue below.

For Alpine:
apk add alpine-sdk python-dev libffi-dev

```
pip install virtualenv
virtualenv env
. env/bin/activate
pip install cffi  nnpy pyinstaller service sqlalchemy
cd modules/nanoservice
python setup.py install
cd ../oi
python setup.py install
cd ../apscheduler
python setup.py install

```
