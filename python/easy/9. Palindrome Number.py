# 9. Palindrome Number

def isPalindrome(x: int) -> bool:
  if(x < 0):
    return False # as negetive numbers will not be palindrome 

  temp = x
  check = 0
  while temp > 0:
    check *= 10
    check += temp % 10
    temp //= 10
  
  if check == x: 
     return True   

  return False

print(isPalindrome(1221))