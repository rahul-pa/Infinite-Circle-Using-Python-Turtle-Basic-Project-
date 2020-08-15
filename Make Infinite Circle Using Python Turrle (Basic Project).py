import turtle

tu = turtle.Turtle()
tu.speed(1)

x = 1
i = 0
j = 0
k = 0
l = 0

while x < 100:
  tu.forward(2.5 + i + l)
  tu.right(90)
  tu.forward(2.5 + i + j)
  tu.right(90)
  tu.forward(2.5 + i + j )
  tu.right(90)
  tu.forward(5 + i + j)
  tu.right(90)
  
  print ("Box Number", x ,"/n")
  j = j+2.5
  k = k+2.5
  i = i+2.5
  l = j-2.5
  x = x+1