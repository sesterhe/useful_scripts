import re 
import sys 

input_file = sys.argv[1]
pCT_adapter_5 = "GCAGGCATGTACCATGATGATACAGAATTTTGTTTAACTTTAAGAAGGAGATATACATATGGCTAGC"
pCT_adapter_3 = "GGCTCTCTCGAGCACCACCACCACCACCACGTATGACTAGTATACCAGTAGCCAGTGCA"


output_file=sys.argv[2]
dna = []
sequences = []

def read_fasta(input_file):

    with open(input_file) as file:    
        for line in file: 
            header = re.search('>', line)
            if header:
                line = line.rstrip("\n")
		line = line.replace(">","")
                dna.append(line)            
            else:               
                seq = line.replace('\n', '')  
                sequences.append(seq)      
read_fasta(input_file)
print dna
suffix="_pET21"
adaptered_sequence = [pCT_adapter_5 + e + pCT_adapter_3 for e in sequences]
new_name = [">3hb_" + name.strip(">") + suffix for name in dna]

test=zip(new_name, adaptered_sequence)
#a = ''.join(str(e) for e in test)

a = '\n'.join(">""\n".join(e) for e in test)

#b = a.replace("'","")
#c = b.replace(",","\n")
#d = c.replace("(","\n").replace(")","")


with open(output_file, "w") as fo: 
	fo.write(a)
