from unittest import result

def get_options_ratio(option, total):
        ratio = option / total
    
        return float(ratio)

def get_faculty_rating(ratio): 
      rating = " "  

      if(ratio >=.9 and ratio <1):
             rating = "Excellent"
      elif(ratio >=.8 and ratio <.9):
             ratio = "Very Good"
      elif(ratio >=.7 and ratio <.8):
              rating = "Good"
      elif(ratio >=0 and ratio <.59):
             rating = "Unacceptable"
             



            
    

    
    
 

 





