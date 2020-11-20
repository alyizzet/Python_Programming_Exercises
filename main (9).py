class Divider():
  def func():
    students = int(input())
    pens = int(input())
    each_gets = pens // students
    remainder = pens%students
    return print(each_gets),print(remainder)
    
Divider.func()