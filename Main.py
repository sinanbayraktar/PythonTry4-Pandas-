import matplotlib.pyplot as plt
y_axes = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x_axes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.plot (x_axes, y_axes)
plt.fill_between(x_axes, y_axes, 0, color="green")
plt.show()
plt.clf()
plt.scatter (x_axes, y_axes, s=[30, 40, 50], color = "purple", alpha=0.8)  #alpha is transparecy
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("X and Y values of points")
plt.yticks([1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], ["1b", "2b", "3b", "4b", "5b", "6b", "7b", "8b", "9b", "10b"])
plt.text(5, 25, 'middle')
plt.grid(True)
plt.show()
plt.clf()
list1 = [1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 3.8, 4.2, 4.3, 4.4]
plt.hist(list1, bins=4, range=[1, 5])
plt.show()
plt.clf()
