my_list=["madam","bab","shweta"]

def palindrome(my_list):
     palindrome_list=[]
     for word in my_list:
          if word==word[::-1]:
               palindrome_list.append(word)
          
     return palindrome_list
    



print(palindrome(my_list))




          
          