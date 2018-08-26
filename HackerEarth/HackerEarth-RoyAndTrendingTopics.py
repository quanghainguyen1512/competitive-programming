#HackerEarth-RoyAndTrendingTopics
from queue import PriorityQueue

class Topic:
    def __init__(self, id, score, change):
        self.id = id
        self.score = score
        self.change = change

    def __lt__(self, other):
        if self.change > other.change:
            return True
        return self.change == other.change and self.id > other.id

    @classmethod
    def fromString(topic, line):
        _id, z, p, l, c, s = map(int, line.split())
        newScore = p * 50 + l * 5 + c * 10 + s * 20
        change = newScore - z
        return topic(_id, newScore, change)


#### main
n = int(input())
topics = PriorityQueue()
while n != 0:
    line = input()
    topics.put(Topic.fromString(line))
    n -= 1
for i in range(5):
    topic = topics.get()
    print(topic.id, topic.score, sep = ' ')
