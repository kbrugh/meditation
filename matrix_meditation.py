# Matrix Modelling, Meditation, & Motivation
#	Prototype August 2014
#
# This program allows you to program your own mind. It works by
# mixing in userdefined meditations with randomly generated characters. The
# concept is that your brain will recognize the pattern. Many, many times.
#
# The print rate coding allows a mechanism to set a specifc target brainwave frequency.

 
import os, random, time
 
def lucid(meditation):
    for i in xrange(0, int(timemax)):
        time.sleep(delay)
        print os.urandom(256), meditation, os.urandom(random.randint(0, 256))

 
if __name__ == '__main__':
    meditation = raw_input("Enter meditation: ")
    Hz = float(raw_input("Enter brainwave frequency, in Hz: "))
    timer = int(raw_input("Enter time, in minutes: "))
    delay = 1 / Hz
    timemax = ((timer * 60) / (1 / Hz))
    lucid(meditation)
	
# Next To Do:
'''
-Select new data into the matrix. Thinking about a flow (time.date?) 
-Add auditory tones
-test and ensure bitrate and frequency --- close enough! - at 10 Hz, the avg error is .72ms or .00072 seconds 
-Wanting to add a range shifting function that can move from an initial Hz to a target resulting Hz.
-Make it hosted on the internet
-Incentives?
-Stimulation and relaxation - arousal levels in balance, specific for the context
-Language considerations: use simple meditations with nouns, verbs, and adjectives'''
