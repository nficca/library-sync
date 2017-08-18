# library-sync
A python program which syncs two directories such that it ensures the second is a copy of the first. 

### Try it yourself:
Make sure you have an installation of Python 3.X.

I recommend you [download the script](https://raw.githubusercontent.com/nficca/library-sync/master/library-sync.py) and save it in a folder in your path as `library-sync`.
Then you can simply run:
```
$ library-sync <master-directory> <copy-directory>
```
*Note: in order for this to work, `which python` should point to a `python3.x` executable*

If you'd like to clone the repo, you can do that too:
```
$ git clone https://github.com/nficca/library-sync && cd library-sync
$ python library-sync.py <master-directory> <copy-directory>
```

### Example:
Consider a directory structure like the following:
```
$ tree
.
├── copy
└── master
    ├── d1
    │   ├── f2.ini
    │   └── f3.py
    └── f1.txt

3 directories, 3 files
```
We can sync `master` and `copy` easily like so:
```
$ library-sync master/ copy/
Copying all of d1
Copying f1.txt
```
Which results in:
```
$ tree
.
├── copy
│   ├── d1
│   │   ├── f2.ini
│   │   └── f3.py
│   └── f1.txt
└── master
    ├── d1
    │   ├── f2.ini
    │   └── f3.py
    └── f1.txt

4 directories, 6 files
```
Nothing too fancy.

Say, however, that I make a change to `f2.ini` and add a new directory with some files to `master/d1`:
```
$ tree
.
├── copy
│   ├── d1
│   │   ├── f2.ini
│   │   └── f3.py
│   └── f1.txt
└── master
    ├── d1
    │   ├── d1a
    │   │   ├── f4.mp3
    │   │   └── f5.mp4
    │   ├── f2.ini
    │   └── f3.py
    └── f1.txt

5 directories, 8 files
```
Now if I run `library-sync`:
```
$ library-sync master/ copy/
Copying all of d1/d1a
Overwriting d1/f2.ini
```
It made only the necessary changes, and left everything else the same.

#### Warning
This is just something I am personally fiddling around with to ease the management of my music libraries. Don't flip out on me if you use this and things go wrong or don't work the way you'd expect. As such, **I recommend you to backup your files before using this.**
