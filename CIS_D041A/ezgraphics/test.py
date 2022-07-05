from ezgraphics import GraphicsWindow
X_SIZE= 640
Y_SIZE = 500
win = GraphicsWindow(X_SIZE, Y_SIZE)
canvas = win.canvas()
canvas.drawLine(0,0,X_SIZE,Y_SIZE)
canvas.drawLine(0,Y_SIZE,X_SIZE,0)
canvas.drawRect(15, 10, 20, 30)
#set out line to black
canvas.setOutline("red")
#set fill to green
canvas.setFill(0, 255, 0)
canvas.drawRect(100, 200, 100, 50)
canvas.drawLine(100,100,150,150)
#set fill to red
canvas.setFill("red")
#set out line to blue
canvas.setOutline(0,0,255)
# drawing a circle with a blue outline
canvas.drawOval(50,50,20,20)
# drawing a text with a blue outline
canvas.drawText(75,75,"Hello World!")
win.wait()