import os,sys,codecs

def trav(rev_head,h,visited):
	if rev_head.has_key(h):
		for d in rev_head[h]:
			if d in visited:
				return True
			visited.append(d)
			trav(rev_head,d,visited)
	return False

def has_loop(sens):
	print 'checking for repeated sentences'
	sen_dic=dict()
	rep=0
	cnt=0
	
	for sen in sens:
		cnt+=1
		if cnt%1000==0:
			sys.stdout.write(str(cnt)+'...')
		sen=sen.strip().replace('\r','')
		if not sen:
			continue
		ls=sen.split('\n')
		hd=dict()
		rev_head=dict()
		i=1
		for l in ls:
			if len(l.split('\t'))<7:
				print len(l.split('\t'))
				print l
				print l.split('\t')
				continue
			h=int(l.split('\t')[6].strip())
			hd[i]=int(h)
			if not rev_head.has_key(h):
				rev_head[h]=list()
			rev_head[h].append(i)
			i+=1

		visited=list()
		#print rev_head
		if trav(rev_head,0,visited):
			print sen
		if len(visited)<len(ls):
			print sen


	sys.stdout.write('\n')



sens=codecs.open(os.path.abspath(sys.argv[1]),'r',encoding='utf-8').read().split('\n\n')
print len(sens)
#sen_writer=codecs.open(os.path.abspath(sys.argv[1])+'.ref','w',encoding='utf-8')

has_loop(sens)