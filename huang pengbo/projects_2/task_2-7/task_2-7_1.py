files = ["seq1", "seq2", "seq3", "seq4"]
date = "2026-04-02"

for name in files:
    new_name = name + "_" + date + ".fasta"
    print(new_name)