# Implement queue using python

queue=[]

#Enqueue

queue.append(78)
queue.append(56)
queue.append(12)
queue.append(67)

print("Queue: " , queue)

#Dequeue

print("Removed: ", queue.pop(0))

print("Queue after dequeue: ", queue)

#Front

print("First Element: ",queue[0])

#Check Empty

if len(queue)==0:
    print("Queue is empty!")
else:
    print("Queue is not empty! ")    