# coding: utf8

import os,sys,codecs
from collections import defaultdict

def main(input_conll_file,output_conll_file):
	sens=codecs.open(input_conll_file,'r').read().split('\n\n')
	writer=codecs.open(output_conll_file,'w')

	for sen in sens:
		sen=sen.strip()

		if not sen:
			continue

		new_lines=list()
		lines=sen.split('\n')
		index_list=dict()
		rev_index_list=dict()
		rev_index_list[0]=0

		new_index=0
		index=0
		for line in lines:
			index+=1
			flds=line.split('\t')
			pos=flds[3]
			fpos=flds[4]
			feats=flds[5].split('|')
			tma=''
			for feat in feats:
				if feat.startswith('tma='):
					tma=feat[4:]
					break

			word=flds[1].strip()
			w_split=word.split(' ')

			if len(w_split)==1:
				new_index+=1
				index_list[new_index]=index
				rev_index_list[index]=new_index
				new_lines.append(line)
			elif pos!='V' and len(w_split)>1:
				#print word,pos
				nf=str(index)+'\t'+w_split[0]+'\t'+w_split[0]+'\t'+'\t'.join(flds[3:])+'\t_\t_'
				new_lines.append(nf)
				new_index+=1
				index_list[new_index]=index
				rev_index_list[index]=new_index
				
				for ind in range(1,len(w_split)):
					nf=str(index)+'\t'+w_split[ind]+'\t'+w_split[ind]+'\t'+'\t'.join(flds[3:6])+'\t'+str(index)+'\t'+'POSDEP\t_\t_'
					new_lines.append(nf)
					new_index+=1
					index_list[new_index]=index
			else:
				if (tma=='AY'  or (tma=='HEL' and 'خواه' in w_split[0]) ) and len(w_split)==2:
					for ind in range(0,1):
						nf=str(index)+'\t'+w_split[ind]+'\t'+w_split[ind]+'\t'+'\t'.join(flds[3:6])+'\t'+str(index)+'\t'+'AUX\t_\t_'
						new_lines.append(nf)
						new_index+=1
						index_list[new_index]=index
					nf=str(index)+'\t'+w_split[1]+'\t'+w_split[1]+'\t'+'\t'.join(flds[3:])+'\t_\t_'
					new_lines.append(nf)
					new_index+=1
					index_list[new_index]=index
					rev_index_list[index]=new_index			
				elif tma=='AY'  or tma=='GNES' or tma=='GBES' or tma=='GES' or tma=='GN' or tma=='GB' or\
				 tma=='H' or tma=='HA' or tma=='GS' or tma=='GBESE' or tma=='GESEL'  or tma=='GBEL' or tma=='GEL' or (tma=='HEL' and not 'خواه' in w_split[0]):
					nf=str(index)+'\t'+w_split[0]+'\t'+w_split[0]+'\t'+'\t'.join(flds[3:])+'\t_\t_'
					new_lines.append(nf)
					new_index+=1
					index_list[new_index]=index
					rev_index_list[index]=new_index
						
					for ind in range(1,len(w_split)):
						nf=str(index)+'\t'+w_split[ind]+'\t'+w_split[ind]+'\t'+'\t'.join(flds[3:6])+'\t'+str(index)+'\t'+'AUX\t_\t_'
						new_lines.append(nf)
						new_index+=1
						index_list[new_index]=index

		final_output=list()		
		for i in range(0,len(new_lines)):
			line=new_lines[i]
			new_index=i+1
			index=index_list[new_index]
			flds=line.split('\t')
			head=int(flds[6])
			new_head=rev_index_list[head]
			output=str(new_index)+'\t'+'\t'.join(flds[1:6])+'\t'+str(new_head)+'\t'+'\t'.join(flds[7:])
			final_output.append(output)

		writer.write('\n'.join(final_output)+'\n\n')

	writer.flush()
	writer.close()



if __name__ == '__main__':
	if len(sys.argv)<2:
		print 'python split_multiword_verbs.py [input_conll_file] [output_conll_file]'
		print '>> This script converts the conll file such that multiword verbs become more than one token'
		sys.exit(0)
	main(os.path.abspath(sys.argv[1]),os.path.abspath(sys.argv[2]))