import collections

queue = collections.deque()

#append() - add to the right
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

#appendleft() - add to the left
queue.appendleft(9)

print(f"Queue: {queue}")
# [1,2,3,4,5] since it is a queue (FIFO)

#---------------------------------------------

#popleft() - remove from the left
print(queue.popleft())

#pop() - remove from the right
print(queue.pop())

print(f"Queue: {queue}")

#---------------------------------------------

#index(ele, beg, end):
#This function returns the first index of the value mentioned
#in arguments, starting searching from beg till end index.
print(f"Index of 3: {queue.index(3,0,len(queue))}")

#insert(i, a):
#This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
queue.insert(2, 33)

print(f"Queue: {queue}")

#remove(a) - remove the first occurance of the value 'a'
queue.remove(33)

print(f"Queue: {queue}")

#count(a) - count the number of occurances of the value 'a'
print(f"Count of 2: {queue.count(2)}")

#len(queue) - get the length of the queue
print(f"Length of queue: {len(queue)}")

#extend(iterable) - extend the queue by adding all elements (on the right) from iterable
queue.extend([11,22,33,44])

print(f"Queue: {queue}")

#extendleft(iterable) - extend the queue by adding all elements (on the left) from iterable

queue.extendleft([99,88,77,66])

print(f"Queue: {queue}")

#reverse() - reverse the queue
queue.reverse()

print(f"Queue: {queue}")

#rotate(n) - rotate the queue by n elements to the right
queue.rotate(2)

print(f"Queue: {queue}")

#rotate(-n) - rotate the queue by n elements to the left

queue.rotate(-2)

print(f"Queue: {queue}")
#---------------------------------------------
