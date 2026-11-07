import re, io
for f in ["295_level_1.md","295_level_2.md","295_level_3.md"]:
    text=open(f,encoding="utf-8").read()
    lines=text.split("\n")
    print("=== ",f, len(text.split()),"words")
    bad=[]
    for i,l in enumerate(lines):
        if "$$" in l:
            if l.strip()!="$$":
                bad.append((i+1,"inline display line: "+l[:60]))
            else:
                prev=lines[i-1] if i>0 else ""
                nxt=lines[i+1] if i+1<len(lines) else ""
                if i>0 and prev.strip()!="" and prev.strip()!="$$":
                    bad.append((i+1,"no blank before"))
    # blank after closing blocks
    for i,l in enumerate(lines):
        if l.strip()=="$$":
            pass
    # check paragraph directly after closing $$ lacking blank line
    inblock=False; openline=0
    for i,l in enumerate(lines):
        if l.strip()=="$$":
            if not inblock:
                inblock=True; openline=i
            else:
                inblock=False
                if i+1<len(lines) and lines[i+1].strip()!="" and not lines[i+1].startswith(">"):
                    bad.append((i+1,"no blank after close: "+lines[i+1][:40]))
    for b in bad[:12]: print("  ",b)
    if inblock: print("  UNCLOSED BLOCK at",openline+1)
    print("  headings:")
    for l in lines:
        if l.startswith("## "):
            print("   ",l)
