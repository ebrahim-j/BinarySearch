class BinarySearch(list):

  def __init__(self, a, b): 
    self.a = a
    self.b = b
         
    for item in range(self.a): #Initializes list of length a with steps of b between consecutivevalues
      list.append(self, self.b)
      
      self.b += b
      
    self.length = item + 1  #increments to the value of length of the array(item is current index NOT length)

  def search(self,value):
    first = 0
    last = self.length - 1
    
    found = False #flag
    tally = 0 #tally counter for amoun of time iteration occurs
    
    i = None #initialize index variable
    
    listMember = False #initialize kind of isinstance checker
    
    try: #checks to see if value in array and handles exception if not
      i = self.index(value)
      listMember = True
    except ValueError:
      i = -1
      listMember = False
    
    
    #provided these conditions are met, search will keep looping
    while first <= last and not found and listMember and value != self[last]: 
        midpoint = (first + last) // 2 #narrowing the search 
        mid_value = self[midpoint] 
        if mid_value == value: #keep looping till this condition is met
            found = True
            tally += 1
            i = midpoint
        else:
            if value < mid_value: #means value is in lower half of array
                last = midpoint - 1
                tally += 1
            else:
                first = midpoint + 1 #value in upper half of array
                tally += 1
    
    
    return {"count": tally, "index": i}
