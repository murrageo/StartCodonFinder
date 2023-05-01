import sys

# Get input from the command line arguments
if len(sys.argv) != 2:
    print("Usage: python find_in_frame_atg.py FILENAME")
    exit()
filename = sys.argv[1]

# Read the transcript sequence from the file, ignoring special characters and spaces
with open(filename, "r") as f:
    transcript = "".join([base.upper() for base in f.read() if base.upper() in ["A", "C", "G", "T"]])

# Find the location of the first ATG codon
start_codon = "ATG"
start_index = transcript.find(start_codon)
if start_index == -1:
    print("No start codon found.")
    exit()

# Trim the transcript to start at the first ATG codon
transcript = transcript[start_index:]

# Find the location of the next in-frame ATG codon and the codon boundaries
in_frame_atg = []
codon_boundaries = []
for i in range(3, len(transcript), 3):
    codon = transcript[i-3:i]
    codon_boundaries.append(i-3)
    if codon == start_codon:
        in_frame_atg.append(i-3)

# Print the location of in-frame ATG codons
if in_frame_atg:
    print("In-frame ATG codons found at bases:")
    for index in in_frame_atg:
        print(f"[{index+start_index}-{index+start_index+2}]")
else:
    print("No in-frame ATG codon found.")

# Count the total number of codons
num_codons = len(transcript) // 3

# Print the total number of codons
print(f"Total number of codons: {num_codons}")

# Format the transcript with in-frame ATG codons as uppercase
formatted_transcript = ""
for i in range(num_codons):
    codon = transcript[i*3:i*3+3]
    if i*3 in in_frame_atg:
        codon = f"[{codon}]"
    formatted_transcript += f"{codon} "

# Print the formatted transcript
print("Transcript with codons and in-frame ATG codons in uppercase:")
print(formatted_transcript.strip())