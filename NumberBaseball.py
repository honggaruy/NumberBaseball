import random

class CommonBasic:
    dicScoreTr =  {300:"3S0B", 120:"1S2B", 30:"0S3B",
                   200:"2S0B", 110:"1S1B", 20:"0S2B",
                   100:"1S0B",  10:"0S1B",  0:"OUT"}
    dicStBallTr = {"3S0B":300, "1S2B":120, "0S3B":30,
                   "2S0B":200, "1S1B":110, "0S2B":20,
                   "1S0B":100, "0S1B": 10,  "OUT": 0}
    # make number list in normal order
    lst1000 = [
        [i]*3 for i in range(1000)
        ]
    lst720 = [
        [i]*3 for i in range(720)
        ]

    def __init__(self):
        print("commonbasic init")
        for i in range(1000):
            self.lst1000[i][0] = divmod(i,100)[0] # 100's place
            self.lst1000[i][1] = divmod(divmod(i,10)[0],10)[1] #  10's place
            self.lst1000[i][2] = divmod(i,10)[1] #   1's place
        tup1000 = tuple(self.lst1000)

        j=0
        for i in range(1000):
            if self.lst1000[i][0] == self.lst1000[i][1]: pass
            elif self.lst1000[i][0] == self.lst1000[i][2]: pass
            elif self.lst1000[i][1] == self.lst1000[i][2]: pass
            else:
                self.lst720[j] = self.lst1000[i]
                j += 1

    # decide Strike or ball
    # example input : list1 [ 0, 1, 2 ] , list2 [ 1, 2, 3]
    # example output : tuple ( 20, 0S2B )
    def CalculateDecision(self, list1, list2):
        Score = 0
        StBall = self.dicScoreTr[Score]
        for i in range(3):
            for j in range(3):
                if list1[i] == list2[j]:
                    if i == j: Score += 100
                    else: Score += 10
        StBall = self.dicScoreTr[Score]
        return Score,StBall


class Referee(CommonBasic):
    def __init__(self):
        super().__init__()
        pass
    def CreateTarget(self):
        pass
    def CheckInput(self):
        pass

class Pitcher(CommonBasic):
    #  list of each Score Case

    def __init__(self):
        super().__init__()
        print("pitcher init")
        self.lstScore_300    = [ ]
        self.lstScore_120    = [ ]
        self.lstScore_30     = [ ]
        self.lstScore_200    = [ ]
        self.lstScore_110    = [ ]
        self.lstScore_20     = [ ]
        self.lstScore_100    = [ ]
        self.lstScore_10     = [ ]
        self.lstScore_0      = [ ]

    '''
        Count the case
        input : lst ( list of group to test ) , ask1 ( trial input )
    '''
    def CountCase (self, lst, lstnum, ask1, makeScore = False ):
        dicCountCase = {300:0, 120:0, 30:0,
                        200:0, 110:0, 20:0,
                        100:0,  10:0,  0:0}

        # initialize the global list
        if makeScore:
            del self.lstScore_0[:]
            del self.lstScore_10[:]
            del self.lstScore_100[:]
            del self.lstScore_20[:]
            del self.lstScore_110[:]
            del self.lstScore_200[:]
            del self.lstScore_30[:]
            del self.lstScore_120[:]
            del self.lstScore_300[:]

        for i in range(lstnum):
            dicCountCase[self.CalculateDecision(lst[i],ask1)[0]] += 1
            if makeScore:
                if   self.CalculateDecision(lst[i], ask1)[0] ==   0: self.lstScore_0.append(lst[i])
                elif self.CalculateDecision(lst[i], ask1)[0] ==  10: self.lstScore_10.append(lst[i])
                elif self.CalculateDecision(lst[i], ask1)[0] == 100: self.lstScore_100.append(lst[i])
                elif self.CalculateDecision(lst[i], ask1)[0] ==  20: self.lstScore_20.append(lst[i])
                elif self.CalculateDecision(lst[i], ask1)[0] == 110: self.lstScore_110.append(lst[i])
                elif self.CalculateDecision(lst[i], ask1)[0] == 200: self.lstScore_200.append(lst[i])
                elif self.CalculateDecision(lst[i], ask1)[0] ==  30: self.lstScore_30.append(lst[i])
                elif self.CalculateDecision(lst[i], ask1)[0] == 120: self.lstScore_120.append(lst[i])
                elif self.CalculateDecision(lst[i], ask1)[0] == 300: self.lstScore_300.append(lst[i])
        return dicCountCase

    def SetTrial(self,trialnumber):
        if trialnumber == 1:
            self.trial = self.lst720[random.randrange(0,720)]
            self.CountCase(self.lst720,720,self.trial,True)
            print("trial :",self.trial)

    def Copylist(self,srclst,tgtlst):
        for i in range(len(srclst)):
            tgtlst.append(srclst[i])

    def FindNextTrial(self,result):
        lstResult = []
        # select list
        if   result == 300: self.Copylist(self.lstScore_300,lstResult)
        elif result == 120: self.Copylist(self.lstScore_120,lstResult)
        elif result ==  30: self.Copylist(self.lstScore_30 ,lstResult)
        elif result == 200: self.Copylist(self.lstScore_200,lstResult)
        elif result == 110: self.Copylist(self.lstScore_110,lstResult)
        elif result ==  20: self.Copylist(self.lstScore_20 ,lstResult)
        elif result == 100: self.Copylist(self.lstScore_100,lstResult)
        elif result ==  10: self.Copylist(self.lstScore_10 ,lstResult)
        elif result ==   0: self.Copylist(self.lstScore_0  ,lstResult)

        print("lstResult",len(lstResult),len(self.lstScore_200))

        maxCol = []
        zeroCntCol = []
        lstTest = []
        for i in range(len(self.lst720)):
            dic = self.CountCase(lstResult,len(lstResult),self.lst720[i])
            val = list(dic.values())
            lstTest.append([self.lst720[i],dic,max(val),val.count(0)])
            maxCol.append(max(val))
            zeroCntCol.append(val.count(0))
        print(min(maxCol),maxCol.index(min(maxCol)))
        print(min(zeroCntCol),zeroCntCol.index(min(zeroCntCol)))

        lstNext = []
        for i in range(len(self.lst720)):
            if lstTest[i][2] == min(maxCol):
                lstNext.append([self.lst720[i],lstTest[i][1]])
        print(len(lstNext))
        for i in range(10):
            print(i, lstNext[i])
        self.trial = lstNext[random.randrange(0,len(lstNext))]
        print(self.trial)

class GameManager:
    def __init__(self):
        pass
    def SetGameMode(self, mode):
        pass
    def CheckInput(self):
        pass
    def DisplayResult(self):
        pass


pitcher01 = Pitcher()
referee01 = Referee()
print(type(pitcher01))
print(type(referee01))
manager01 = GameManager()

pitcher01.SetTrial(1)
pitcher01.FindNextTrial(200)
