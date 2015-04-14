import os,sys,codecs

def has_rep(train_sens,dev_sens,test_sens,train_writer,dev_writer,test_writer):
	print 'checking for repeated sentences'
	sen_dic=dict()
	rep=0
	cnt=0
	for sen in train_sens:
		cnt+=1
		sen=sen.strip()
		if not sen:
			continue
		ls=sen.split('\n')
		ws=list()
		for l in ls:
			ws.append(l.split('\t')[1].strip())

		sentence=' '.join(ws)
		if sen_dic.has_key(sentence):
			print sentence
			rep+=1
			#return True
		else:
			sen_dic[sentence]=sen
			train_writer.write(sen+'\n\n')

	for sen in dev_sens:
		cnt+=1
		sen=sen.strip()
		if not sen:
			continue
		ls=sen.split('\n')
		ws=list()
		for l in ls:
			ws.append(l.split('\t')[1].strip())

		sentence=' '.join(ws)
		if sen_dic.has_key(sentence):
			print sentence
			rep+=1
			#return True
		else:
			sen_dic[sentence]=sen
			dev_writer.write(sen+'\n\n')

	for sen in test_sens:
		cnt+=1
		sen=sen.strip()
		if not sen:
			continue
		ls=sen.split('\n')
		ws=list()
		for l in ls:
			ws.append(l.split('\t')[1].strip())

		sentence=' '.join(ws)
		if sen_dic.has_key(sentence):
			print sentence
			rep+=1
			#return True
		else:
			sen_dic[sentence]=sen
			test_writer.write(sen+'\n\n')
	train_writer.flush()
	train_writer.close()
	dev_writer.flush()
	dev_writer.close()
	test_writer.flush()
	test_writer.close()
	print rep


train_sens=codecs.open(os.path.abspath(sys.argv[1]),'r',encoding='utf-8').read().split('\n\n')
dev_sens=codecs.open(os.path.abspath(sys.argv[2]),'r',encoding='utf-8').read().split('\n\n')
test_sens=codecs.open(os.path.abspath(sys.argv[3]),'r',encoding='utf-8').read().split('\n\n')
print len(train_sens),len(dev_sens),len(test_sens)

train_writer=codecs.open(os.path.abspath(sys.argv[1])+'.ref','w',encoding='utf-8')
dev_writer=codecs.open(os.path.abspath(sys.argv[2])+'.ref','w',encoding='utf-8')
test_writer=codecs.open(os.path.abspath(sys.argv[3])+'.ref','w',encoding='utf-8')

has_rep(train_sens,dev_sens,test_sens,train_writer,dev_writer,test_writer)