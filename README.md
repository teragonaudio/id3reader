About Id3reader
===============
Id3reader.py is a Python module that reads ID3 metadata tags in MP3 files.  It can read ID3v1, ID3v2.2, ID3v2.3, or ID3v2.4 tags.  It does not write tags at all.

Id3reader.py was originally written by [Ned Batchelder](http://nedbatchelder.com/).  In November 2010, [Nik Reiman](http://www.nikreiman.com) took over maintainence of the codebase and ported it to Python 3.  The original code (and last Python 2.x compatible version) can be found in the [1.0 tag](https://github.com/nikreiman/id3reader/tree/1.0).  All changes after this point cannot be guaranteed to be compatible with Python 2.x.

Installation
------------
To install id3reader, just copy id3reader.py to your Python path.

Usage
-----
Using id3reader couldn't be simpler:

import id3reader

    # Construct a reader from a file or filename.
    id3r = id3reader.Reader('my_favorite.mp3')

    # Ask the reader for ID3 values:
    print id3r.getValue('TT2')

In addition to whatever literal ID3 tag ids are found in the file (TP1, TIT2, etc), id3reader defines five pseudo-ids for convenience:

    id3r.getValue('album')
    id3r.getValue('performer')
    id3r.getValue('title')
    id3r.getValue('track')
    id3r.getValue('year'

These ids find the appropriate ID3 id for the ID3 version read from the file, so you can get at this basic data without having to consider the different versions of the ID3 spec.

If you run id3reader from the console, it will dump the ID3 information for the MP3 file named as its argument.

Coverage
--------
The ID3 spec is quite extensive, and specifies functionality that I have never encountered in actual MP3 files. Id3reader implements as much of the spec as I have seen used. If you have files that id3reader does not properly interpret, please mail them to me. I'll extend id3reader to read them.

History
-------
* 5 January 2004: It wasn't reading ID3v1 tags properly, and had problems with empty string values.
* 9 January 2004: Now it reads ID3v2.3 properly, and reads unsyncronized tags.
* 13 January 2004: Fix unsynchronized reading, reads compressed frames, improved detection of end of frames, extended headers are read (but not interpreted), multi-string frames are interpreted, and the file is closed if we opened it.
* 3 August 2004: Add support for genres (although they're stupid), and the command-line mode will print strings regardless of their encoding.
* 13 September 2004: Better protection against non-character data when showing the data on the command line.
* 6 November 2010: Now compiles under Python 3
* 13 November 2010: Project moved to github under new maintainer; all changes after this point are listed on the project's github page.
