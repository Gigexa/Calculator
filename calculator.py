import customtkinter as ctk

root = ctk.CTk()
root.title("Custom Calculator")
root.geometry("300x500")

class Calculator:
	def __init__(self):
		self.frame_for_answer= ctk.CTkFrame(root, width = 299, height = 99, border_width = 1)
		self.frame_for_answer.pack(anchor="n",expand=True)
		self.frame_for_numbers = ctk.CTkFrame(root,width =300, height= 400)
		self.frame_for_numbers.pack(anchor="s",expand= True)
		self.label = ctk.CTkLabel(self.frame_for_answer, text ="",wraplength = 200)
		self.label.pack()
		self.put_numbers()
		self.put_operators()


	def put_operators(self):
		self.plus_b = ctk.CTkButton(self.frame_for_numbers, text = "+", width = 100,command = self.plus)
		self.plus_b.grid(column=0,row=3)
		self.minus_b = ctk.CTkButton(self.frame_for_numbers, text = "-", width = 100, command = self.minus)
		self.minus_b.grid(column=2,row=3)
		self.equals_b = ctk.CTkButton(self.frame_for_numbers, text = "=", width = 100, command = self.equals)
		self.equals_b.grid(column = 1, row=4)
		self.multiply_b = ctk.CTkButton(self.frame_for_numbers, text ="*", width = 100, command = self.multiply)
		self.multiply_b.grid(column =0,row =4)
		self.devide_b = ctk.CTkButton(self.frame_for_numbers, text ="/", width = 100, command = self.devide)
		self.devide_b.grid(column =2,row =4)
		self.bracket_a = ctk.CTkButton(self.frame_for_numbers, text = "(", width = 100, command = self.brackets_a)
		self.bracket_a.grid(column = 0,row = 5)
		self.bracket_b = ctk.CTkButton(self.frame_for_numbers, text = ")", width = 100, command = self.brackets_b)
		self.bracket_b.grid(column=1, row= 5)
		self.clear_b = ctk.CTkButton(self.frame_for_numbers, text = "C", width =100, command = self.clear)
		self.clear_b.grid(column=2, row= 5)

	def put_numbers(self):
		row = 0
		column = 0
		count = 1
		numbers = []
		for i in range(1,10):
			exec(f"numbers.append(ctk.CTkButton(self.frame_for_numbers, text = '{i}',width = 100, command = self.add_{i}))")
			exec(f"numbers[{i-1}].grid(column ={column}, row = {row})")

			column += 1
			if count %3 == 0:
				row+=1
				column = 0
			count+=1
		number0 = ctk.CTkButton(self.frame_for_numbers, text = "0",width = 100,command = self.add_0)
		number0.grid(column = 1, row = 3)


	def add_0(self):
		self.label.configure(text = self.label.cget("text")+"0")

	def add_1(self):
		self.label.configure(text = self.label.cget("text")+"1")
	def add_2(self):
		self.label.configure(text = self.label.cget("text")+"2")
	def add_3(self):
		self.label.configure(text = self.label.cget("text")+"3")
	def add_4(self):
		self.label.configure(text = self.label.cget("text")+"4")
	def add_5(self):
		self.label.configure(text = self.label.cget("text")+"5")
	def add_6(self):
		self.label.configure(text = self.label.cget("text")+"6")
	def add_7(self):
		self.label.configure(text = self.label.cget("text")+"7")
	def add_8(self):
		self.label.configure(text = self.label.cget("text")+"8")
	def add_9(self):
		self.label.configure(text = self.label.cget("text")+"9")


	def multiply(self):
		self.label.configure(text = self.label.cget("text")+"*")

	def devide(self):
		self.label.configure(text = self.label.cget("text")+"/")

	def equals(self):
		try:
			self.label.configure(text = str(eval(self.label.cget("text"))))
		except:
			pass

	def plus(self):
		self.label.configure(text = self.label.cget("text")+"+")
	def minus(self):
		self.label.configure(text = self.label.cget("text")+"-")


	def brackets_a(self):
		self.label.configure(text = self.label.cget("text")+"(")

	def brackets_b(self):
		self.label.configure(text = self.label.cget("text")+")")


	def clear(self):
		self.label.configure(text = "")

calculator = Calculator()

root.mainloop()