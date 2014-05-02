==================================
simpletail - Read a file backwards
==================================

Before we go into technical details, a note about the license: It's
GPLv3. This practically means that if you use this module, your
program needs to be GPLv3. Sorry about that.

Briefly, the following will print ``my_file`` backwards::

   import sys

   from simpletail import ropen

   with ropen('my_file') as f:
       for line in f:
           sys.stdout.write(line)

It will work on Unix. It will work on Windows. On Python 2 and 3. It
will work regardless what kind of line endings you have. It should
work with any file encoding (but you need to specify an encoding, see
below), but I'm not certain about that; if in your encoding there are
multibyte characters that contain the bytes ``\n`` or ``\r``, it will
probably not work.

Reference
=========

::

   ropen(file, bufsize=4096, encoding=None, errors=None,
         newline=None, closefd=True)

``ropen()`` returns a file object.  *file* is usually a file name, but
in Python 3 it can be anything ``open()`` accepts as a first argument
(however wrapping files opened in text mode will probably not work).
The file is read from the end in chunks of size *bufsize*. The rest of
the arguments have the meaning they have in the ``open()`` built-in
function of Python 3, but they will also work in Python 2, with the
exception of *closefd*, which is ignored in Python 2.

License
=======

Written by Antonis Christofides.

Copyright (C) 2014 TEI of Epirus

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
