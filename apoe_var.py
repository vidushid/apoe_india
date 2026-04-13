import pandas as pd

df = pd.read_csv("apoe_genotypes.txt", sep="\t", header=None)

snp1 = df.iloc[0, 1:]  # 44908684
snp2 = df.iloc[1, 1:]  # 44908822

def convert(gt, ref, alt):
    if gt == "0|0": return [ref, ref]
    if gt in ["0|1", "1|0"]: return [ref, alt]
    if gt == "1|1": return [alt, alt]
    return [None, None]

counts = {}

for g1, g2 in zip(snp1, snp2):
    a1, a2 = g1.split("|")
    b1, b2 = g2.split("|")

    def map_hap(x, y):
        if x == "0" and y == "1": return "e2"
        elif x == "0" and y == "0": return "e3"
        elif x == "1" and y == "0": return "e4"
        else: return None  # invalid

    h1 = map_hap(a1, b1)
    h2 = map_hap(a2, b2)

    if h1 is None or h2 is None:
        continue

    genotype = "/".join(sorted([h1, h2]))
    counts[genotype] = counts.get(genotype, 0) + 1

print(counts)
