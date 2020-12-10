



def main():

    user_records = []   # To hold all N number of users record (i.e list of dictionaries)
    user_record = {}    # To hold each user record
    information = ['roll_num', 'name', 'age', 'marks']    # list of information that will be asked in input.

    for i in range(5):
        user_record = {}  # for each next user, it will reset 
        print(f'\n-----Enter student no.{i+1} information------')
        for j in range(len(information)):

            # Checking whether input is integer or string [Validation]
            if (j == 0 or j == 2 or j == 3):
                answer = int(input(f'\nEnter the {information[j]}: '))
                if j == 0:
                    while answer < 0:
                        answer = int(input(f'\nPlease input a valid {information[j]}: '))

                    # updating or creating(if not exist) new key with corresponding user input value. 
                    user_record.update({information[j]: answer})
                
                elif j == 2:
                    while not(answer > 0 and answer < 100):
                        answer = int(input(f'\nPlease input a valid {information[j]}: '))
                    user_record.update({information[j]: answer})
                
                elif j == 3:
                    while not(answer > 0 and answer < 100):
                        answer = int(input(f'\n{information[j]} cannot be less than 0 and greater than 100, Enter again: '))
                    user_record.update({information[j]: answer})

            else:
                answer = input(f'\nEnter the student\'s {information[j]}: ')
                user_record.update({information[j]: answer})

        user_records.append(user_record)
       
    # Returning all 5 user records and keys information
    return user_records, information


def show_data_in_tabular_form(keys, user_records):
    '''
        Formatting and Displaying user data in tabular form.
    '''

    print('\n')
    for key in keys:
        print(f' {key}', end='    |        ')
    print('\n')
    for user in user_records:
        for key, value in user.items():
            print(f' {value}', end='      |      ')
        print('\n')


def calulate_and_show_class_average_highest_lowest(user_records):
    
    # Getting the marks key from user dictionary and appending to list students_marks
    students_marks = [user['marks'] for user in user_records]

    average = sum(students_marks) / len(user_records)
    highest = max(students_marks)
    lowest = min(students_marks)

    print(f'The class Average is {average}')
    print(f'The class highest is {highest}')
    print(f'The class lowest is {lowest}')


    
if __name__ == '__main__':
    user_records, information = main()
    
    show_data_in_tabular_form(information, user_records)
    calulate_and_show_class_average_highest_lowest(user_records)