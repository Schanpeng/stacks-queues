# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         Saksorn Chanpeng 
# ASSIGNMENT:   Technical HW: Stacks & Queues

from Queue import Queue

# count longest sequence of duplicates in a queue
# can destroy the queue & make it empty
def count_longest(q):
  len = 1
  max = 0 
  length = q.size()

  while length > 0:
    length -= 1
    check = q.deq()
    current = q.front()

    if check == current:
      len += 1 
    else:
      print(check, current, len)
      if max < len:
        max = len
      len = 1 

    
  return max

    
    


      
      

def main():
    print("out 2:", count_longest( Queue( [ l for l in "hello" ] ) ))
    print("out 1:", count_longest(Queue([l for l in "m"])))
    print("out 4:", count_longest(Queue([l for l in "+__--___----__--_+"])))


# Don't run main on import
if __name__ == "__main__":
    main()

