import os,re,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings.development')
django.setup()
from prep.models import PrepTopic,PrepContentCache
from services.prep_ai_router import (_cache_payload_as_dict,_note_validation_options,_note_completion_issues,_display_math_issues,_latex_syntax_issues)
from services.prep_blocks import parse_markdown_to_blocks,validate_structured_blocks
SL=chr(92)
LET=r'A-Za-z\u0391-\u03c9\u0394\u03a3\u03a0\u2211\u222b\u2207\u221a'
FUNCS={'sin','cos','tan','ln','log','exp','max','min','lim','sup','inf','product','sum','det','rank','trace','span','arg','mod','delta','pi'}
PROTECTED=re.compile(r'(```[\s\S]*?```|`[^`\n]*`|\$\$[\s\S]*?\$\$|'+re.escape(SL+'[')+r'[\s\S]*?'+re.escape(SL+']')+'|'+re.escape(SL+'(')+r'[\s\S]*?'+re.escape(SL+')')+r'|(?<!\\)\$(?!\$)[^$\n]*?(?<!\\)\$(?!\$))')
LEFT=re.compile(r'(?<![\w$])(?P<lhs>['+LET+r']['+LET+r'0-9_{}^+\-\x27\u2032\u2019\u2070\u00b2\u00b3\u2074-\u2079]*(?:\([^()\n]{1,80}\))?)(?P<sp>\s*)(?P<op>=|\u2248|\u2264|\u2265|\u2260|<|>)')
LEFT_NUM=re.compile(r'(?<![\w$])(?P<lhs>[+-]?\d+(?:\.\d+)?(?:\s*[+\-\u2212*/]\s*\d+(?:\.\d+)?)+)(?P<sp>\s*)(?P<op>=|\u2248|\u2264|\u2265|\u2260|<|>)')
LEFT_DERIV=re.compile(r'(?<![\w$])(?P<lhs>d(?:[\u2070\u00b2\u00b3\u2074-\u2079]|\^[0-9]+)?\s*/\s*d[A-Za-z](?:[\u2070\u00b2\u00b3\u2074-\u2079]|\^[0-9]+)?)(?P<sp>\s*)(?P<op>=|\u2248|\u2264|\u2265|\u2260|<|>)')
LEFT_BRACKET=re.compile(r'(?<![\w$])(?P<lhs>['+LET+r']['+LET+r'0-9_{}^]*\[[^\]\n]{1,80}\])(?P<sp>\s*)(?P<op>=|\u2248|\u2264|\u2265|\u2260|<|>)')
LEFT_PAREN=re.compile(r'(?<![\w$])(?P<lhs>\([^()\n]{1,60}\)[A-Za-z0-9_{}^]+(?:[+\-][A-Za-z0-9_{}^]+)*)(?P<sp>\s*)(?P<op>=|\u2248|\u2264|\u2265|\u2260|<|>)')
SCRIPT=re.compile(r'(?<![\w\\$])(?:['+LET+r']['+LET+r'0-9]*(?:_(?:\{[^{}\n]+\}|\([^()\n]+\)|[A-Za-z0-9+\-]+)|\^(?:\{[^{}\n]+\}|\([^()\n]+\)|[A-Za-z0-9+\-]+))+(?:\([^()\n]{1,80}\))?|[A-Za-z]['+LET+r'0-9_{}^\x27\u2032\u2019]*\([^()\n]{1,80}\)|['+LET+r']['+LET+r'0-9]*[\u2080-\u2089\u2070\u00b9\u00b2\u00b3\u2074-\u2079]+[A-Za-z0-9_{}^]*)')
ARITH=re.compile(r'(?<![\w$])(?:['+LET+r'][A-Za-z0-9_{}^]*|\d+(?:\.\d+)?)(?:\s*[+\-\u2212*/\u00d7\u00f7]\s*(?:['+LET+r'][A-Za-z0-9_{}^]*|\d+(?:\.\d+)?))+(?![\w$])')
COEFF=re.compile(r'(?<![\w$])[-+]?\d+(?:\.\d+)?['+LET+r'](?:_[A-Za-z0-9{}()+\-]+|\^[A-Za-z0-9{}()+\-]+)*(?:\([^()\n]{1,60}\))?(?!\w)')
FRAC=re.compile(r'(?<![\w$])(?:\[[^\]\n]{1,120}\]|\([^()\n]{1,120}\)|['+LET+r'][A-Za-z0-9_{}^\u2070\u00b2\u00b3\u2074-\u2079]*)\s*/\s*(?:\[[^\]\n]{1,120}\]|\([^()\n]{1,120}\)|['+LET+r'][A-Za-z0-9_{}^\u2070\u00b2\u00b3\u2074-\u2079]*|\d+(?:\.\d+)?!?)')
LIST=re.compile(r'(?<![\w$])['+LET+r'][A-Za-z0-9]*[_^][A-Za-z0-9{}]+(?:\s*,\s*\.{3}\s*,\s*['+LET+r'][A-Za-z0-9]*[_^][A-Za-z0-9{}]+)+')
PRIME=re.compile(r"(?<!\w)[A-Za-z]\'{1,3}(?!\w)")
TERM=r'(?:\d+(?:\.\d+)?['+LET+r'][A-Za-z0-9_{}^+\-\u2070\u00b2\u00b3\u2074-\u2079]*|['+LET+r'][A-Za-z0-9_{}^+\-\u2070\u00b2\u00b3\u2074-\u2079]*|\d+(?:\.\d+)?)'
SUM=re.compile(r'(?<![\w$])'+TERM+r'(?:\s*[+\-\u2212]\s*'+TERM+r')+(?![\w$])')
PAREN_BRACKET=re.compile(r'(?<![\w$])\([^()\n]{1,60}\)\s*\[[^\]\n]{1,160}\]')
AMBIG=re.compile(r"(?<!\w)h\?f'{1,3}(?!\w)")
REL=re.compile(r'(?<![=<>])(?:=|\u2248|\u2264|\u2265|\u2260|<|>)')
ATOM=r'(?:\d+(?:\.\d+)?|(?:['+LET+r']|['+LET+r'][A-Za-z0-9]*(?:_(?:\{[^{}\n]+\}|[A-Za-z0-9()+\-]+)|\^(?:\{[^{}\n]+\}|[A-Za-z0-9()+\-]+)|[\u2080-\u2089\u2070\u00b9\u00b2\u00b3\u2074-\u2079]+)?)(?:\'{1,3})?(?:\([^()\n]{1,80}\))?)'
EXPR=re.compile(r'(?<![\w$])'+ATOM+r'(?:\s*(?:[+\-\u2212*/\u00d7\u00f7]|=|\u2248|\u2264|\u2265|\u2260|<|>|,)\s*'+ATOM+r')+(?!\w)')
ONLY=re.compile(r'^[A-Za-z0-9\u0391-\u03c9\u0394\u03a3\u03a0\u2211\u222b\u2207\u221a_{}^\u2032\u2019()\[\].,:+\-\u2212*/=<>\u2264\u2265\u2248\u2260\u00d7\u00f7\u00b1|\s]+$')
def _spans(s): return [(m.start(),m.end()) for m in PROTECTED.finditer(s)]
def _overlaps(a,b,spans): return any(a<y and b>x for x,y in spans)
def _end(s,pos):
    i=pos; depth=0
    while i<len(s):
        c=s[i]
        if c in '([{': depth+=1
        elif c in ')]}':
            if depth: depth-=1
            elif c in ')]': break
        if depth==0:
            if c in ';:': break
            if c in '!?':
                if i+1==len(s) or s[i+1].isspace(): break
            if c==',' and not(i>0 and i+1<len(s) and s[i-1].isdigit() and s[i+1].isdigit()): break
            if c=='.':
                if s[i:i+3]=='...': i+=3; continue
                if not(i>0 and i+1<len(s) and s[i-1].isdigit() and s[i+1].isdigit()): break
            if c.isspace():
                w=re.match(r'\s+([A-Za-z]+)\b',s[i:])
                if w and len(w.group(1))>1 and w.group(1).lower() not in FUNCS: break
        i+=1
    return i
