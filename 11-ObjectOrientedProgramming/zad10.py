class c:
    def __init__(self, points):
        self.points = points
    def m(self, n):
        count = sum(1 for x, y in self.points if x>0 and y>0)
        return count>=n
def main():
    punkty = c([[2,3],[1,8],[-6,4],[3,-7]])
    print(punkty.m(3))
    print(punkty.m(2))
if __name__ == '__main__':
    main()