import os,sys,codecs

orig_sens=codecs.open(os.path.abspath(sys.argv[1]),'r').read().strip().split('\n\n')
new_sens=codecs.open(os.path.abspath(sys.argv[2]),'r').read().strip().split('\n\n')
writer=codecs.open(os.path.abspath(sys.argv[3]),'w')

sen_dict=dict()
for s in new_sens:
	x=s.split('\n')[0].split('\t')[5]
	number=int(x[x.find('senID=')+6:x.find('senID=')+11])
	sen_dict[number]=s.strip().split('\n')


for orig in orig_sens:
	x=orig.split('\n')[0].split('\t')[5]
	number=int(x[x.find('senID=')+6:x.find('senID=')+11])
	new_sen=sen_dict[number]

	output=list()
	i=0
	for l in orig.strip().split('\n'):
		try:
			x=new_sen[i].split('\t')[0:6]+l.split('\t')[6:]
		except:
			print i, len(new_sen)
			print number
			print new_sen
			print l
			sys.exit(0)
		output.append('\t'.join(x))
		i+=1

	writer.write('\n'.join(output).strip()+'\n\n')

writer.flush()
writer.close()
