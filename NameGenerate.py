import random
a= list(input('ваше имя: '))
p = int(input('Укажите ваш пол(1 = женский, 2 = мужской): '))
feend=['М','Т','Б','й','ц','к','н','г','ш','щ','з','х','ф','С','в','п','л','д','ж','ч','с','м','т','б']
gl = ['а','е','и','ё','у','ы','о','э','я','ю','Ё','Е','У','О','Ы','А','Э','Я','И', 'Ю']
ok = ['а','я']
ngl=[]
for i in range(len(a)):
    for b in range(len(gl)):
        if a[i]==gl[b]:
            ngl.append(a[i])
word=[]
b=''
for i in range(len(ngl)):
    word.append(random.choice(Sogl))
    word.append(ngl[i])
for i in range(len(word)):
    b+=word[i]
if a[-1]== 'я' or a[-1]== 'а' :
    b+='лини'
if p == 1:
    b+=random.choice(ok)
print(b)
