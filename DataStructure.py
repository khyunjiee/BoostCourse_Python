# Collections
# List, Tuple, Dict에 대한 Python Built-in 확장 자료 구조 (모듈)
# 편의성, 실행 효율 등을 사용자에게 제공함
# deque, Counter, OrderedDict, defaultdict, namedtuple의 모듈이 존재함

# deque
# Stack과 Queue를 지원하는 모듈
# List에 비해 효율적인 자료 저장 방식을 원함
# deque는 기존 list보다 효율적인 자료구조를 제공
# 효율적 메모리 구조로 처리 속도 향
from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)

deque_list.appendleft(10)
print(deque_list)

deque_list.rotate(2)
print(deque_list)
deque_list.rotate(2)
print(deque_list)

deque_list.extend([5, 6, 7])
print(deque_list)
deque_list.extendleft([5, 6, 7])
print(deque_list)

print(deque(reversed(deque_list)))

# OrderedDict
# Dict와 달리, 데이터를 입력한 순서대로 dict를 반환함
# Dict type의 값을 value 또는 key 값으로 정렬할 때 사용 가
from collections import OrderedDict

d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k, v in d.items():
    print(k, v)

for k, v in OrderedDict(sorted(d.items(), key = lambda t: t[0])).items():
    print(k, v)

for k, v in OrderedDict(sorted(d.items(), key = lambda t: t[1])).items():
    print(k, v)

# defaultdict
# Dict type 값에 기본 값을 지정, 신규 값 생성시 사용
from collections import defaultdict

d = defaultdict(object)     # Default dictionary를 생성
d = defaultdict(lambda: 0)      # Default 값을 0으로 설정
print(d["first"])

word_count = defaultdict(object)
word_count = defaultdict(lambda: 0)
text = "A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was created for the bliss of souls like mine. I am so happy, my dear friend, so absorbed in the exquisite sense of mere tranquil existence, that I neglect my talents. I should be incapable of drawing a single stroke at the present moment; and yet I feel that I never was a greater artist than now. When, while the lovely"

for word in text.lower().split():
    word_count[word] += 1

for i, v in OrderedDict(sorted(
    word_count.items(), key = lambda t: t[1],
    reverse = True)).items():
    print(i, v)

# Counter
# Sequence type의 data element들의 갯수를 dict 형태로 반환
from collections import Counter

c = Counter()       # a new, empty counter
c = Counter('gallahad')     # a new counter from an iterable
print(c)

# namedtuple
# Tuple 형태로 Data 구조체로 저장하는 방법
# 저장되는 data의 variable을 사전에 지정해서 저장함
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y = 22)
print(p[0], p[1])

x, y = p
print(x, y)
print(p.x + p.y)
print(Point(x = 11, y = 22))
