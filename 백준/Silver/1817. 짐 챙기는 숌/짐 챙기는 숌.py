#1817번 짐 챙기는 숌

book_num, box_weight = map(int, input().split())

tmp_box_weight = box_weight # 12
box_count = 0

if(book_num > 0):
    book_weight = list(map(int,input().split()))
    for i in range((len(book_weight))):
        if(tmp_box_weight == box_weight):
            box_count = box_count + 1
        if(book_weight[i] <= tmp_box_weight):
            tmp_box_weight = tmp_box_weight - book_weight[i]
        else:
            box_count = box_count + 1
            tmp_box_weight = box_weight - book_weight[i]
            
print(box_count)
