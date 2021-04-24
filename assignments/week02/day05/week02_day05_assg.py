#   Give two examples each of typecasting between each of the following types:

#   a. string to boolean


string1 = "Shivam Singh"
print(string1, "data type", type(string1))
str_to_bool1 = bool(string1)
print(str_to_bool1, "data type", type(str_to_bool1))

string2 = "Shiv456Singh"
print(string2, "data type", type(string2))
str_to_bool2 = bool(string2)
print(str_to_bool2, "data type", type(str_to_bool2))
# (All non empty string will give true, empty string will give False)



#   b. integer to boolean


integer1 = 6306518466
print(integer1, "data type", type(integer1))
int_to_bool1 = bool(integer1)
print(int_to_bool1, "data type", type(int_to_bool1))

integer2 = 44
print(integer2, "data type", type(integer2))
int_to_bool2 = bool(integer2)
print(int_to_bool2, "data type", type(int_to_bool2))
# (non zero numbers will become true when converted to boolean)



#   c. boolean to string


boolean1 = True
print(boolean1, "data type", type(boolean1))
bool_to_str1 = str(boolean1)
print(bool_to_str1, "data type", type(bool_to_str1))

boolean2 = False
print(boolean2, "data type", type(boolean2))
bool_to_str2 = str(boolean2)
print(bool_to_str2, "data type", type(bool_to_str2))



#   d. string to integer


string1 = "8853289753"
print(string1, "data type", type(string1))
str_to_int1 = int(string1)
print(str_to_int1, "data type", type(str_to_int1))

string2 = "shivaMsingH4458"
print(string2, "data type", type(string2))
str_to_int2 = int(string2)
print(str_to_int2, "data type", type(str_to_int2))
# (Case of error: integer can contain nothing but digits.)


