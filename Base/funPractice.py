def find_max(lst):
    if len(lst) == 0:
        return None
    result = lst[0]
    for i in range(1,len(lst)):
        if lst[i] > result:
            result = lst[i]
    return result

a = [2,3,41,3,1,3]

print(find_max(a))


dic = {
    '语文': 90,
    '数学': 97,
    '英语': 98
}

def find_score(score_dic):
    max_score = 0
    max_course = ''
    for course,score in score_dic.items():
        if score > max_score:
            max_score = score
            max_course = course
        return max_course,max_score

print(find_score(dic))