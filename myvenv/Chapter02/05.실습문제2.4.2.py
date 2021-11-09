# 실습문제 2.4.2
# 리스트 내포를 사용해서 다음과 같이 변경해보자

# 변경 전
# ['오메가3', None, '비타민C500', None, '홍삼절편']

# 변경 후
# ['오메가3','','비타민C500','','홍삼절편']

# 내 코드 -> 여기가 한계 ''없이 아예 None를 지움
word_list = ['오메가3', None, '비타민C500', None, '홍삼절편']
result = [i for i in word_list if i != None]
print(result)

# 강사코드
# 1. 리스트 내포 사용 전
itmes = ['오메가3', None, '비타민C500', None, '홍삼절편']
for item in itmes:
    if item != None:
        result.append(item)
    else:
        result.append('')
print(result)

#2. 리스트 내포 사용 후/else가 있는 경우 if를 for보다 먼저 사용 맨처음 i는 표현식
result = [i if i !=None else '' for i in itmes]
print(result)
