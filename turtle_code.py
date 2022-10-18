Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Pen()
t.shape("turtle")
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
for i in range(5):
    print(i)

    
0
1
2
3
4
for i in range(5):
    print(i, end=',')

    
0,1,2,3,4,
for i in range(2,9):
    print(i, end=',')

    
2,3,4,5,6,7,8,
for i in range(2,21,2):
    print(i, end=',')

    
2,4,6,8,10,12,14,16,18,20,
for i in range(2,21,4):
    print(i, end=',')

    
2,6,10,14,18,
t.reset()
for i in range(4):
    t.forward(200)
    t.left(90)

    
t.reset()
for i in range(60):
    t.forward(3 * i)
    t.left(45)

    
