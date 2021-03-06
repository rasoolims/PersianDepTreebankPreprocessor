# -*- coding: utf8
import os,sys,codecs
from collections import defaultdict

def main(input_conll_file,output_conll_file):
	sens=codecs.open(input_conll_file,'r',encoding='utf-8').read().split('\n\n')
	writer=codecs.open(output_conll_file,'w',encoding='utf-8')

	for sen in sens:
		sen=sen.strip()

		if not sen:
			continue

		new_flds=defaultdict(list)
		new_index_list=dict()
		flds=sen.split('\n')

		new_index=0
		new_index_list[0]=0
		for i in range(0,len(flds)):
			index=i+1
			if not 'attachment=PRV' in flds[i]:
				new_index+=1
			new_flds[new_index].append(flds[i])
			new_index_list[index]=new_index

		final_output=list()
		for i in range(1,new_index+1):
			if len(new_flds[i])==1:
				cpnd=new_flds[i][0].split('\t')
				head=int(cpnd[6])
				new_head=new_index_list[head]
				cpnd[6]=str(new_head)
				cpnd[0]=str(i)
				final_output.append('\t'.join(cpnd))
			elif len(new_flds[i])==2:
				flds1=new_flds[i][0].split('\t')
				head1=int(flds1[6])
				new_head1=new_index_list[head1]
				pos1=flds1[3]
				fpos1=flds1[4]
				lemma1=flds1[2]
				word1=flds1[1]
				feat1=flds1[5]
				label1=flds1[7]

				flds2=new_flds[i][1].split('\t')
				head2=int(flds2[6])
				new_head2=new_index_list[head2]
				pos2=flds2[3]
				word2=flds2[1]
				fpos2=flds2[4]
				feat2=flds2[5]
				lemma2=flds2[2]
				label2=flds2[7]

				combined_word=u''
				combined_word=word1+word2
				if (word2.startswith(u'ا') or word2.startswith(u'آ')) and len(word2.strip())>1 and \
				not (word1.endswith(u'د') or word1.endswith(u'ذ') or word1.endswith(u'ر') or word1.endswith(u'ز') or word1.endswith(u'ا') or word1.endswith(u'آ')): 
					combined_word=word1+u'‌'+word2
					print combined_word
				combined_pos=pos1
				combined_fpos=fpos1
				combined_label=label1
				combined_lemma=lemma1+'|'+lemma2
				combined_feat=feat1+'|'+feat2
				combined_head=new_head1


				
				if (pos2=='N' and pos1!='V') or pos2=='V' or pos1=='POSTP'  or pos2=='POSTP':
					combined_pos=pos2
					combined_fpos=fpos2
					combined_head=new_head2
					combined_label=label2
					
				if pos1=='PR' and (pos2=='SUBR' or pos2=='CONJ'):
					combined_pos=pos2
					combined_head=new_head2
					combined_fpos=fpos2
					combined_label=label2
				if combined_head==i:
					if combined_head==new_head1:
						combined_head=new_head2
					else:
						combined_head=new_head1


				#if combined_word==u'مرا' and combined_label=='ACC-CASE':
					#combined_label=label2
					#combined_head=new_head2

				if combined_head==i:
					print i,new_head1,new_head2
				cpnd=str(i)+'\t'+combined_word+'\t'+combined_lemma+'\t'+combined_pos+'\t'+\
				combined_fpos+'\t'+combined_feat+'\t'+str(combined_head)+'\t'+combined_label+'\t_\t_'
				final_output.append(cpnd)
			else:
				print new_flds[i]
				sys.exit(1)

		final_output2=list()
		for x in range(0,len(final_output)):
			spl=final_output[x].split('\t')
			if spl[1]==u'مرا' and spl[7]=='ACC-CASE':
				spl[7]='OBJ'
			final_output2.append('\t'.join(spl))
		writer.write('\n'.join(final_output2)+'\n\n')
	writer.flush()
	writer.close()




if __name__ == '__main__':
	if len(sys.argv)<2:
		print 'python merge_disjoint_words.py [input_conll_file] [output_conll_file]'
		print '>> This script converts the conll file such that disjoint words are merged'
		print '>> Disjoint words are attachment=NXT and attachment=PRV'
		sys.exit(0)
	main(os.path.abspath(sys.argv[1]),os.path.abspath(sys.argv[2]))