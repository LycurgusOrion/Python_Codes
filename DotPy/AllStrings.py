
String_var = 'Python'
String_var = "Python"
String_var = """Python"""

String_var = """ This is a multiline
string and these are 
made by using triple quotes"""

substr_var = String_var.replace("world", "hello")
print (substr_var)

sample_str = 'Python String'

# return 1st character
print (sample_str[0])      

# return last character
print (sample_str[-1])      

# return last second character
print (sample_str[-2]) 

sample_str = 'Python String'

#return a range of character
print (sample_str[3:5])	    

# return all characters from index 7
print (sample_str[7:])      

# return all characters before index 6
print (sample_str[:6])      
print (sample_str[7:-4])

# to uppercase
print(sample_str.upper())
# to lowercase
print(sample_str.lower())

sample_str = "LOWERCASE IS NOT ALLOWED"
print(sample_str.isupper())
print(sample_str.islower())

sample_str = "A String Example Of Title String"
print(sample_str.istitle())

sample_str = "1234 ABCD"
print(sample_str.isalnum())

sample_str = "ASDF1"
print(sample_str.isalpha())

# length of string
print(len(sample_str))

sample_str = "Hello World!"
print(" ".join(sample_str))
print("".join(reversed(sample_str)))

print(sample_str.split())



