# Warmup-1 : monkey_trouble.py

def monkey_trouble(a_smile, b_smile):
  if(a_smile == True):
    if(b_smile == True):
      return True
    return False
  else:
    if(b_smile == True):
      return False
    return True
