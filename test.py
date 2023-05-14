line = "[[(}]]"
brackets = {"(": ")", "[": "]", "{": "}"}
brackets0 = {")": "(", "]": "[", "}": "{"}
a = list(line)
result = ''
tracker = {}
for i, j in enumerate(line):
    if j in brackets.keys():
        if brackets[j] in line[i::]:
            result = result + j
    elif j in brackets0.keys():
        if brackets0[j] in line[0:i]:
            result = result + j
for i in result:
    if i in brackets.keys():
        tracker[i] = result.count(i)
    elif i in brackets0.keys():
        tracker[i] = result.count(i)
print(result)
print(tracker)
for i in tracker.keys():
    if i in brackets.keys():
        if tracker[i] > tracker[brackets[i]]:
            result = result.replace(i, '', 1)
for i, j in enumerate(result):
    if j in brackets.keys() and i < len(result) and result[i+1] != brackets[j]:
        result = result.replace(j, '')
    elif j in brackets0.keys() and i < len(result):
        if result[i-1] != brackets0[j]:
            result = result.replace(j, '')

print(result)