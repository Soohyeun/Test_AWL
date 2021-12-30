import random

awl = open("AWL2.csv",'r')

words = list()
sublist = list()
test_words = list()

# AWL 단어 불러오기
while True:
    words_list = awl.readline()
    words.append(words_list.rstrip().split(','))
    if not words_list: break
awl.close()


# sublist 리스트 내에 1~10까지 나누기
for i in range(1,10):
    sublist.append(words[(i-1)*60:i*60])
sublist.append(words[540:570])


#사용자에게 sublist 목록 받기
num = input('Select sublist number (1-10): ')
num = num.split(',')


#사용자가 원하는 sublist만 시험 보는 단어로 저장
for i in num:
    if int(i) <= 10 and int(i) >= 1:
        for j in sublist[int(i)-1]:
            test_words.append(j)
        print('add sublist%s'%i)

    else:
        print('Error: Please enter 1 to 10')
        exit()


#print(len(test_words))

ek = input('Press 1: Korean to English \npress 2: English to Korean \n')
print('Typing \'end\' to finish quiz')

#문제 출제
while True:
    if ek == '1':
        randnum = random.randint(0,len(test_words)-1)
        print(test_words[randnum][1])
        ans = input('answer: ')
        print("your answer: %s, answer: %s"%(ans,test_words[randnum][0]))


    elif ek == '2':
        randnum = random.randint(0,len(test_words)-1)
        print(test_words[randnum][0])
        ans = input('answer: ')
        print("your answer: %s, answer: %s"%(ans,test_words[randnum][1]))

    end = input('Next')
    if end == 'end':
        break
