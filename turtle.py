#!/usr/bin/env python3

# Turtle program draws 6 hexagones in a comb

from turtle import shape

shape("turtle")

from turtle import forward, left, right,penup, pendown, exitonclick

#Nakresli 6 hexagonů
for i in range(6):

    #nakresli hexagon
    forward(50)
    left(60)
    forward(50)
    left(60)
    forward(50)
    left(60)
    forward(50)
    left(60)
    forward(50)
    left(60)
    forward(50)
    left(60)
    forward(50)
    right(60)
    
     
exitonclick()
    
    
