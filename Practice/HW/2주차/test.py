from structures import LinkedList, Stack, Queue, HashTable
from prac import isPalindrome, is_valid_parenthesis, test_problem_queue

# 아이디어: Linked List -> 배열로 옮김
# 첫번째와 마지막을 꺼내서 같은지 확인하기


l1 = LinkedList()
for num in [1, 2, 2, 1]:
    l1.append(num)

l2 = LinkedList()
for num in [1, 2]:
    l2.append(num)

assert isPalindrome(l1)
assert not isPalindrome(l2)


##############################

def test_stack():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    assert stack.is_empty()


##################################

assert is_valid_parenthesis("()")
assert is_valid_parenthesis("()[]{}")
assert is_valid_parenthesis("({[][]})")
assert is_valid_parenthesis("({[]})")
assert not is_valid_parenthesis("(]")
assert not is_valid_parenthesis("(()]")
assert not is_valid_parenthesis("(((])")
assert not is_valid_parenthesis("((())")


#################################


def test_queue():
    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)

    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.pop() is None
    assert queue.is_empty()


###############################3

assert test_problem_queue(2) == 2
assert test_problem_queue(3) == 2
assert test_problem_queue(4) == 4
assert test_problem_queue(5) == 2
assert test_problem_queue(6) == 4
assert test_problem_queue(7) == 6

##################################

ht = HashTable()

ht.put(1, 1)
ht.put(2, 2)
assert ht.get(1) == 1
assert ht.get(2) == 2
assert ht.get(3) == -1

ht.put(12, 1)
ht.put(22, 2)
ht.put(32, 3)
assert ht.get(12) == 1
assert ht.get(22) == 2
assert ht.get(32) == 3

ht.remove(12)
assert ht.get(2) == 2
assert ht.get(12) == -1
assert ht.get(22) == 2
assert ht.get(32) == 3

ht.get(2)