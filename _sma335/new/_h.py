for f in ["295_level_1.md","295_level_2.md","295_level_3.md"]:
    print("===",f)
    for l in open(f,encoding="utf-8"):
        if l.startswith("### "):
            print("  ",l.strip())
