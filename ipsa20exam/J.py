'''
    SOCCER TOURNAMENT

    In this problem we consider a soccer tournament among n teams.
    The teams play m games. For each game among two teams A and B, we
    know the number of goals a and b scored by A and B, respectively.
    If the game ends in a draw, i.e. a == b, then both teams receive
    one point. Otherwise, the winning team receives 3 points and the
    loosing team 0 points.

    Input:

        The first line contains two integers n and m, separated by
        space, being the number of teams n and the number of mathes
        played m. Then follows n lines, each with a unique team name
        being a non-empty string only containing characters A-Z and
        _. Each team name has length at most 25. Then follows m lines,
        one for each match, of the form A B a b, where A and B are
        valid distinct team names and a and b are the number of goals
        scored by A and B respectively.

        2 <= n <= 20
        0 <= m <= n * (n - 1)

    Output:

        The output consists of n lines, the final ranking after all m
        games. Each line should contain a team name followed by the
        team's final points, separated by a space. The teams should be
        sorted in decreasing point order. If several teams have the
        same number of points, the teams should appear sorted
        alphabetically. All points and team names are separated by a
        space:

             Team1 point1 Team2 point2 ...

    Example:

      Input:  3 6
              A
              B
              C
              A B 3 1
              A C 1 2
              B C 2 0
              B A 1 0
              C A 2 1
              C B 5 1

      Output: C 9
              B 6
              A 3
'''

n, m = map(int, input().split())

teamnames=[]
points=[0]*m
for i in range(n):
    teamnames.append(input())
    
teams=dict((team,0) for team in teamnames)


for match in range(m):
    A, B, a, b = input().split()
    
    if a==b:
        teams[A]+=1
        teams[B]+=1
        continue
    
    if a<=b:
        teams[B]+=3
        continue
    
    teams[A]+=3

sort=sorted(teams, key=lambda x: teams[x],reverse=True)

for i in range(n):
    print(sort[i]+' '+str(teams[sort[i]]))