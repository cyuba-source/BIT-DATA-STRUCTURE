stack=[]
stack.append("deposit")
stack.append("transfer")
stack.append("pay bills")

stack.pop()
print(stack)

stack=[]
stack.append("Read notes")
stack.append("do exercises")
stack.append("Rivise past papers")
stack.pop()
stack.pop()
print(stack)

stack=[]
stack.append("task1")
stack.append("task2")
stack.append("task3")
stack.pop()
stack.append("task4")
print(stack)

Queue=[]
Queue.append("1 bus")
Queue.append("2 bus")
Queue.append("3 bus")
Queue.append("4 bus")
Queue.append("5 bus")
Queue.append("6 bus")
Queue.append("7 bus")
Queue.pop(0)
Queue.pop(0)
Queue.pop(0)
print("Queue after 3 bus depart:",Queue[0])

Queue=[]
Queue.append("1 patient")
Queue.append("2 patients")
Queue.append("3 patients")
Queue.append("4 patients")
Queue.append("5 patients")
Queue.pop(0)
print("print patient who served second:",Queue[0])