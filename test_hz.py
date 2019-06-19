#/usr/bin/python
from __future__ import print_function
import sys
import time
import rosbag
from sets import Set
import numpy as np
import subprocess, yaml
import xml.etree.ElementTree as ET
import os
import datetime as dt
import math 
import fractions
from fractions import Fraction

def round_to_1(x):
	return round(x, -int(math.floor(math.log10(abs(x)))))

def gcd(L):
	#return reduce(fractions.gcd, map(fractions.Fraction,L))
	return reduce(fractions.gcd, L)

def find_hz(bag_name):
	bag = rosbag.Bag(bag_name)
	bag_info = yaml.load(subprocess.Popen(['rosbag', 'info', '--yaml', bag_name], stdout=subprocess.PIPE).communicate()[0])
	bag_topic_dict = bag_info['topics']
	temp = []
	print(bag_topic_dict)
	for topic in bag_topic_dict:
		temp.append(topic['topic'])
	bag_topics = np.array(temp)
	print(bag_topics)
	hz_dict = dict.fromkeys(bag_topics)
	bag_hzs = dict.fromkeys(bag_topics)
	for topic in bag_topics:
		hz_dict[topic] = []
	for topic, msg, t in bag.read_messages():
		temp = hz_dict[topic]
		temp.append(t)
		#if(topic == "/user_input"):
		#	print(msg)
		# 	print(temp)
	bag.close()

	nanoavgs = []
	for topic in bag_topics:
		timelist = hz_dict[topic]
		i = 0
		temp = []
		for t in timelist:
			if(i < len(timelist)-1):
				diff = timelist[i+1]-timelist[i]
				temp.append(diff.secs  + diff.nsecs * 10**-9)
			i = i+1
		summation = np.sum(temp)
		try:
			avg = summation / len(temp)
		except:
			avg = 0.0
		if(math.isnan(avg)):
			avg = 0.0
		f_avg = Fraction(str(long(avg))).limit_denominator(100)
		
		print()
		print(topic + " " + str(avg))
		print("f_avg=" + str(f_avg) +"="+str(float(f_avg)))
		try:
			print("avg "+str(avg))
			r_avg = round_to_1(avg)
			print("round_to_1 avg "+str(r_avg))
		except Exception as e:
			print(e)
		print("avg="+str(summation)+"/"+str(len(temp))+"="+str(r_avg))
		if(math.isnan(r_avg)):
			avg = 0.0
		f_avg = Fraction(str(r_avg)).limit_denominator(1000)
		nanoavgs.append(f_avg)
		hz_dict[topic] = r_avg
	print()
	print(nanoavgs)
	gcd_ans = gcd(nanoavgs)
	print(type(gcd_ans))
	# 17230363332
	print("gcd("+str(nanoavgs)+")="+ str(gcd_ans)+"="+str(float(gcd_ans)))
	hz_dict['all'] = float(gcd_ans)
	print("done find_hz")
	print(hz_dict)
	return hz_dict

def main():
	print("begin test_hz")
	bag_name = sys.argv[1]
	print(bag_name)
	find_hz(bag_name)
	print("done main")


if __name__ == "__main__":
    # execute only if run as a script
    main()
