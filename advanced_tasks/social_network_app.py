# Problem in this unit centres around data from a social networking app.

# PROBLEM STATEMENT

# Social Networking App that allows users to form groups
# Each group = unique ID ranging (1 - n), n = total groups

# Function analyze_logs
# Input: String of logs 
# Output: list of tuples representing the groups with the longest lifetime
# CONDITION: lifetime = creation time to deletion time
# CONDITION: lifetime can include multiple instances of a group being created and deleted, in this case we sum the lifetime's
# CONDITION@ If multiple groupss have same lifetime, arrange in ascending order of ID

# Example:
# Input: "1 create 09:00, 2 create 10:00, 1 delete 12:00, 3 create 13:00, 2 delete 15:00, 3 delete 16:00"
# Output: [(2, '05:00')]

from datetime import datetime, timedelta  #Importing datetime for handling timestamps
    
log = '1 create 09:00, 2 create 10:00, 1 delete 12:00, 3 create 13:00, 2 delete 15:00, 3 delete 16:00'

def analyze_logs(logs):
    log_list = logs.split(", ") # Break down the log string into individual logs by splitting

    time_dic = {} # Key = G_D, Value = Time
    lifetime_dic = {}
    format = '%H:%M'

    for log in log_list:
        G_ID, action, time = log.split()
        G_ID = int(G_ID)
        time = datetime.strptime(time, format)

        if action == 'create':
            time_dic[G_ID] = time
        else:
            if G_ID in lifetime_dic:
                lifetime_dic[G_ID] += (time - time_dic[G_ID])
            else:
                lifetime_dic[G_ID] = (time - time_dic[G_ID])

    # Loop through lifetime_dic and convert each timedelta value using format_timedelta_easy()
    formatted_lifetime_dic = {G_ID: format_timedelta(lifetime) for G_ID, lifetime in lifetime_dic.items()}


    return formatted_lifetime_dic  #Return the list sorted in ascending order of the group IDs   

def format_timedelta(td):
    total_seconds = int(td.total_seconds())
    hours, minutes = divmod(total_seconds // 60, 60)
    return f"{hours:02}:{minutes:02}"  # Display in HH:MM format

    # THIS IS HOW TO SPLIT UP THE LOG LIST
    
ans = analyze_logs(log)
print(ans)





