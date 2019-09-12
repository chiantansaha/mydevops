school = [['dia', 87],
          ['ria', 100],
          ['gud', 59],
          ['ria', 85],
          ['gud', 76],
          ['don', 99]]


res = {}
for x in school:
    res.setdefault(x[0],[]).append(x[1])

print(res)

for i in res:
    avg_score=sum(res[i])/len(res[i])
    print(avg_score)

#print(students)
    
    
