
def palindrome( string ):
  string =  ''.join(string.split(' ')).lower()
  return string == string[::-1] 
 
is_palindrome = palindrome('101')
print(is_palindrome)


#passportjs paquete npm
