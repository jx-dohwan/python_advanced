# 제너레이터란

# 1. 이터레이터를 만드는 함수

def season_generator(*args):
    for arg in args:
        yield arg

g = season_generator('sprint','summer','autumn','winter')

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())


def func():
    print("첫번째 작업 중...")
    yield 1 # return을 하면 바로 끝난다.

    print("두번째 작업 중...")
    yield 2

    print("세번째 작업 중...")
    yield 3

ge = func()
data = ge.__next__()
print(data)

data = ge.__next__()
print(data)

data = ge.__next__()
print(data)