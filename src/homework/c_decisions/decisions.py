def get_options_ratio(option, total):
    result = option / total 
    
    return float(result)

def get_faculty_rating (get_options_ratio):
    if 0.9 <=get_options_ratio <1: 
        return "Excellent"
    if get_options_ratio > 0.8:
        return "Very Good"  
    if get_options_ratio > 0.7:
         return "Good"
    if get_options_ratio > 0.6:
        return "Needs Improvement"
    if get_options_ratio <0.59:
        return "Unnacceptable"
    
    
 

 





