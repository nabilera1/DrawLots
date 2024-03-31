import tkinter as tk
from tkinter import ttk
import random


# 발표 순서를 랜덤하게 생성하고 결과를 표시하는 함수
def generate_order():
    N = int(entry.get())  # 사용자 입력을 받아 학생 수 N을 설정
    random_order = random.sample(range(1, N + 1), N)  # 1부터 N까지 숫자 중 N개를 랜덤하게 선택

    # 표(treeview)를 초기화
    for i in tree.get_children():
        tree.delete(i)

    # 랜덤하게 생성된 발표 순서를 표에 추가
    for i, number in enumerate(random_order, start=1):
        tree.insert("", "end", values=(i, number))


# 기본 tkinter 윈도우 설정
window = tk.Tk()
window.title("발표 순서 생성기")

# 중앙 정렬을 위해 프레임 설정
frame = tk.Frame(window)
frame.pack()

# 사용자 입력을 받는 엔트리 위젯 설정
entry_label = tk.Label(frame, text="학생 수:")
entry_label.pack(side=tk.LEFT)
entry = tk.Entry(frame, justify='center')
entry.pack(side=tk.LEFT)

# 발표 순서를 생성하는 버튼 설정
generate_button = tk.Button(frame, text="발표 순서 생성", command=generate_order)
generate_button.pack(side=tk.LEFT)

# 표시할 발표 순서를 나타내는 표(treeview) 설정
tree = ttk.Treeview(window, columns=("발표 순서", "학생 번호"), show="headings")
tree.heading("발표 순서", text="발표 순서")
tree.heading("학생 번호", text="학생 번호")
# 컬럼 내용 가운데 정렬
tree.column("발표 순서", anchor='center')
tree.column("학생 번호", anchor='center')
tree.pack()

window.mainloop()
