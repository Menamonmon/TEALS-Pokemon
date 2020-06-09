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
            answer = [int(an) for an in answer.split(dilimeter)]
        else:
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
        
                