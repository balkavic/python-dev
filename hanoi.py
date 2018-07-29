from datastructures.stack import Stack
import time

n = 26
transfers = 0

stack_i = Stack()
stack_j = Stack()
stack_k = Stack()

for i in reversed(range(n)):
    # print(".")
    stack_i.push(i)

start_time = time.time()


def transfer(from_stack, to_stack):
    global transfers
    transfers += 1
    to_stack.push(from_stack.pop())


def do_hanoi(n, stack_i, stack_j, stack_k):
    if n == 0:
        return
    do_hanoi(n - 1, stack_i, stack_k, stack_j)
    transfer(stack_i, stack_j)
    do_hanoi(n - 1, stack_k, stack_j, stack_i)


do_hanoi(n, stack_i, stack_j, stack_k)


def print_stack(stack):
    while (stack.peek() != None):
        print(stack.pop())


print("Stack i:")
print_stack(stack_i)

print("Stack j:")
print_stack(stack_j)

print("Stack k:")
print_stack(stack_k)

print("Transfers: %d" % transfers)

end_time = time.time()

# print("Time: %d" % (end_time - start_time) * 1000)
