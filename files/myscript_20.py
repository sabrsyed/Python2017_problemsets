#!/usr/bin/env python3
#Python_05 question 5

alpaca_all= open ("../alpaca_all_genes.tsv", "r")
alpaca_pigm= open ("../alpaca_pigmentation_genes.tsv", "r")
alpaca_sc= open ("../alpaca_stemcellproliferation_genes.tsv", "r")

all= alpaca_all.read().split('\n')[1:] 
all_set = set(all)
#print(all_set)

pigm= alpaca_pigm.read().split('\n')[1:]
pigm_set = set(pigm)
#print(pigm_set)

sc= alpaca_sc.read().split('\n')[1:]
sc_set = set(sc)
#print(sc_set)


#Find all the genes that are not stem cell proliferation genes.

#print(all_set - sc_set)
not_sc= all_set - sc_set
not_sc_count= 0

for line in not_sc:
	not_sc_count += 1
	
print("not_sc_count:", not_sc_count)

###Find all genes that are both stem cell proliferation genes and pigment genes.

both_scandpigm = sc_set & pigm_set
both_scandpigm_count = 0

for gene in both_scandpigm:
	
	both_scandpigm_count += 1
	print(gene) 
	
print("both_scandpigm_count:", both_scandpigm_count)

alpaca_all.close()
alpaca_pigm.close()
alpaca_sc.close()


****it's counting a blank line.. need to fix
