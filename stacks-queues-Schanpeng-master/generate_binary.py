# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:         Saksorn Chanpeng
# ASSIGNMENT:   Technical HW: Stacks & Queues

from Queue import Queue

# generate & return a queue of binary number strings from 1 to N
# front of queue begins @ '1', returns empty Queue otherwise
def generate_binary_numbers(N):
    numbers = Queue([])
    ans = Queue([])
    numbers.enq('1')

    while N > 0:
      N -= 1 
      front = str(numbers.deq())

      numbers.enq(front + '0')
      numbers.enq(front + '1')

      ans.enq(front)

    return ans

def main():
    generate_binary_numbers(5).print()


# Don't run main on import
if __name__ == "__main__":
    main()

