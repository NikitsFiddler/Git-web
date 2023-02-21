print(1)
doska_=[[" "]*3 for i in range(3)]
num = 0
def doska():
    print()
    print("   |0|1|2|")
    print("---------")
    for i,row in enumerate(doska_):
        j_doska = f" {i} |{'|'.join(map(str,row))}|"
        print(j_doska)
        print("-----------")
print(1)

def hod():
  while True:
      hod_ = input("     Ваш ход:").split()

      if len(hod_) != 2:
          print("Введите 2 координаты")
          continue
      x, y = hod_

      if not (x.isdigit()) or not (y.isdigit()):
          print("Введите число")
          continue
      x, y = int(x), int(y)

      if 0 > x or x > 2 or 0 > y or y > 2:
          print("Вне диапозона ")
          continue

      if doska_[x][y] != " ":
          print(" координата занята ")
          continue
      return x, y



def win ():
  win_comb = (((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,2),(1,1),(2,0)),((0,0),(1,1),(2,2)),((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
  for comb in win_comb:
     symbols =[]

     for c in comb:
        symbols.append(doska_[c[0]][c[1]])
     if symbols == ["X","X","X"]:
       print("выйграл крестик")
       return True
     if symbols == ["0","0","0"]:
       print("выйграл нолик")
       return True
  return False


def hi ():
    print('-------------------' )
    print ('----привет---------------' )
    print('-----это игра крестики нолики--------------')
    print('-----ваша задача ставить Х и 0 на доске ,вписывая ее координаты-------------')
    print('-----победит то кто расположит свои три фигуры так что их можно будет соеденить прямой линией----')
    print('-----приступим!--------------')
hi()

num=0
while True:
    num+=1
    doska()
    if num % 2 == 1 :
      print ("ходит крестик")
    else:
      print("ходит нолик " )

    x,y = hod()

    if num % 2 == 1 :
        doska_[x][y] = "X"
    else:
        doska_[x][y] = "0"
    if win():
        break

    if num == 9 :
        print("Ничья")
        break
