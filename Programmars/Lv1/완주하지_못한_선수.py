'''
sort 후 확인하는 방법
해쉬로 풀어보기
'''

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
             return participant[i]
    
    return participant[-1]


# hash로 푼 버전
def solution_hash(participant, completion):
    hash_person = {}
    sum = 0
    for person in participant:
        hash_person[hash(person)] = person
        sum += hash(person)
    for c in completion:
        sum -= hash(c)
    return hash_person[sum]
    
print(solution_hash(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution_hash(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution_hash(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]	))