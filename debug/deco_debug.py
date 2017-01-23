#!/usr/bin/env python

# written by: Oliver Cordes 2017-01-20
# changed by: Oliver Cordes 2017-01-20


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


def Ddebug( func ):

    def inner( *args, **kwargs):

        print( func.__name__ )
        print( args, kwargs )

        if kwargs is not None:
            for key in kwargs.keys():
                print( "%s == %s" %(key, kwargs[key] ) )

        # call original function
        ret = func( *args, **kwargs) #2

        # print return values, if any
        if ret is not None:
            print( 'return values:', ret )

        return ret


    return inner




# main

if __name__ == "__main__":

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
