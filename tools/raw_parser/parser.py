# -*- coding: utf-8 -*-

import re

'''
with open('list.txt','r',encoding='utf-8') as file:
    changes=file.read().replace('\n','')
'''
changes=(
    ('','\n'),
    ('≅','\n'),
    ('본문 [0-9]{2,3}~[0-9]{2,3}쪽([0-9]{4})?',''),
    ('(([0-9]{2}~)?[0-9]{2})\n','\\1\n\n'),
    #('[0-9]{2}\~?\n','\n'),
    ('  EBS 수능특강 영어',''),
    ('영단어·숙어  [0-9]\d\n.+편',''),
    ('Part(Ⅰ-Ⅲ).*\n',''),
    ('수능특강영어영역   영어\n유형편',''),
    ('[0-9]{2}\n',''),
    ('…','...'),
    (' *_ *','\t'),
    (' *\( pl\. ',' (pl.'),
    (' {2,}',' '),
    ('\n(^\t)+\n','\n'),
    ('(글의 목적 파악|분위기·심경·어조 파악|함축적 의미 파악|요지·주장 파악|주제 파악|제목 파악|도표 정보 파악|내용 일치·불일치|어법 정확성 파악|어휘 적절성 파악|지칭 추론|빈칸 내용 추론|흐름에 무관한 문장 찾기|문단 내 글의 순서 파악|문단 속에 문장 넣기|문단 요약|장문 독해 \(1\)~*|장문 독해 \(2\)~*|인물, 일화, 기담|철학, 종교, 역사, 풍습, 지리|환경, 자원, 재활용|물리, 화학, 생명과학, 지구과학|스포츠, 레저, 취미, 여행|음악, 미술, 영화, 무용, 사진, 건축|교육, 학교, 진로|언어, 문학, 문화|컴퓨터, 인터넷, 정보, 미디어, 교통|심리, 대인 관계|정치, 경제, 사회, 법|의학, 건강, 영양, 식품|Test *1|Test *2|Test *3)',''),
    ('영단어·숙어 \n[가-힣•]+편Part[Ⅰ-Ⅲ]',''),
    ('[가-힣•]+편Part[Ⅰ-Ⅲ]',''),
    ('PartⅠ',''),
    ('(\n){2,}','\n'),
    ('= ','=')
)

with open('raw.txt','r',encoding='utf-8') as file:
    data=file.readlines()

result=[]
for line in data:
    changed=line
    for change in changes:
        pre,to=change
        changed=re.sub(pre,to,changed)
    result.append(changed)

out='\n'.join(result)

with open('test.txt','w',encoding='utf-8') as file:
    file.write(out)