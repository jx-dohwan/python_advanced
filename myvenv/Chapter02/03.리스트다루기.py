# 리스트 메서드

# 리스트 데이터 삭제
fruits = ['apple','orange','mango']
del fruits[1]
print(fruits)

# 리스트 정렬
numbers = [5,2,3,5,1,2]
numbers.sort()
print(numbers)

# enumerate
titles = ['출석','뭘보노','138','237이다.']
for index, title in enumerate(titles, 1):
    print(f"{index}번째 글입니다. 제목 : {title}")