inputValues = input().split()

W = int(inputValues[0])
H = int(inputValues[1])
x = int(inputValues[2])
y = int(inputValues[3])
r = int(inputValues[4])

answer = 'Yes'

if W < (x + r):
    answer = 'No'
if x < r:
    answer = 'No'

if H < (y + r):
    answer = 'No'
if y < r:
    answer = 'No'

print(answer)
