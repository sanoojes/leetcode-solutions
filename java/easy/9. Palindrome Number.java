// 9. Palindrome Number

class Solution {
  public boolean isPalindrome(int x) {
      if (x < 0) return false;

      int a = x;
      int b = 0;
      
      while(a>0){
          b *= 10;
          b += a % 10;
          a /= 10;
      }

      if (b == x) return true;

      return false;
  }
}