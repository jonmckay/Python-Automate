import pprint

# Create a list of dictionaries (data structure)

cat = {'name' : 'zophie', 'age' : 7, 'color' : 'gray'}
allCats = []
allCats.append({'name' : 'zophie', 'age' : 7, 'color' : 'gray'})
allCats.append({'name' : 'Pooka', 'age' : 5, 'color' : 'black'})
allCats.append({'name' : 'Fat-tail', 'age' : 5, 'color' : 'gray'})
allCats.append({'name' : '???', 'age' : -1, 'color' : 'orange'})

print(allCats)

# Store a tic-tac-toe board with strings representing the spaces in a dictionary
theBoard = {'top-L' : 'O', 'top-M' : 'O', 'top-R' : 'O', 'mid-L' : 'X', 'mid-M' : 'X', 'mid-R' : ' ', 'low-L' : ' ', 'low-M' : ' ', 'low-R' : 'X'}

#pprint.pprint(theBoard)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


printBoard(theBoard)
