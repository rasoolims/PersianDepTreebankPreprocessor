import os,sys,codecs

if len(sys.argv)<5:
	print 'python split2train_dev_test.py [main_conll] [train-path] [dev-path] [test-path]'
	sys.exit(0)

sens=codecs.open(os.path.abspath(sys.argv[1]),'r').read().strip().split('\n\n')

l=len(sens)

f1=int(l-float(l)*0.2)
f2=int(l-float(l)*0.1)

print f1,f2,l

codecs.open(os.path.abspath(sys.argv[2]),'w').write('\n\n'.join(sens[:f1]))
codecs.open(os.path.abspath(sys.argv[3]),'w').write('\n\n'.join(sens[f1:f2]))
codecs.open(os.path.abspath(sys.argv[4]),'w').write('\n\n'.join(sens[f2:]))

print 'done!'