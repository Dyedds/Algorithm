#1181번

N = int(input())
words = []
for i in range(N):
    words.append(input())
words = list(set(words))            #중복제거
words.sort()                        #사전순 정렬
words.sort(key = lambda x: len(x))  #길이순 정렬
for i in words:
    print(i)
