'''
Reversy() : 리버시(오델로) 게임
'''
'''
1. print_field : 게임 보드 출력
2. able_list : 수를 둘 수 있는 위치 체크
3. end checker : 게임 끝을 확인
4. find_next : 
5. put_mark
6. reverse
7. count_score
8. print_log
9. print_result
10. game_start : 게임 시작
'''
'''
기능 1 : 리버시 환경 출력
기능 2 : 리버시 환경 기본 세팅
기능 3 : 둘 수 있는 경우의 수 출력
기능 4 : 뒤집어 지는 기능
기능 5 : 개수 카운트 기능
경우의 수 로직
1. -1일때 주위 3x3을 탐색
2. 탐색시 0이 있는지 확인
3. 있으면 그걸 기준으로 그 방향을 +1 해서 재귀 탐색
4. -1이면 그냥 종료, 1이 있으면 시작점을 true, 0이면 계속해서 탐색
'''

class Reversy():
    def __init__(self):
        self.map = [
            [-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,0,1,-1,-1,-1],
            [-1,-1,-1,1,0,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1]
        ]
        
        self.log = []
        self.turn = 0
        self.mark = ['O','X']
        self.able = None
        self.checker = False
        self.end = True
        self.score = [0,0]

    def print_field(self):
        print("x\\y  0   1   2   3   4   5   6   7")
        print("   ---------------------------------")
        for i in range(8):
            print(f"{i}  ", end="")
            for j in range(8):
                if self.map[i][j] == 1:
                    print(f"| {self.mark[0]} ", end="")
                elif self.map[i][j] == -1:
                    if [i,j] in self.able:
                        print(f"| {'*'} ", end="")
                    else:
                        print(f"| {' '} ", end="")
                else:
                    print(f"| {self.mark[1]} ", end="")
                    
            print("|")
            print("   ---------------------------------")

    def able_list(self):
        self.able = []
        for i in range(8):
            for j in range(8):
                if self.map[i][j] == -1:
                    if self.find_next(i+1,j,6,False) + self.find_next(i-1,j,4,False) + self.find_next(i,j-1,2,False) + self.find_next(i,j+1,8,False) + self.find_next(i+1,j-1,3,False) + self.find_next(i-1,j+1,7,False) + self.find_next(i-1,j-1,1,False) + self.find_next(i+1,j+1,9,False):
                        self.able.append([i,j])
                    
        if len(self.able) == 0:
            self.end_checker()
        else:
            self.checker = False

    def end_checker(self):
            if self.checker:
                self.end = False
            else:
                self.checker = True
                self.turn += 1
                self.able_list()

    def find_next(self,x,y,seed,bool):
        if x == -1 or y == -1 or x == 8 or y == 8 or self.map[x][y] == -1:
            return 0
        if self.map[x][y] == (self.turn % 2):
            if seed == 1:
                return self.find_next(x-1,y-1,seed,True)
            if seed == 2:
                return self.find_next(x,y-1,seed,True)
            if seed == 3:
                return self.find_next(x+1,y-1,seed,True)
            if seed == 4:
                return self.find_next(x-1,y,seed,True)
            if seed == 6:
                return self.find_next(x+1,y,seed,True)
            if seed == 7:
                return self.find_next(x-1,y+1,seed,True)
            if seed == 8:
                return self.find_next(x,y+1,seed,True)
            if seed == 9:
                return self.find_next(x+1,y+1,seed,True)
        else:
            return bool
        
    def put_mark(self,x,y):
        finder = False
        if [x,y] in self.able:  
            finder = True
        if finder:
            self.turn += 1
            self.map[x][y] = (self.turn % 2)
            
            self.log.append([x,y])
            
            self.reverse(x-1,y-1,1,0)
            self.reverse(x,y-1,2,0)
            self.reverse(x+1,y-1,3,0)
            self.reverse(x-1,y,4,0)
            self.reverse(x+1,y,6,0)
            self.reverse(x-1,y+1,7,0)
            self.reverse(x,y+1,8,0)
            self.reverse(x+1,y+1,9,0)
            
    def reverse(self,x,y,seed,cnt):
        if x == -1 or y == -1 or x == 8 or y == 8 or self.map[x][y] == -1:
            return
        if self.map[x][y] != (self.turn % 2):
            if seed == 1:
                self.reverse(x-1,y-1,seed,cnt+1)
            if seed == 2:
                self.reverse(x,y-1,seed,cnt+1)
            if seed == 3:
                self.reverse(x+1,y-1,seed,cnt+1)
            if seed == 4:
                self.reverse(x-1,y,seed,cnt+1)
            if seed == 6:
                self.reverse(x+1,y,seed,cnt+1)
            if seed == 7:
                self.reverse(x-1,y+1,seed,cnt+1)
            if seed == 8:
                self.reverse(x,y+1,seed,cnt+1)
            if seed == 9:
                self.reverse(x+1,y+1,seed,cnt+1)
        else:
            if cnt:
                if seed == 1:
                    for i in range(1,cnt+1):
                        self.map[x+i][y+i] = (self.turn % 2)
                if seed == 2:
                    for i in range(1,cnt+1):
                        self.map[x][y+i] = (self.turn % 2)
                if seed == 3:
                    for i in range(1,cnt+1):
                        self.map[x-i][y+i] = (self.turn % 2)
                if seed == 4:
                    for i in range(1,cnt+1):
                        self.map[x+i][y] = (self.turn % 2)
                if seed == 6:
                    for i in range(1,cnt+1):
                        self.map[x-i][y] = (self.turn % 2)
                if seed == 7:
                    for i in range(1,cnt+1):
                        self.map[x+i][y-i] = (self.turn % 2)
                if seed == 8:
                    for i in range(1,cnt+1):
                        self.map[x][y-i] = (self.turn % 2)
                if seed == 9:
                    for i in range(1,cnt+1):
                        self.map[x-i][y-i] = (self.turn % 2)
            
    def count_score(self):
        self.score = [0,0]
        
        for i in range(8):
            for j in range(8):
                if self.map[i][j] < 0:
                    continue
                self.score[self.map[i][j]] += 1
                
        print("  X     O")
        print("%3d : %3d" % (self.score[0], self.score[1]))
    
    def print_log(self):
        for i,j in self.log:
            print(f"[{i},{j}] ",end="")
            
    def print_result(self):
        self.count_score()
        print('\n===============')
        print(f'O : {self.score[1]}')
        print(f'X : {self.score[0]}')
        if self.score[0] > self.score[1]:
            print('winner : X')
        else:
            print('Winner : O')
            
    def game_start(self):
        self.able_list()
        while self.end:
            self.print_field()
            self.count_score()
            x, y = map(int, input("x y: ").split())
            self.put_mark(x,y)
            self.able_list()
            
        self.print_result()