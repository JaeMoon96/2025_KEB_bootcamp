#  딕셔너리 생성 (과목명을 key, 교수명을 value로 설정)
sugang = dict(python="kim", cpp="sung", db="kang")  # {"python": "kim", "cpp": "sung", "db": "kang"}
#sugang = {'py thon': 'kim', c p p: 'sung', db : 'kang') 아래코드는 공란이있어도 무방
#  딕셔너리 전체 출력
print(sugang)  
# 출력: {'python': 'kim', 'cpp': 'sung', 'db': 'kang'}

#  새로운 key-value 쌍 추가
sugang['datastructure'] = 'kim'  # 'datastructure' 과목의 담당 교수를 'kim'으로 추가

#  딕셔너리 출력 (추가된 값 확인)
print(sugang)  
# 출력: {'python': 'kim', 'cpp': 'sung', 'db': 'kang', 'datastructure': 'kim'}

#  기존 key의 값 변경 (업데이트)
sugang['datastructure'] = 'park'  # 'datastructure' 담당 교수를 'park'으로 변경

#  딕셔너리 출력 (변경된 값 확인)
print(sugang)  
# 출력: {'python': 'kim', 'cpp': 'sung', 'db': 'kang', 'datastructure': 'park'}

#  특정 과목의 담당 교수 출력
print(sugang['db'])  # 'kang'

#  get()을 사용한 key 조회 (안전한 방식)
print(sugang.get('db'))  # 'kang'

#  존재하지 않는 key 조회 시 None 반환
print(sugang.get('opensource'))  # None

#  존재하지 않는 key 조회 시 기본값 설정
print(sugang.get('opensource', 'not exist'))  # 'not exist'

#  딕셔너리의 key-value 쌍을 반복문으로 출력
for subject, professor in sugang.items():
    print(f'{subject} 과목 담당교수는 {professor}입니다')

# 출력 결과:
# python 과목 담당교수는 kim입니다
# cpp 과목 담당교수는 sung입니다
# db 과목 담당교수는 kang입니다
# datastructure 과목 담당교수는 park입니다

#  딕셔너리의 key만 출력 (방법 1: keys() 사용)
for k in sugang.keys():
    print(k)

#  딕셔너리의 key만 출력 (방법 2: keys() 없이도 가능)
for k in sugang:
    print(k)

# 출력 결과:
# python
# cpp
# db
# datastructure

#  딕셔너리의 값(value)만 출력
for v in sugang.values():
    print(v)

# 출력 결과:
# kim
# sung
# kang
# park

#  딕셔너리 key-value 쌍을 튜플 형태로 출력
for s in sugang.items():
    print(s)

# 출력 결과:
# ('python', 'kim')
# ('cpp', 'sung')
# ('db', 'kang')
# ('datastructure', 'park')

#  정리 
# - `sugang = dict(python="kim", cpp="sung", db="kang")` → 딕셔너리 생성
# - `sugang['datastructure'] = 'kim'` → 새 key-value 추가
# - `sugang['datastructure'] = 'park'` → 기존 값 업데이트
# - `sugang['db']` → 특정 key의 값 조회
# - `sugang.get('opensource')` → 존재하지 않는 key 조회 (None 반환)
# - `sugang.get('opensource', 'not exist')` → 기본값을 설정하여 조회
# - `sugang.items()` → key-value 쌍 반환 (튜플)
# - `sugang.keys()` → key 목록 반환
# - `sugang.values()` → value 목록 반환