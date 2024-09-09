from collections import deque
def isPalindrome(ln):
    arr = []
    head = ln.head

    # 빈 배열인 경우
    if not head:
        return True

    # 모든 요소를 배열에 넣음
    node = head
    while node:
        arr.append(node.val)
        node = node.next

    # 길이가 1보다 클 떄 앞에 있는 배열과 맨 뒤에 있는 배열을 뽑음
    while len(arr) > 1:
        first = arr.pop(0)
        last = arr.pop()
        if first != last:
            print("false")
            return False

    print("true")
    return True


####################################

def is_valid_parenthesis(s):
    pair = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    opener = "({["
    stack = []

    for char in s:
        if char in opener:
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if pair[char] != top:
                return False

    return not stack


###################################

def test_problem_queue(num):
    deq = deque([i for i in range(1, num + 1)])
    while len(deq) > 1:
        deq.popleft()
        deq.append(deq.popleft())
    return deq.popleft()