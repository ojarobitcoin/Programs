file1,names,i,bases=[],[],0,["A","T","G","C"]
with open(input("Which file are you going to analyze?/n>>"), "r") as gff:
    for lines in gff:
        if set(lines).difference(bases) == set():#Store the names and all the sequences
            continue
        cord1,cord2=(lines.find("ATG")),(lines.find("TAG"))
        if lines.startswith(">"):
            names=(lines.replace(">","")).replace("\n","")
            continue
        motiffind=(lines[lines.find("ATG"):lines.find("TAG")+3:])
        if not len(lines[lines.find("ATG"):lines.find("TAG")+3:])<5:
            print(f"{names}    {len(motiffind)}    {cord1,cord2} TAG\n{motiffind}")
            file1.append((lines[lines.find("ATG"):lines.find("TAG")+3:]).replace("\n", ""))
        motiffind=(lines[lines.find("ATG"):lines.find("TAA")+3:])
        if not len(lines[lines.find("ATG"):lines.find("TAA")+3:])<5:
            print(f"{names}    {len(motiffind)}    {cord1,cord2}    TAA\n{motiffind}")
            file1.append((lines[lines.find("ATG"):lines.find("TAA")+3:]).replace("\n", ""))
        motiffind=lines[lines.find("ATG"):lines.find("TGA")+3:]
        if not len(lines[lines.find("ATG"):lines.find("TGA")+3:])<5:
            print(f"{names}    {len(motiffind)}    {cord1,cord2}    TGA\n{motiffind}")
            file1.append((lines[lines.find("ATG"):lines.find("TGA")+3:]).replace("\n", ""))
