class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width = len(board[0])
        height = len(board) 
        # up = height + 1
        #down = height -1
        #left = width -1
        #right = width + 1
       
        def dfs():
            for index_height in range(height):
                for index_width in range(width):
                    current = ""
                    current += board[index_height][index_width]
                    visited = []
                 
                    if(search_word(index_width, index_height, current, visited.copy())):
                        return True
            return False
        def search_word(width_pos, height_pos, current, visited):
            if (height_pos,width_pos) not in visited:
                visited.append((height_pos, width_pos))
            else:
                return False
            if current == word:
                return True
            size_of_current = len(current)
            if(current != word[:size_of_current]):
                return False


            board_of_records = [(height_pos + 1, width_pos), (height_pos-1, width_pos), (height_pos, width_pos -1), (height_pos, width_pos + 1)]
            for x in range(len(board_of_records)):
                if(board_of_records[x][0] >= height or board_of_records[x][0] < 0 or board_of_records[x][1] >= width or board_of_records[x][1] < 0 ):
                    continue
             
                if(search_word(width_pos = board_of_records[x][1], height_pos= board_of_records[x][0] ,current=  current + board[board_of_records[x][0]][board_of_records[x][1]], visited = visited.copy() )):
                    return True
            return False

        return dfs()


