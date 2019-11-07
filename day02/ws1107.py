
# 배열의 길이를 구하는 함수는 len(배열)
# 반올림 하는 함수는 round(숫자, 소숫점)
# 1. 평균을 구하세요.
score = {
    "수학": 90,
    "영어": 87,
    "한국지리": 92
}

size = len(score)
avg = 0
for tmp in score.values():
    avg += tmp
print(avg)
avg = avg/size
print(round(avg,1))

'''
if 조건1:
    a
elif 조건2:

else:
    a

'''

# 2. 각 학생의 평균 점수와 반 평균을 구하세요.
scores = {
    "a학생": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "b학생": {
        "수학": 100,
        "국어": 70,
        "음악": 80
    },
}

size = len(scores["a학생"])
avg_a = 0
for tmp in scores["a학생"].values():
    avg_a += tmp
print(avg_a)
avg_a = avg_a/size
print(round(avg_a,1))


size = len(scores["b학생"])
avg_b = 0
for tmp in scores["b학생"].values():
    avg_b += tmp
print(avg_b)
avg_b = avg_b/size
print(round(avg_b,1))

print("here")


for tmp1 in scores.values():
    for tmp2 in tmp1.values():
        avg += tmp2
print(avg)
avg = avg/size
print(round(avg))

