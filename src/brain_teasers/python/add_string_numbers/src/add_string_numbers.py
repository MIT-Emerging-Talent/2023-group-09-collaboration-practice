def add_string_numbers(s1, s2):
    """
     a function for adding two string numbers together and returning the result as a string
     takes in s1 and s2 strings
     returns final, a string (sum of strings)

    """

    #check if atleast one of the numbers are floats so we can convert
    if "." not in s1 and "." in s2:
      s1 += "."
    if "." not in s2 and "." in s1:
      s2 += "."
    
    if  s1 or s2:
     #check to see how many numbers come after the decimal
       for i in range(len(s1)):
          if s1[i] == ".":
            savedigits1 = len(s1[i+1:(len(s1)-1)])
            break
    
       for i in range(len(s2)):
          if s2[i] == ".":
            savedigits2 = len(s1[i+1:(len(s2)-1)])
            break
       
#check which one has the longest decimal
    if savedigits1>savedigits2:
      diff = savedigits1 - savedigits2
      for i in range(diff):
            s2 += "0"
    elif savedigits2>savedigits1:
       diff = savedigits2 - savedigits1
       for i in range(diff):
            s1 += "0"
    carry = 0
    result = []
    # for i in s1[::-1]:
    #     for h in s2[::-1]:
#Calculate backwards with carry
    for i in range(len(s1)-1,-1,-1):
      if s1[i]==".":
          result.insert(0,'.')
          continue
        
      num1 = int(s1[i])
      num2 = int(s2[i])
    
      calc = num1 + num2 +carry
      carry = calc//10
      result.insert(0,str(calc%10))
    if carry:
      result.insert(0, str(carry))
    final = ''.join(result)
    
    return final