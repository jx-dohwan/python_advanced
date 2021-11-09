# 1. replace
# 문자열 고체
a = '오늘 날씨는 흐림입니다.'.replace("흐림","맑음")
print(a)

# 2. find
# 문자열 찾기
b = 'Hello world'.find('world')
print(b)

# 3. split
# 문자열 분리
d = '나이키:신말 265 X1212 78000'.split(':')
print(d)

# 4. strip
# 문자열 공백 제거
e = '    Yeah   '.lstrip()
f = '    Yeah   '.rstrip()
g = '    Yeah   '.strip()
print(e)
print(f)
print(g)