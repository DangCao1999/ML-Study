def isPalindrome( x: int) -> bool:
        if x <= 0:
            return False
        temp = str(x)
        temp2 = ""
        for i in temp:
            temp2 = i + temp2
        
        if(temp == temp2):
            return True            
        
        return False

rs = isPalindrome(10)

print(rs)