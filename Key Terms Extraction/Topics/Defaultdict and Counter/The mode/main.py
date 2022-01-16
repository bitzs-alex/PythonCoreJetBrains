import collections

text = input()
counter = collections.Counter(text.split())
print(counter.most_common()[0][0])
