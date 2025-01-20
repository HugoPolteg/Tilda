from array import array
from  arrayQFile import ArrayQ
from linkedQFile import LinkedQ


if __name__ == "__main__":
    user_inputs = input()
    user_inputs = user_inputs.split(' ')
    user_input_arr = array('i')
    q = ArrayQ()
    for user_input in user_inputs:
        if user_input.isnumeric():
            q.enqueue(int(user_input.strip()))

    bord = []
    count = 0 
    while q.size() != 0:
        if count % 2 == 0:
            first = q.dequeue()
            q.enqueue(first)
        else:
            first = q.dequeue()
            bord.append(first)
        count += 1
    print(bord)