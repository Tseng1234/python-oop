class GuessingGame:
    def __init__(self,answer):
        self.answer=int(answer)
    def guess(self,num):
        self.num=int(num)
        if self.num==self.answer:
            print("你猜對了")
        elif self.num>self.answer:
            print("你猜太大了")
        else:
            print("你猜太小了")
    def play(self):
        print("請猜個數字")
        guess_answer=input()
        self.guess(guess_answer)
game = GuessingGame(42)  # 創建遊戲實例，設定答案為 42
game.play()  # 開始遊戲
