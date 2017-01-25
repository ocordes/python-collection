#!/usr/bin/env python

from deco_debug import *

import os, sys


@Ddebug
def test_func1( x, y, z ):
    print( x, y, z )

    return x+y, x*z

@Ddebug
def test_func2( x, y, z=1 ):
    print( x, y, z )


class Demo( object ):
    def __init__( self, x, y, z=1 ):
        self._x = x
        self._y = y
        self._z = z

    @Ddebug
    def add( self ):
        return self._x + self._y, self._x * self._z

# main

debug_init( 'debug.log')

print( 'Start ...' )

print( 'Normal calls ...' )

a,b = test_func1( 1, 2.0, 3.14 )
print( a, b )

test_func2( 1,2, z=2 )

print( 'Class calls ...' )

c = Demo( 1,2.0,z=3.14)

print( c.add() )


print( 'Done.' )
