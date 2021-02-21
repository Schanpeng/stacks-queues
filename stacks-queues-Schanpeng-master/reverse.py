# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Saksorn Chanpeng (Joey)
# ASSIGNMENT:   Technical HW: Stacks & Queues

from Queue import Queue
from Stack import Stack


# Return a new queue in reverse order
# Hint: can use a stack to help
def reverse(q_orig):
  q_new = Queue([])
  s = q_orig.size()-1
  while (not q_new.size() == q_orig.size()):
    q_new.enq(q_orig.queue[s])
    s -= 1 

  return q_new

def main():
    q = Queue(list(range(1,-10, -1)))
    q.print()
    print("reverse: ", end="")
    reverse(q).print()

# Don't run main on import
if __name__ == "__main__":
    main()