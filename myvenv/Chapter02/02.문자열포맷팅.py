# 문자열 포맷팅이 없다면?
# 기준님 수강기간이 7일 남았습니다.

name = "기준"
duration = 7

message = name + '님 수강기간이 ' + str(duration) + "일 남았습니다."
print(message)

# 문자열 포맷팅 사용시
message_format = f"{name}님 수강기간이 {duration}일 남았습니다."
print(message_format)

# format 메서드 사용
a = 'hello {1}{0}{2}'.format('apple','pineapple','pen')
print(a)

b = 'hello {}{}{}'.format('apple','pineapple','pen')
print(b)

# f-string 사용
name1 = 'apple'
name2 = 'pineapple'
name3 = 'pen'

c = f"hello {name1}{name2}{name3}"
print(c)