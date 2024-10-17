logs = "1 solve 09:00 50, 2 solve 10:00 60, 1 fail 11:00, 3 solve 13:00 40, 2 fail 14:00, 3 solve 15:00 70"

def analyze_competition(logs):
    # TODO: implement the function
    
    # Input: "1 solve 09:00 50, 2 solve 10:00 60, 1 fail 11:00, 3 solve 13:00 40, 2 fail 14:00, 3 solve 15:00 70"
    
    # Output: [(3, 110, 2, 0), (2, 60, 1, 1), (1, 50, 1, 1)]
    
    # Output [(student number, student score, successful attempts, unsuccessful attempts)]
    
    log_string = logs.split(', ')
    
    success_dic = {}
    fail_dic = {}
    score_dic = {}
    output = []
    
    for log in log_string:
        parts = log.split(' ')
        
        student_id, result, time = parts[0], parts[1], parts[2]        
        
        if result == 'solve':
            score = int(parts[3])
            if student_id in success_dic:
                success_dic[student_id] += 1
                score_dic[student_id] += score
            else:
                success_dic[student_id] = 1
                score_dic[student_id] = score
                
        elif result == 'fail':
            if student_id in fail_dic:
                fail_dic[student_id] += 1
            else:
                fail_dic[student_id] = 1
    
    for student_id in success_dic:
        score = score_dic.get(student_id, 0)
        successes = success_dic.get(student_id, 0)
        failures = fail_dic.get(student_id, 0)
        
        student_tuple = (int(student_id), score, successes, failures)
        
        output.append(student_tuple)
    
    output = sorted(output, key=lambda x: -x[1])
    
    return output
    
    
    
            
             
    