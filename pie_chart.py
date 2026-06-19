import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "History"]
marks = [30, 25, 20, 25]

plt.pie(marks, labels=subjects, autopct="%1.1f%%")

plt.title("Subject Distribution")

plt.show()