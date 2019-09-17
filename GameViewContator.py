from GameManageContrator import GameManageContrator
class GameConsoleView:
    def __init__(self):
        self.controller=GameManageContrator()

    #游戏入口
    def main(self):
        self.controller.mine()
        self.controller.print_mine_count()



    #绘界面
    def draw_map(self):
        print('  x 0  1  2  3  4  5  6  7  8')
        print('y   ==========================')
        for k in range(0,9):
            print('%d |'%k,end=' ')
            for i in self.controller.shade_map[k]:
                print(i,end='  ')
            print()

      #输入坐标开始游戏
    def check_mine_input(self):
        x=int(input('输入x坐标>>'))
        y=int(input('输入y坐标>>'))
        self.controller.find_blank(x,y)
        for item in self.controller.mine_set:
            self.controller.shade_map[item[0]][item[1]]=self.controller.map[item[0]][item[1]]
        self.controller.mine_set=[]

    #更新界面
    def up_date(self):
        while True:
            #开始选方格
            self.check_mine_input()
            #绘地图
            self.draw_map()
            # if self.controller.






if __name__ == '__main__':
    csv=GameConsoleView()
    csv.main()
    csv.draw_map()
    csv.check_mine_input()
    csv.draw_map()