def _scriptlike(expr):
    return '_' in expr or '^' in expr or any(c in expr for c in '₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹')
def _is_math(expr):
    if _scriptlike(expr): return True
    words=[w.lower() for w in re.findall(r'\b[A-Za-z]{2,}\b',expr)]
    return all(w in FUNCS for w in words)
def _math_bridge(gap):
    gap=re.sub(r'\\[()]','',gap)
    if not gap.strip(): return True
    if re.search(r'[^\w\s{}()\[\].,:+\-\u2212*/^_=<>|!]',gap): return False
    words=re.findall(r'[A-Za-z]+',gap)
    return all(len(w)==1 or w.lower() in FUNCS for w in words)
def _para(p):
    spans=_spans(p); hm=re.match(r'^(\s*#{1,6}\s+)',p); heading=hm.group(1) if hm else ''; s=p[len(heading):]
    if not s.strip() or s.lstrip().startswith('```'): return p,0,0,0
    table=s.lstrip().startswith('|')
    if not heading and not table and not spans and ONLY.fullmatch(s.strip()) and re.search(r'[=<>+\-*/^_\u2080-\u2089\u2070-\u2079]',s):
        words=[w.lower() for w in re.findall(r'\b[A-Za-z]{2,}\b',s)]
        if all(w in FUNCS for w in words):
            n=sum(bool(re.search(r'[=<>]',line)) for line in s.splitlines() if line.strip()) or 1
            return '$$\n'+s.strip()+'\n$$',n,0,1
    ranges=[];eq=other=0
    for pattern in (LEFT_DERIV,LEFT_BRACKET,LEFT_PAREN,LEFT_NUM,LEFT):
        for m in pattern.finditer(s):
            if _overlaps(m.start(),m.end(),spans): continue
            a=m.start('lhs'); b=_end(s,m.end()); pre=re.search(r'(?<!\w)([A-Za-z])\s+$',s[:a])
            if pre and not _overlaps(pre.start(1),b,spans): a=pre.start(1)
            while b>m.end() and s[b-1].isspace(): b-=1
            if b>m.end() and s[b-1] in '.,;:': b-=1
            if b>m.end() and s[m.end():b].strip(): ranges.append((a,b)); eq+=1
    for pat in [PAREN_BRACKET,EXPR,SUM,LIST,SCRIPT,ARITH,COEFF,FRAC,PRIME,AMBIG]:
        for m in pat.finditer(s):
            if _overlaps(m.start(),m.end(),spans) or any(m.start()<b and m.end()>a for a,b in ranges): continue
            if not _is_math(m.group(0)): continue
            ranges.append((m.start(),m.end())); other+=1
    ranges.sort(); merged=[]
    for a,b in ranges:
        if merged and (a<merged[-1][1] or _math_bridge(s[merged[-1][1]:a])): merged[-1]=(merged[-1][0],max(merged[-1][1],b))
        else: merged.append((a,b))
    out=[]; pos=0
    for a,b in merged:
        before=s[a-1] if a else ''; after=s[b] if b<len(s) else ''
        pre=' ' if before and (before.isalnum() or before=='_') else ''
        post=' ' if after and (after.isalnum() or after=='_') else ''
        out.extend([s[pos:a],pre,SL+'(',s[a:b],SL+')',post]); pos=b
    out.append(s[pos:])
    return heading+''.join(out),len(merged),eq,other
