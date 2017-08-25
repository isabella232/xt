xt
===

[![Build Status](https://travis-ci.org/mapbox/xt.svg?branch=master)](https://travis-ci.org/mapbox/xt) [![Coverage Status](https://coveralls.io/repos/github/mapbox/xt/badge.svg?branch=master)](https://coveralls.io/github/mapbox/xt?branch=master)

Automatically convert a stream of tile coordinates to another format

- `z/x/y | z-x-y` ==> `[x, y, z]`

- `[x, y, z]` ==> `z/x/y` | `z-x-y` | `z?x?y -d ?`


Installation
-------------
```
pip install xt
```
Or to develop:
```
git@github.com:mapbox/xt.git && cd xt && pip install -e '.[test]'
```

Examples
---------
Tile URL to [mercantile](https://github.com/mapbox/mercantile) `[x, y, z]`
```
» echo https://map.s/17/20971/5051.png | xt
[20971, 50651, 17]
```
mercantile to `z/x/y`
```
» echo '[0, 0, 0]' | xt
0/0/0
```
mercantile to `z-x-y`
```
» echo '[100, 100, 100]' | xt -d -
100-100-100
```
roundtripping
```
» pbpaste | xt | xt -d - | xt | xt | xt | xt -d | xt | xt 
17/20972/50653
```
