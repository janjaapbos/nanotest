# nanotest
Testing nanomsg


For Alpine:
Link /usr/local/lib to /usr/local/lib64, or better fix how cffi finds the nanomsg library in /usr/local/lib64. ;-)

apk add cmake alpine-sdk python-dev libffi-dev py2-pip

Set the time zone, e.g. UTC, like:
https://wiki.alpinelinux.org/wiki/Setting_the_timezone

First install nanomsg:
https://github.com/nanomsg/nanomsg

Then continue below.

```
pip install virtualenv
virtualenv env
. env/bin/activate
pip install cffi  nnpy pyinstaller service sqlalchemy
cd modules/nanoservice
make install
cd ../oi
make install
cd ../apscheduler
python setup.py install

```
