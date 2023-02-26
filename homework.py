import numpy as np

number = np.random.randint(1, 101) # предполагаемое число

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    num_max = 100
    min_num = 0
    predict_number = np.random.randint(1, 101) # предполагаемое число
    
    while True:
        count += 1
        
        if number > predict_number:
            min_num = predict_number + 1
            predict_number = (num_max + min_num ) // 2
            
        elif number < predict_number:
            num_max = predict_number - 1
            predict_number = (num_max + min_num ) // 2
            
        else:
            break # выход из цикла, если угадали
        
    return(count)

print(f'Количество попыток: {random_predict()}')