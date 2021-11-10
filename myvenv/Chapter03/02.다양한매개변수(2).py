# 1. 위치 가변 매개변수
def print_fruits(*args):
    for arg in args:
        print(arg)

print_fruits('apple', 'orange', 'mongo', 'grape')

# 2. 키워드 가변 매개변수
def comment_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


comment_info(name="파린이",content="정말 감사합니다.")