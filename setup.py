from distutils.core import setup

setup(name = "id3reader",
      version = "1.53.20070415",
      description = "Python module that reads ID3 metadata tags in MP3 files",
      author = "Ned Batchelder, Nik Reiman",
      packages = ['id3reader'],
      package_data = {'id3reader': ["id3reader/*"]}
)
