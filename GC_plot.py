import sys
import matplotlib.pyplot as plt (# if yoy found error like not installed so install it after)

#Input file
Input=sys.argv[1]

sequence={}
seq_id=""
seq=""

#opening fasta
with open (Input,"r")as f:
        for line in f:
                line=line.strip()
                if line.startswith(">"):
                        if seq_id:
                                sequence[seq_id]=seq
                        seq_id =line[1:]
                        seq=""
                else:
                        seq+=line.upper()
#reading last sequence
        if seq_id:
                sequence[seq_id]=seq
#parameters for graph
ids=[]
gc_value=[]

#calculating GC%
for id,sequence in sequence.items():
        length=len(sequence)
        GC_count=sequence.count("G") + sequence.count("C")
        GC_percent=(GC_count / length) *100 if length >0 else 0
        ids.append(id)
        gc_value.append(GC_percent)

#plot
plt.figure(figsize=(8,5))
plt.bar(ids,gc_value)
plt.xlabel("Sequence IDS")
plt.ylabel("GC percents")
plt.title("GC content per sequence")
plt.savefig("gc_plot1.png")
print("plot save as gc_plot")
