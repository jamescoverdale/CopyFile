import os.path
from sys import argv
script, source, dest = argv

def copyfile(source, dest, buffer_size=1024*1024):   
   
    if os.path.exists(dest):
        print "File %s already exists" % dest
        return
       
    if not os.path.exists(source):
        print "File %s doesnt exist" % source
        return
   
    if not hasattr(source, 'read'):
        source = open(source, 'rb')
    if not hasattr(dest, 'write'):
        dest = open(dest, 'wb')

    print "Start copy..."   
    while 1:
        copy_buffer = source.read(buffer_size)
        if copy_buffer:
            dest.write(copy_buffer)
        else:
            break

    source.close()
    dest.close()
    print "Finished!"

copyfile(source, dest)