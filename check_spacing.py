# -*- coding: utf8
import os,sys,codecs
from collections import defaultdict

reader=codecs.open(os.path.abspath(sys.argv[1]),'r',encoding='utf8')
writer=codecs.open(os.path.abspath(sys.argv[2]),'w',encoding='utf8')

line=reader.readline()
while line:
	line=line.strip()
	if line:
		spl=line.split('\t')
		output=list()
		x=False
		for s in spl:
			s=s.strip()
			if spl[3]!='V':
				
				if ' ' in s:
					print s
					x=True
				s=s.replace(' ','\u200C')
				s=s.replace('\u200C\u200C','\u200C')
				if x:
					print s
			output.append(s)
		if x:
			print '\t'.join(output)
		writer.write('\t'.join(output)+'\n')
	else:
		writer.write(line+'\n')
	line=reader.readline()

writer.flush()
writer.close()
