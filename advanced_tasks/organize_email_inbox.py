## TODO: Implement this function
    
# Input: "Sender Email Address1, Subject1, 09:00; Sender Email Address2, Subject2, 10:00; Sender Email Address1, Subject3, 12:00"
    
# Output: [("Sender Email Address1", 2), ("Sender Email Address2", 1)].

metadata = 'Sender Email Address1, Subject1, 09:00; Sender Email Address2, Subject2, 10:00; Sender Email Address1, Subject3, 12:00'

def organize_inbox(inbox_string):

    metadata_string = inbox_string.split('; ')

    output_dic = {}
    result = []

    for data in metadata_string:
        sender_email, subject, time = data.split(', ')

        if sender_email in output_dic:
            output_dic[sender_email] += 1
        else:
            output_dic[sender_email] = 1

    for key, value in output_dic.items():
        result += [(key, value)]

    sorted_result = sorted(result, key=lambda result: (-result[1], result[0]))

    return sorted_result

ans = organize_inbox(metadata)
print(ans)
