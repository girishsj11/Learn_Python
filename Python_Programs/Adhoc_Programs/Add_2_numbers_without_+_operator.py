#Adding two numbers with using an arithmatic + operator .

def add_two_numbers_without_plus_operator(a,b):
  data = 0
  while b!=0:
    data = a&b
    a=a^b
    b=data<<1
    
  return a

if __name__ == "__main__":
  print(add_two_numbers_without_plus_operator(5,10))
    
