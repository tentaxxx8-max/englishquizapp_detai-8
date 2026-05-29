from question import create_question
from file_handler import save_result

# Khởi tạo điểm ban đầu
score = 0

# Tạo danh sách lưu các câu trả lời sai
wrong_answers = []

# Danh sách các đáp án hợp lệ
letters = ["A", "B", "C"]

print("=" * 35)
print("        QUIZ TIẾNG ANH")
print("=" * 35)
print("  1. Việt  ->  Anh")
print("  2. Anh   ->  Việt")
print("-" * 35)

#MỚI:
# Bắt người dùng chọn đúng chế độ 1 hoặc 2.
# Nếu nhập sai, chương trình sẽ yêu cầu nhập lại.
while True:
    try:
        mode = int(input("Chọn: ").strip())

        if mode in [1, 2]:
            break

        print("Chỉ được chọn 1 hoặc 2. Nhập lại!")

    except ValueError:
        print("Vui lòng nhập số 1 hoặc 2!")


# Lặp 10 lần để tạo 10 câu hỏi
for i in range(10):

    print("\n")
    print("Câu", i + 1)

    # Gọi hàm create_question(mode) và nhận 3 giá trị trả về:
    # question: câu hỏi
    # answers: danh sách 3 đáp án
    # correct: vị trí đáp án đúng
    question, answers, correct = create_question(mode)

    print(question)

    # In ra 3 đáp án A, B, C
    for j in range(3):
        print(f"{letters[j]}. {answers[j]}")

    # NOTE MỚI:
    # Nếu người dùng nhập ngoài A, B, C thì chương trình sẽ không tính sai.
    # Nó sẽ kệ đáp án đó và bắt nhập lại cho tới khi hợp lệ.
    while True:
        user = input("Đáp án: ").upper().strip()

        if user in letters:
            break

        print("Chỉ được nhập A, B hoặc C. Nhập lại!")

    # Chuyển A/B/C thành vị trí 0/1/2 để so sánh với biến correct
    index = letters.index(user)

    # So sánh đáp án người dùng với đáp án đúng
    if index == correct:
        print("Đúng")

        # Nếu đúng thì cộng điểm
        score += 1

    else:
        print("Sai")

        # Lưu lại câu sai, đáp án người dùng chọn và đáp án đúng
        text = (
            f"Sai câu {i + 1}: {question}"
            f" | Bạn chọn: {answers[index]}"
            f" | Đúng: {answers[correct]}"
        )

        wrong_answers.append(text)


# In kết quả sau khi làm xong 10 câu
print("\n===== KẾT QUẢ =====")
print(f"Điểm của bạn: {score}/10")

if len(wrong_answers) > 0:
    print("\nCác câu sai:")

    for x in wrong_answers:
        print(x)
else:
    print("\nBạn không sai câu nào!")


# Cuối cùng gọi hàm lưu kết quả
save_result(score, wrong_answers)

print("\nĐã lưu vào result.txt")