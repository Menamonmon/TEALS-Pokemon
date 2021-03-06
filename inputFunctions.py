def take_number(prompt, min_val, max_val, dilimeter=None, dil_count=0):
    while True:
        answer = input(prompt).strip()
        if answer == '':
            print('An empty string is not a valid input.\n')
            continue
            
        if dilimeter is not None:
            if dilimeter not in answer:
                if dil_count > 0:
                    if dil_count != answer.count(dilimeter):
                        print(f'You need to input {dil_count + 1} values separated by "{dilimeter}".\n')
                        continue

                print(f'Your values need to be separated by {dilimeter}\n')
                continue
            else:
                if not answer.replace(dilimeter, "").isnumeric():
                    print(f'Please type numbers separated by {dilimeter} not a string')
                    continue

            answer = [int(an) for an in answer.split(dilimeter)]
            if len(set(answer)) < len(answer):
                print('You can not choose duplicate values. The values must be different.')
                continue

            elif len(answer) > dil_count + 1:
                print(f'You can only type {dil_count+1} values separated by a {dilimeter}.')
                continue
                
        else:
            if not answer.isnumeric():
                print('Your answer must be a single number.')
                continue 
                
            answer = [int(answer)]
    
        valid_values = True   
        for val in answer:
            if not (min_val <= val and val <= max_val):
                print(f'Invalid values. Your value(s) has to be between {min_val} and {max_val}\n')
                valid_values = False
                break

        if not valid_values:
            continue
            
        return answer

def take_command(prompt, correct_values):
    while True:
        answer = input(prompt).lower().strip()
        if answer not in correct_values:
            print(f'\nInvalid response. Your response must be one of the following:')
            print("    ", *correct_values)
            continue
        
        return answer

        
                