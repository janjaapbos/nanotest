# nanotest
Testing nanomsg


For Alpine:
Link /usr/local/lib to /usr/local/lib64, or better fix how cffi finds the nanomsg library in /usr/local/lib64. ;-)

apk --update --no-cache add cmake alpine-sdk python-dev libffi-dev py2-pip

Set the time zone, e.g. UTC, like:
https://wiki.alpinelinux.org/wiki/Setting_the_timezone

First install nanomsg:
```
https://github.com/nanomsg/nanomsg
```

Create virtualenv
```
pip install virtualenv
virtualenv env
. env/bin/activate
pip install --upgrade pip
```

For Alpine build custom pyinstaller
(see https://github.com/gliderlabs/docker-alpine/issues/48 and
https://github.com/six8/pyinstaller-alpine)
```
cat <<EOM >env/bin/ldd
#!/bin/sh

# From http://wiki.musl-libc.org/wiki/FAQ#Q:_where_is_ldd_.3F
#
#     Musl's dynlinker comes with ldd functionality built in. just create a
#     symlink from ld-musl-$ARCH.so to /bin/ldd. If the dynlinker was started
#     as "ldd", it will detect that and print the appropriate DSO information.
#
# Instead, this string replaced "ldd" with the package so that pyinstaller
# can find the actual lib.
exec /usr/bin/ldd "$@" | \
    sed -r 's/([^[:space:]]+) => ldd/\1 => \/lib\/\1/g' | \
    sed -r 's/ldd \(.*\)//g'
EOM
chmod a+x env/bin/ldd

# PyInstaller needs zlib-dev, gcc, libc-dev, and musl-dev
apk --update --no-cache add \
    zlib-dev \
    musl-dev \
    libc-dev \
    gcc \
    git \
    pwgen

# Install pycrypto so --key can be used with PyInstaller
pip install pycrypto

# Build bootloader for alpine
git clone https://github.com/pyinstaller/pyinstaller.git tmppyinstaller \
    && cd tmppyinstaller/bootloader \
    && python ./waf configure --no-lsb all \
    && pip install .. \
    && cd ../..
    && rm -Rf tmppyinstaller
```

For other distri use generic pyinstaller
```
pip install pyinstaller
```

Install other packages
```
pip install cffi  nnpy service sqlalchemy

cd modules/nanoservice
make install
cd ../oi
make install
cd ../apscheduler
python setup.py install
```
