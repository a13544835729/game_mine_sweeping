'''
*表示地雷
'''
import random
class GameManageContrator:
   def __init__(self):
       self.map=[
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
       ]
       self.mine_num=[]
       self.mine_set=[]
       self.shade_map=[
           ['#','#','#','#','#','#','#','#','#'],
           ['#','#','#','#','#','#','#','#','#'],
           ['#','#','#','#','#','#','#','#','#'],
           ['#','#','#','#','#','#','#','#','#'],
           ['#','#','#','#','#','#','#','#','#'],
           ['#','#','#','#','#','#','#','#','#'],
           ['#','#','#','#','#','#','#','#','#'],
           ['#','#','#','#','#','#','#','#','#'],
           ['#','#','#','#','#','#','#','#','#'],
       ]

    #随机生成地雷
   def mine(self):
       for i in range(10):
           x = random.randint(0,8)
           y = random.randint(0,8)
           if self.map[x][y]==0:
               self.map[x][y]='*'

    #打印地雷地图
   def print_mine_count(self):
       for x in range(0,9):
           for y in range(0,9):
               if self.map[x][y] != '*':
                    self.map[x][y]= self.cacula_mine_count(x,y)


    #计算每个方格四周的地雷数量
   def cacula_mine_count(self,x,y):
            if self.map[x][y]!='*':
               #每次循环列表归零
                self.mine_num = []
                if  x-1>=0 and y-1>=0:
                    self.mine_num.append(self.map[x-1][y-1])
                if x-1>=0 :
                    self.mine_num.append(self.map[x-1][y])
                if x-1>=0 and y+1<=8:
                    self.mine_num.append(self.map[x-1][y+1])
                if y-1>=0:
                    self.mine_num.append(self.map[x][y-1])
                if y+1<=8:
                    self.mine_num.append(self.map[x][y+1])
                if x+1<=8 and y-1>=0:
                    self.mine_num.append(self.map[x+1][y-1])
                if x+1<=8:
                    self.mine_num.append(self.map[x+1][y])
                if x+1<=8 and y+1<=8:
                    self.mine_num.append(self.map[x+1][y+1])
                return  self.mine_num.count('*')

    #如果为非雷且其周围一圈的地雷数量为0，
    # 则自动翻开其周围一圈的方格，
    # 再检测是否还存在数量为0的方格，
    # 如有则继续翻开其周围一圈方格，
    # 直至没有数量为0的方格为止。
   def find_blank(self,x,y):
        # if self.cacula_mine_count(x,y)!=0 :
        #     return
        if self.cacula_mine_count(x, y) == 0 :
            #选中其周围一圈的方格
             if x - 1 >= 0 and y - 1 >= 0 and (x-1,y-1) not in self.mine_set:
                 self.mine_set.append((x-1,y-1))
                 self.find_blank(x-1,y-1)
             if x - 1 >= 0 and (x-1,y) not in self.mine_set:
                 self.mine_set.append((x-1,y))
                 self.find_blank(x-1, y)
             if x - 1 >= 0 and y + 1 <= 8 and (x-1,y+1) not in self.mine_set:
                 self.mine_set.append((x-1,y+1))
                 self.find_blank(x - 1, y+1)
             if y - 1 >= 0 and (x,y-1) not in self.mine_set:
                 self.mine_set.append((x,y-1))
                 self.find_blank(x, y - 1)
             if y + 1 <= 8 and (x,y+1) not in self.mine_set:
                 self.mine_set.append((x,y+1))
                 self.find_blank(x, y+1)
             if x + 1 <= 8 and y - 1 >= 0 and (x+1,y-1) not in self.mine_set:
                 self.mine_set.append((x+1,y-1))
                 self.find_blank(x+1, y-1)
             if x + 1 <= 8 and (x+1,y) not in self.mine_set:
                 self.mine_set.append((x+1,y))
                 self.find_blank(x+1, y)
             if x + 1 <= 8 and y + 1 <= 8 and (x+1,y+1) not in self.mine_set:
                 self.mine_set.append((x+1,y+1))
                 self.find_blank(x+1, y+1)

    #游戏失败,并选出所有地雷的坐标
   def is_game_over(self,x,y):
       mine=[]
       if self.map[x][y]=='*':
           for i in range(0,9):
               for j in range(0,9):
                   if self.map[i][j]=='*':
                       mine.append((i,j))
       return mine


    #游戏通关,选出除了地雷外的所有方块
   def is_game_win(self):
       pass



if __name__ == '__main__':
    manage=GameManageContrator()
    manage.mine()
    manage.print_mine_count()
    for i in manage.map:
        for c in i:
            print(c, end=' ')
        print()

    print()

    for i in manage.shade_map:
        for c in i:
            print(c, end=' ')
        print()

    manage.find_blank(0,0)
    print(manage.mine_set)