def format_content(text):
    parts=PROTECTED.split(text); out=[]; counts=[0,0,0]
    for j,part in enumerate(parts):
        if not part: continue
        if j%2: out.append(part); continue
        st=0
        for m in re.finditer(r'\n[ \t]*\n',part):
            q,a,b,c=_para(part[st:m.start()]); out.append(q); counts=[x+y for x,y in zip(counts,[a,b,c])]; out.append(m.group(0)); st=m.end()
        q,a,b,c=_para(part[st:]); out.append(q); counts=[x+y for x,y in zip(counts,[a,b,c])]
    return ''.join(out),counts[0],counts[1],counts[2]
def _dewrap(text):
    pat=r'\$\$|\$|'+re.escape(SL+'(')+r'|'+re.escape(SL+')')+r'|'+re.escape(SL+'[')+r'|'+re.escape(SL+']')
    return re.sub(r'\s+',' ',re.sub(pat,'',text)).strip()
def _equal(old,new):
    a,b=_dewrap(old),_dewrap(new)
    return re.sub(r'\s+','',a)==re.sub(r'\s+','',b)
if __name__=='__main__':
    for tid in (200,201,202):
        topic=PrepTopic.objects.get(pk=tid,course_id=48); latest={}
        for row in PrepContentCache.objects.filter(topic=topic,content_type='topic_notes').order_by('-created_at','-pk'):
            payload=_cache_payload_as_dict(row.payload) or {}; level=payload.get('level')
            if level and level not in latest: latest[level]=(row,payload)
        for level in ('level_1','level_2','level_3'):
            row,payload=latest[level]; old=str(payload.get('content') or ''); new,n,neq,nother=format_content(old)
            raw=PROTECTED.sub(' ',new)
            if row.pk in (1478,1312,1525):
                for para in re.split(r'\n\s*\n',new):
                    u=PROTECTED.sub(' ',para)
                    if re.search(r'(?<![=<>])=(?!=)|\b[A-Za-z]+_[A-Za-z0-9({+\-]|\b[A-Za-z0-9]+\^[A-Za-z0-9({]|\b[A-Za-z][A-Za-z0-9_]*\([^()\n]{1,60}\)|\b\d+[A-Za-z](?:\^[A-Za-z0-9{}]+)?',u):
                        print('UNWRAPPED',row.pk,repr(u[:400]))
                        break
            residual=list(re.finditer(r'(?<![=<>])=(?!=)|\b[A-Za-z]+_[A-Za-z0-9({+\-]|\b[A-Za-z0-9]+\^[A-Za-z0-9({]|\b[A-Za-z][A-Za-z0-9_]*\([^()\n]{1,60}\)|\b\d+[A-Za-z](?:\^[A-Za-z0-9{}]+)?',raw))
            opts=_note_validation_options(topic.course,topic.title,topic.summary,topic.subtopics,topic_obj=topic)
            issues=_note_completion_issues(new,topic.title,level=level,allow_validated_legacy_headings=False,**opts)
            math_issues=_display_math_issues(new)+_latex_syntax_issues(new)
            blocks=parse_markdown_to_blocks(new); block_status=validate_structured_blocks(blocks)
            print('ROW',row.pk,level,'inline',n,'equations',neq,'other',nother,'display',new.count('$$')-old.count('$$'),'integrity',_equal(old,new),'issues',issues,'math',math_issues,'blocks',block_status,'raw_candidates',len(residual))
            shown=0
            for para in re.split(r'\n\s*\n',new):
                unwrapped=PROTECTED.sub(' ',para)
                if re.search(r'(?<![=<>])=(?!=)|\b[A-Za-z]+_[A-Za-z0-9({+\-]|\b[A-Za-z0-9]+\^[A-Za-z0-9({]|\b[A-Za-z][A-Za-z0-9_]*\([^()\n]{1,60}\)|\b\d+[A-Za-z](?:\^[A-Za-z0-9{}]+)?',unwrapped):
                    print('REMAIN',repr(para[:500]))
                    shown+=1
                    if shown==1: break
            if not _equal(old,new):
                a,b=_dewrap(old),_dewrap(new)
                print('DIFF',repr(a[:160]),repr(b[:160]))
                for k,(x,y) in enumerate(zip(a,b)):
                    if x!=y:
                        print('FIRST_DIFF',k,repr(a[max(0,k-80):k+120]),repr(b[max(0,k-80):k+120]))
                        break
            for m in residual[:3]: print('RAW',repr(raw[max(0,m.start()-50):m.end()+80]))
