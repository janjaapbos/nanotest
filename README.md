# nanotest
Testing nanomsg


First install nanomsg:
https://github.com/nanomsg/nanomsg

For Alpine:
Create links in /usr/local/lib for nanomsg from /usr/local/lib64, or better fix how cffi finds the nanomsg library in /usr/local/lib64. ;-)

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
