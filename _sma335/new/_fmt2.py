for f in ["295_level_1.md","295_level_2.md","295_level_3.md"]:
    lines=open(f,encoding="utf-8").read().split("\n")
    norm=[l[2:] if l.startswith("> ") else l for l in lines]
    bad=[]; inb=False; o=0
    for i,l in enumerate(norm):
        s=l.strip()
        if s=="$$":
            if not inb:
                inb=True; o=i
                if i>0 and norm[i-1].strip()!="" and norm[i-1].strip()!="$$":
                    bad.append((i+1,"no blank before open"))
            else:
                inb=False
                if i+1<len(norm) and norm[i+1].strip()!="" and not norm[i+1].startswith(">"):
                    bad.append((i+1,"no blank after close -> "+lines[i+1][:50]))
        elif "$$" in s:
            bad.append((i+1,"mixed line: "+s[:60]))
    if inb: bad.append((o+1,"UNCLOSED"))
    print(f, "issues:", bad if bad else "none")
