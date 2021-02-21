# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         Saksorn Chanpeng
# ASSIGNMENT:   Technical HW: Stacks & Queues

from Stack import Stack


# Returns True if the braces match,
# & False otherwise
def matcher(str):
    stack = []
    new = []

    str = str.replace(" ","")
    for char in str:
        if char in ["(", "{", "[","}",")","]"]:
            new.append(char)
    str = "".join(new)
    if not str:
        return True
    for char in str:
      if char in ["(", "{", "["]:
        stack.append(char)
      else:
        if not stack:
          return False
        current_char = stack.pop()
        if current_char == '(':
          if char != ")":
            return False
        if current_char == '{':
          if char != "}":
            return False
        if current_char == '[':
          if char != "]":
            return False
    if stack:
      return False
    return True


def main():
    print("matcher: ", matcher("[]"))


# Don't run main on import
if __name__ == "__main__":
    main()
