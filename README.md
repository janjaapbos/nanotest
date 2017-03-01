# nanotest
Testing nanomsg


First install nanomsg:
https://github.com/nanomsg/nanomsg

Then continue below.

```
pip install virtualenv
virtualenv env
. env/bin/activate
pip install nnpy pyinstaller service sqlalchemy
cd modules/nanoservice
python setup.py install
cd ../oi
python setup.py install
cd ../apscheduler
python setup.py install

```
