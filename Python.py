## Import and read file containing DNA Sequences in multi-FASTA format
try:
	f = open("/Users/khaitlinbernaldez/Desktop/dna2.fasta")
except IOError:
	print("File dna.example.fasta does not exist!")

seqs = {}
for line in f:
	line = line.rstrip()
	if line[0] == '>':
		words = line.split()
		name = words[0][1:]
		seqs[name] = ''
	else:
		seqs[name] = seqs[name] + line

## How many records are in the file?
print(len(seqs)) ## 25

## What are the lengths of the sequences in the file? 
## Longest sequence?
## Shortest sequence? 
## More than one of each? 
## What are their identifiers?
sorted_values = sorted(seqs.values(), key = len)
sorted_seq = {}

for i in sorted_values:
		for k in seqs.keys():
				if seqs[k] == i:
					sorted_seq[k] = seqs[k]
					break

for name, seq in sorted_seq.items():
	 print('NAME:' + name, 'LENGTH:' + str(len(seq)))

## Find ORFs in file input
## Longest ORF with specific identifier?
def find_orf(sequence, frame):
	start_indices = []
	stop_indices = []
	orf = []
	front = 0
	start_codon = 'ATG'
	stop_codon = ['TAA', 'TAG', 'TGA']
	for i in range(frame, len(sequence), 3):
		codon = sequence[i:i+3]
		if codon == start_codon:
			start_indices.append(i)
	## print("start:" + str(start_indices))
	for i in range(frame, len(sequence), 3):
		codon = sequence[i:i+3]
		if codon in stop_codon:
			stop_indices.append(i)
	## print ("stop:" + str(stop_indices))
	for i in range(0, len(start_indices)):
		for j in range(0, len(stop_indices)):
			if start_indices[i] < stop_indices[j] and start_indices[i] > front:
				orf.append(sequence[start_indices[i]:stop_indices[j] + 3])
				front = stop_indices[j] + 3
	return orf

def find_max_length(sequence, frame):
	orf_length = []
	for i in range(0, len(find_orf(sequence, frame))):
		orf_length.append(len(find_orf(sequence, frame)[i]))
	for i in orf_length:
		if i:
			return max(orf_length)

## Length of longest ORF in reading frame?
max_length = []
for value in seqs.values():
	if find_max_length(value, 2) != None: ## Removes nulls
		max_length.append(find_max_length(value, 2))
print(max(max_length))

## Starting position of longest ORF?
target_sequence = []
for value in seqs.values():
	for i in range(0, len(find_orf(value, 2))):
		if len(find_orf(value, 2)[i]) == 1821:
			target_sequence.append(find_orf(value, 2)[i])

for value in seqs.values():
	for i in range(0, len(value)):
		seq = value[i:i+len(b)]
		if seq == b:
			print(i)
