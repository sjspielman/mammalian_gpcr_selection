import re, os

####### FUNCTION gets RSA from SA #########
def getRSA(SA, residue):

	#Matthew's theoretical values, but wrong..
	max_acc = {'A': 128.0, 'R': 275.0, 'N': 192.0, 'D': 191.0, \
    	       'C': 153.0, 'Q': 221.0, 'E': 221.0, 'G': 105.0,  \
        	   'H': 208.0, 'I': 194.0, 'L': 200.0, 'K': 233.0, \
               'M': 214.0, 'F': 230.0, 'P': 159.0, 'S': 149.0, \
               'T': 171.0, 'W': 269.0, 'Y': 259.0, 'V': 169.0}

	for aa in max_acc:
		if str(residue)==aa:
			RSA=float(SA)/float(max_acc[aa])
	
	return RSA
############################################



gene='ENST00000305352.txt'
dssp='3v2w_s1pr1'
outfile='output/3v2w_s1pr1'
outhandle=open(outfile, 'w')
outhandle.write('RSA\tOmega\tPart\n')




path2rates='/Users/stephaniespielman/Dropbox/receptors/Data/mammals/GPCR/hyphy/rel_8.2/siterates_withres/'


ingene=open(path2rates+gene, 'r')
genelines=ingene.readlines()
ingene.close()

indssp=open(dssp, 'r')
dlines=indssp.readlines()
indssp.close()



x=0 #numbering discrepency

rates=[]
SA=[]
for line in genelines:
	find=re.search('^(\d+)\t(\w)\t(\w+)\t(.+)$', line)
	if find != None:
		resnum=int(find.group(1))
		aa=find.group(2)
		partition=find.group(3)
		rate=float(find.group(4))
	
	
		#Residue number in MY file.
		resnum=resnum+x
		
		for n in range(28,len(dlines)):

			resnum2=dlines[n][6]+dlines[n][7]+dlines[n][8]+dlines[n][9]
			resnum2=resnum2.strip()
			find=re.search('\d', resnum2)
			if find !=None:	
				resnum2=int(resnum2)
			
				aa2=dlines[n][13]
				
				if resnum==resnum2 and aa==aa2:
					rates.append(rate)
					#print resnum,resnum2
					#print '\n\n'
					ACC=dlines[n][35]+dlines[n][36]+dlines[n][37]
					ACC=ACC.strip()
					SA.append(ACC)
					RSA=getRSA(float(ACC),aa)
					print ACC, RSA
					print resnum,RSA,rate
					outhandle.write(str(RSA)+'\t'+str(rate)+'\t'+partition+'\n')

#outhandle.close()
print len(rates)
print len(SA)


