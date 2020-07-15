# Definition for a meeting
class Meeting:
    def __init__(self,start_time=0, end_time=0):
        self.start_time=start_time
        self.end_time=end_time
        
    def __repr__(self):
        return repr((self.start_time,self.end_time))
        
 # A function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges
def merge_ranges(meeting_list):
    
    merged_ml=[]
    # sort by start_time
    # https://docs.python.org/3/library/functions.html#sorted
    sorted_ml=sorted(meeting_list, key=lambda meeting:meeting.start_time)
    print("Sorted meeting list:", sorted_ml)
    
    i=0
    temp_m=sorted_ml[0]
    #print(len(sorted_ml))
    
    while (i<=(len(sorted_ml)-1)):
        #print("Index:",i,"Temp meeting:",temp_m)
        #print("Merged List",merged_ml,"\n")
        
        if (i == len(sorted_ml)-1):
            #print("I'm at the last item",i)
            merged_ml.append(temp_m)
            break

        # merge meeting time range if there is overlap
        if (temp_m.end_time >= sorted_ml[i+1].start_time):
            temp_m=Meeting(temp_m.start_time,max(temp_m.end_time,sorted_ml[i+1].end_time))
            #print("Temp meeting:",temp_m)
            
        # if there is no overlap, append the item to the final list
        else:            
            merged_ml.append(temp_m)
            temp_m=sorted_ml[i+1]
        
        i=i+1
            
    return merged_ml
    
# To test above function
    
"""
For example, given:
  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

Sorted meeting list:
  [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]

Your function would return:
  [(0, 1), (3, 8), (9, 12)]
"""

meeting_list=[Meeting(0, 1),
              Meeting(3, 5),
              Meeting(4, 8),
              Meeting(10, 12),
              Meeting(9, 10)]

merge_ranges(meeting_list)


# To test above function for end_time with big number
    
"""
For example, given:
  [(0, 1), (3, 15), (4, 8), (7, 10), (9, 10)]

Your function would return:
  [(0, 1), (3, 15)]
"""

meeting_list=[Meeting(0, 1),
              Meeting(3, 15),
              Meeting(4, 8),
              Meeting(10, 12),
              Meeting(9, 10)]

merge_ranges(meeting_list)
