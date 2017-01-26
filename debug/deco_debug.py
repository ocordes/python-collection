#!/usr/bin/env python

# written by: Oliver Cordes 2017-01-20
# changed by: Oliver Cordes 2017-01-23


# Copyright (C) 2917 Oliver Cordes
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# The GNU General Public License is a free, copyleft license for software aon follow.


import sys, datetime

import atexit


# internal variables
logger = sys.stdout

# debug_goodbye is called when the program ends
#
# using a decorator for simplifying
#
@atexit.register
def debug_goodbye():
    global logger

    if ( logger != sys.stdout ):
        dt = datetime.datetime.now()
        s = dt.strftime( '%Y-%m-%d %H:%M:%S ' ) + 'Logfile closed' + '\n'
        logger.write( s )
        logger.write( '--------------------------------------------------------------------------------\n' )
        logger.close()

# debug_init can be called to redirect the output to a file
#
def debug_init( filename ):
    global logger

    logger = open( filename, 'a')
    dt = datetime.datetime.now()
    s = dt.strftime( '%Y-%m-%d %H:%M:%S ' ) + 'Logfile opened' + '\n'
    logger.write( s )

# print_debug is a helper function to write debug messages into the
# output stream
#
def _print_debug( s ):
    dt = datetime.datetime.now()
    s = dt.strftime( '%Y-%m-%d %H:%M:%S ' ) + s + '\n'
    logger.write( s )


def Ddebug( func ):

    def inner( *args, **kwargs):

        _print_debug( 'call function: %s' % func.__name__ )

        pos = 1
        _print_debug( ' fixed arguments:')
        for i in args:
            val = i.__repr__()
            if ( val[0] == '<' ):
                # detect a self arguments
                s = val[1:].split( ' ')
                val = 'self argument of class: '+s[0]
            _print_debug( '  arg %3i : %s' % ( pos, val ))
            pos += 1

        if ( ( kwargs is not None ) and ( len( kwargs.keys() ) > 0 )):
            _print_debug( ' free arguments: ')
            for key in kwargs.keys():
                _print_debug( '  %s == %s' %(key, kwargs[key] ) )

        # call original function
        ret = func( *args, **kwargs) #2

        # print return values, if any
        if ret is not None:
            _print_debug( ' return values:' )
            pos = 1
            for i in ret:
                _print_debug( '  val %3i : %s' % ( pos, i ) )
                pos += 1

        return ret


    return inner




# main

if __name__ == "__main__":

    debug_init( 'debug.log' )

    @Ddebug
    def test_func1( x, y, z ):
        print( x, y, z )

        return x+y, x*z

    @Ddebug
    def test_func2( x, y, z=1 ):
        print( x, y, z )



    a,b = test_func1( 1, 2.0, 3.14 )
    print( a, b )

    test_func2( 1,2, z=2 )
