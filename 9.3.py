# -*- coding: utf-8 -*-
"""

11 19
#######A###########
#.......#.#...#...#
#.###.###...#.#.#.#
#...#.....#.#...#.#
#.#.###.#.#.#.###.#
#.#.....#...#.#...#
#.###########.#.#.#
#.#.#.....#...#.#.#
#.#.#####.#####.#.#
#.........#.....#.#
###############B###


from time import sleep

txt = open("maze.txt").read()  

n, m = 11,19

mazeini = [ txt[i*(m+1):(i+1)*(m+1)-1] for i in range(n)]



def explore(i, j,maze=mazeini):
    global solution, visited
    
    if (0 <= i < n and 0 <= j < m and
        maze[i][j] != "#" and not visited[i][j]):
        
        visited[i][j] = True
        
        
        
        
        
        if maze[i][j] == 'B':
            solution = True
            print('\n'.join(maze))
        
        maze[i]=list(maze[i])
        
        maze[i][j]='x'
        
        maze[i]="".join(list(maze[i]))
        
        #sleep(0.1)
        #print('\n'.join(maze))
        
        if not solution:
            explore(i - 1, j,maze)
            explore(i + 1, j,maze)
            explore(i, j - 1,maze)
            explore(i, j + 1,maze)


def find(symbol):
    for i in range(n):
        j = mazeini[i].find(symbol)
        if j >= 0:
            return (i, j)
        


solution = False
visited = [m*[False] for i in range(n)]

explore(*find('A'))

if solution:
    print("path from A to B exists")
    #print('\n'.join(mazefinal))
else:
    print("no path")

"""
from time import sleep
from copy import copy

txt = open("maze.txt").read()  

n, m = 11,19

mazeini = [ txt[i*(m+1):(i+1)*(m+1)-1] for i in range(n)]



def explore(i, j,maze):
    global solution, visited
    
    if (0 <= i < n and 0 <= j < m and
        maze[i][j] != "#" and not visited[i][j]):
        
        visited[i][j] = True
        
        
        mazelist=list(maze[i])
        mazelist[j]='x'
        newmaze=copy(maze)        
        newmaze[i]="".join(list(mazelist))
        
        
        sleep(0.1)
        print('\n'.join(newmaze))
        
        
        if maze[i][j] == 'B':
            solution = maze

        
        
        if not solution:
            explore(i - 1, j,newmaze)
            explore(i + 1, j,newmaze)
            explore(i, j - 1,newmaze)
            explore(i, j + 1,newmaze)


def find(symbol):
    for i in range(n):
        j = mazeini[i].find(symbol)
        if j >= 0:
            return (i, j)
        


solution = False
visited = [m*[False] for i in range(n)]

explore(*find('A'),mazeini)

if solution:
    print('')
    print("path from A to B exists")
    print('\n'.join(solution))
else:
    print("no path")




