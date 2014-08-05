# Meditation
#
# This program allows you to program your own mind. It works by
# mixing in userdefined meditations with randomly generated characters. The
# concept is that your brain will recognize the pattern. Many, many times.
 
import os, random, time
 
def lucid(meditation):
    for i in xrange(0, 30000):
        time.sleep(.125)
        print os.urandom(256), meditation, os.urandom(random.randint(0, 256)).replace("?", "x")

 
if __name__ == '__main__':
    meditation = raw_input("Enter your meditation: ")
    lucid(meditation)
	