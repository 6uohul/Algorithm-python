import heapq

def time_convert(string):
    hh, mm = map(int, string.split(":"))
    return hh * 60 + mm

def solution(book_time):
    answer = 0
    book_time.sort(key=lambda x: x[0])
    heap = [] # 종료 시간이 담긴 최소힙

    for start, end in book_time:
        start_time = time_convert(start)
        end_time = time_convert(end)

        # 처리할 방이 남아있고, 다음 시작시간이 끝나는 시간보다 더 클 떄 (예약가능)
        if heap and start_time >= heap[0]:
            heapq.heappop(heap)
        else:
            answer += 1

        heapq.heappush(heap, end_time)
    
    print(answer)
    return answer
    



solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])