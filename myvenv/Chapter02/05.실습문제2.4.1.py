# 실습문제 2.4.1
# 리스트 내포를 사용해서 word_list에 들어있는 문자열 중 
# 첫 글자자가 a인것만 뽑아서 리스트로 만드세요

# 변경전
# ['apple', 'watch', 'apolo','star','abocado']

# 변경후
# ['apple', 'apolo', 'abocado']

#내 코드
word_list = ['apple', 'watch', 'apolo','star','abocado']
word_list_a = [i for i in word_list if i[0] =='a' ] # if문에서 헷갈림[0]으로 첫번째 것만 골라낸다는 것을 생각못함
print(word_list_a)

#강사 코드
# 1. 리스트 내포를 사용하기 전
result = []
for word in word_list:
    if word[0] =='a':
        result.append(word)

print(result)

# 2. 리스트 내포를 사용한 후
result = [i for i in word_list if i[0]=='a'] # 맨처음 i는 몇씩 증가할것인지일듯
print(result)