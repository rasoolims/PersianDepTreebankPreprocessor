import os,sys,codecs


sens=codecs.open(os.path.abspath(sys.argv[1]),'r').read().split('\n\n')

ln=len(sens)

first_writer=codecs.open(os.path.abspath(sys.argv[2]),'w')
second_writer=codecs.open(os.path.abspath(sys.argv[3]),'w')

for i in range(0,ln/2):
	first_writer.write(sens[i].strip()+'\n\n')

for i in range((ln/2)+1,ln):
	second_writer.write(sens[i].strip()+'\n\n')

first_writer.flush()
first_writer.close()
second_writer.flush()
second_writer.close()