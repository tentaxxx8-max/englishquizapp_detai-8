from datetime import datetime

# Nhận điểm số và danh sách câu sai
def save_result(score, wrong_answers):
    
    #Mở file `result.txt` ở chế độ thêm
    with open("result.txt", "a", encoding="utf-8") as file:

        file.write("\n==========\n")
        
        #Ghi thời gian làm bài
        file.write(
            f"Thời gian: {datetime.now()}\n"
        )
        
        #Ghi số điểm đạt được.
        file.write(
            f"Điểm: {score}/10\n"
        )

        #Ghi các câu trả lời sai
        file.write("Câu sai:\n")

        for item in wrong_answers:
            file.write(item+"\n")