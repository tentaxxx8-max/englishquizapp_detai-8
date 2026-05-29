import random
from data import vocab


def create_question(mode):
    #Chọn ngẫu nhiên 1 từ trong danh sách
    word = random.choice(vocab)
    
    #Tách ra từ tiếng Việt và tiếng Anh
    vn = word[0]
    en = word[1]

    wrong = []
    
    #Sinh thêm 2 đáp án sai.
    while len(wrong) < 2:
        temp = random.choice(vocab)

        if mode == 1:
            candidate = temp[1]

            if candidate != en and candidate not in wrong:
                wrong.append(candidate)

        else:
            candidate = temp[0]

            if candidate != vn and candidate not in wrong:
                wrong.append(candidate)
    
    #Tạo câu hỏi theo chế độ đã chọn            
    if mode == 1:
        answers = [en] + wrong
        question = f'"{vn}" tiếng Anh là gì?'

    else:
        answers = [vn] + wrong
        question = f'"{en}" tiếng Việt là gì?'
     
     #Trộn ngẫu nhiên vị trí đáp án   
    random.shuffle(answers)

    correct = answers.index(en if mode == 1 else vn)

    #Trả về 3 giá trị:
    return question, answers, correct