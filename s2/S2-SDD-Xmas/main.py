import xmas

xmas.grid()

xmas.background()

xmas.rectangle()
xmas.rectangle(100, 25)
xmas.rectangle(150, 50, 50)
xmas.rectangle(-100, -25, 100, 25, "green", 8, "blue")


xmas.triangle()
xmas.triangle(100, 25)
xmas.triangle(150, 50, 50)
xmas.triangle(-100, -25, 100, 25, "yellow", 2, "red")
xmas.triangle(-100, -25, -100, 25, "yellow", 4, "red")
xmas.triangle(-100, -25, -100, -25, "yellow", 6, "red")
xmas.triangle(-100, -25, 100, -25, "yellow", 8, "red")


xmas.star()
xmas.star(50, 50)
xmas.star(100, 100, "yellow")
xmas.star(-50, -50, "blue", 2)
xmas.star(-50, 50, "green", 0.5)


xmas.message(50, 50, "Hello", 20, "green")


xmas.leftTri(-100, -25, 100, 25, "yellow", 4, "red")
xmas.rightTri(100, 25, 100, 25, "yellow", 8, "red")

xmas.circle()
xmas.circle(100, 50, 20, "blue")
xmas.circle(-100, 50, 20, "blue", 8, "green")

