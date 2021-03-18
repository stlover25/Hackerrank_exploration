def count_numbers(sorted_list, less_than):
    start = 0
    end = len(sorted_list)-1
    
    while start <= end:
        
        mid = (start+end)//2        

        if mid in [start, end]:

            if sorted_list[start] == less_than or less_than < sorted_list[start]:
                
                return start

            elif sorted_list[end] == less_than:
                return end
            elif less_than > sorted_list[end]:
                return end+1
        

        
        if sorted_list[mid] < less_than:
            start = mid+1
            
                        
        elif sorted_list[mid] > less_than:
            end = mid-1
            
        else: 
            return mid
