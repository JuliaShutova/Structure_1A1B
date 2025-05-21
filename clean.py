with open("pdb1ab1.pdb", "r") as f:
    lines = f.readlines()

# Сохраняем только основную цепь A
cleaned = []
for line in lines:
    if line.startswith("ATOM") and "HOH" not in line:
        if " A " in line:
            cleaned.append(line)

with open("pdb1ab1_clean.pdb", "w") as f:
    f.writelines(cleaned)