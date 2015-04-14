import os,sys,codecs

D={'ADJ':['AJP', 'AJCM','AJSUP'], 'ADR':['PRADR', 'POSADR'], 'ADV':['SADV'], 'CONJ':['CONJ'], 'IDEN':['IDEN'], 'N':['ANM','IANM'], 'PART':['PART', 'SADV', 'POSTP'], 'POSNUM':['POSNUM'], 'POSTP':['POSTP'], 'PR':['SEPER', 'JOPER', 'DEMON', 'INTG', 'CREFX', 'UCREFX', 'RECPR'], 'PREM':['EXAJ', 'QUAJ', 'DEMAJ', 'AMBAJ'], 'PRENUM':['PRENUM', 'IANM', 'POSNUM', 'AMBAJ'], 'PREP':['PREP'], 'PSUS':['PSUS'], 'PUNC':['PUNC'], 'V':['ACT', 'PASS', 'MODL'], 'SUBR':['SUBR']}

sens=codecs.open(os.path.abspath(sys.argv[1]),'r').read().strip().split('\n\n')
E=[]

for sen in sens:
	DTlines=sen.strip().split('\n')
	for i in DTlines:
		try:
			if not i.split('\t')[4] in D[i.split('\t')[3]]:
						print i
		except:
			print i
			print i.split('\t')[3]