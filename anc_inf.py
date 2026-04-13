import pandas as pd

df = pd.read_csv("APOE_windows.msp", delim_whitespace=True, header=None)

print("Total columns:", df.shape[1])

ancestry = df.iloc[:, 6:]
print("Ancestry columns:", ancestry.shape[1])
print("Number of samples:", ancestry.shape[1] // 2)

row = ancestry.iloc[0]

map_dict = {
    0: "SAS",
    1: "AFR",
    2: "AMR",
    3: "EAS",
    4: "EUR"
}

results = []

for i in range(0, len(row), 2):
    hap1 = map_dict[row.iloc[i]]
    hap2 = map_dict[row.iloc[i+1]]
    sample_id = int(i/2)

    results.append([sample_id, hap1, hap2])

out = pd.DataFrame(results, columns=["Sample", "Hap1_ancestry", "Hap2_ancestry"])
out.to_csv("APOE_two_ancestries.txt", sep="\t", index=False)

print(out)
