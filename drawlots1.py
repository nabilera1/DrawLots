import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import csv


# 발표 순서를 랜덤하게 생성하고 결과를 표시하는 함수
def generate_order():
    global random_order  # 저장 기능에서 사용하기 위해 전역 변수로 선언
    N = int(entry.get())  # 사용자 입력을 받아 학생 수 N을 설정
    random_order = random.sample(range(1, N + 1), N)  # 1부터 N까지 숫자 중 N개를 랜덤하게 선택

    # 첫 번째 발표할 학생의 번호를 팝업창으로 보여주기
    messagebox.showinfo("첫 번째 발표자", f"첫 번째 발표할 학생의 번호는 {random_order[0]}입니다.")

    # 표(treeview)를 초기화
    for i in tree.get_children():
        tree.delete(i)

    # 랜덤하게 생성된 발표 순서를 표에 추가
    for i, number in enumerate(random_order, start=1):
        tree.insert("", "end", values=(i, number))


# 발표 순서를 CSV 파일로 저장하는 함수
def save_to_csv():
    if random_order:
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV 파일", "*.csv")])
        if filename:
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["발표 순서", "학생 번호"])
                for i, number in enumerate(random_order, start=1):
                    writer.writerow([i, number])
            messagebox.showinfo("저장 성공", f"'{filename}'로 저장되었습니다.")
    else:
        messagebox.showwarning("경고", "먼저 발표 순서를 생성해주세요.")


# 발표 순서를 TXT 파일로 저장하는 함수
def save_to_txt():
    if random_order:
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("텍스트 파일", "*.txt")])
        if filename:
            with open(filename, mode="w", encoding="utf-8") as file:
                for i, number in enumerate(random_order, start=1):
                    file.write(f"발표 순서 {i}: 학생 번호 {number}\n")
            messagebox.showinfo("저장 성공", f"'{filename}'로 저장되었습니다.")
    else:
        messagebox.showwarning("경고", "먼저 발표 순서를 생성해주세요.")


# 기본 tkinter 윈도우 설정
window = tk.Tk()
window.title("발표 순서 생성기")

# 전역 변수 초기화
random_order = []

# 중앙 정렬을 위해 프레임 설정
frame = tk.Frame(window)
frame.pack()

# 사용자 입력을 받는 엔트리 위젯 설정
entry_label = tk.Label(frame, text="학생 수:")
entry_label.pack(side=tk.LEFT)
entry = tk.Entry(frame, justify='center')
entry.pack(side=tk.LEFT)

# 발표 순서를 생성하는 버튼 설정
generate_button = tk.Button(frame, text="발표 순서 생성", bg="green", command=generate_order)
generate_button.pack(side=tk.LEFT)

# CSV로 저장 버튼
save_csv_button = tk.Button(frame, text="CSV로 저장", command=save_to_csv)
save_csv_button.pack(side=tk.LEFT)

# TXT로 저장 버튼
save_txt_button = tk.Button(frame, text="TXT로 저장", command=save_to_txt)
save_txt_button.pack(side=tk.LEFT)

# 표시할 발표 순서를 나타내는 표(treeview) 설정
# 표시할 발표 순서를 나타내는 표(treeview) 설정
tree = ttk.Treeview(window, columns=("발표 순서", "학생 번호"), show="headings")
tree.heading("발표 순서", text="발표 순서")
tree.heading("학생 번호", text="학생 번호")
# 컬럼 내용 가운데 정렬
tree.column("발표 순서", anchor='center')
tree.column("학생 번호", anchor='center')
tree.pack()

window.mainloop()