import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        return
    
    # Малюємо основну лінію (стовбур)
    t.forward(length)
    
    if level > 1:
        # Зберігаємо позицію та кут для правої гілки
        pos = t.position()
        angle = t.heading()
        
        # Поворот та малювання правої гілки
        t.right(45)
        draw_pythagoras_tree(t, length * math.sqrt(2)/2, level - 1)
        
        t.penup()
        t.setposition(pos)
        t.setheading(angle)
        t.pendown()
        
        # Поворот та малювання лівої гілки
        t.left(45)
        draw_pythagoras_tree(t, length * math.sqrt(2)/2, level - 1)
        
        t.penup()
        t.setposition(pos)
        t.setheading(angle)
        t.pendown()
    
    # Повертаємось до початку стовбура
    t.backward(length)

def main():
    screen = turtle.Screen()
    screen.title("Дерево Піфагора")
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)  
    t.left(90)   
    t.penup()
    t.goto(0, -200)
    t.pendown()
    
    # Запит рівня рекурсії у користувача
    level = int(turtle.textinput("Рівень рекурсії", "Введіть рівень рекурсії (рекомендовано 1-10):") or 5)
    
    # Малювання дерева
    t.color("green")
    draw_pythagoras_tree(t, 100, level)
    
    # Кінець
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()