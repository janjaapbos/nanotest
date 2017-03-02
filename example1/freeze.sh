#!/bin/sh

rm -rf build dist
pyinstaller --hidden-import cffi example1/example1.py

cp example1/config.py dist/example1/config.py
cp example1/scheduler.py dist/example1/scheduler.py

cd dist/example1
ln -s example1 example1d
ln -s example1 example1svc
ln -s example1 example1ctl
cd ../../
