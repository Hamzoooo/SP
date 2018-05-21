import sys
import psutil
pid=int(sys.argv[1])

p = psutil.Process(pid)
print "pid is {0}".format(p.pid)
print "name is {0}".format(p.name())
print "status is {0}".format(p.status())
print "Parent id is {0}".format(p.ppid())
print "parent name is {0}".format(p.parent())
print "process creation time is {0}".format(p.create_time())
print "files opened are {0}".format(p.open_files())
print "memory info is {0}".format(p.memory_info())
