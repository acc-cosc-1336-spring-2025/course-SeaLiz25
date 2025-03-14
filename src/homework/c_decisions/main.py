#
def main():
       
       def get_user_input():
              option = input ("option: ")
              total = input("total: ")
              return option,total
       
       get_user_input()

       def get_options_ratio(option, total):
              ratio = float(option)/float(total)
    
              return float(ratio)

       def get_faculty_rating(ratio): 
              return rating = " "ratio >=0.9 and ratio <1

              if(ratio >=.9 and ratio <1):
                     rating = "Excellent"
              elif(ratio >=.8 and ratio <.9):
                     ratio = "Very Good"
              elif(ratio >=.7 and ratio <.8):
                     rating = "Good"
              elif(ratio >=0 and ratio <.59):
                     rating = "Unacceptable"

       option, total = get_user_input()
       ratio = get_options_ratio(option, total)
       rating = get_faculty_rating(ratio)
       

main()