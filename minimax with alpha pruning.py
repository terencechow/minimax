def next_move(player,board)
    def minimax(level, playerValue,cells,alpha,beta)  
        if playerValue == "X"
            opponent = "O"
        else
            opponent = "X"
        end
    
        if gameover(cells) || level ==0
           return generateScore(cells)
        end
    
        children = ["0 0","0 1", "0 2","1 0", "1 1", "1 2","2 0","2 1","2 2"]
        bestMove =""
        for i in 0..2
            for j in 0..2
                if cells[i][j] == playerValue || cells[i][j] == opponent
                    position = i.to_s + ' ' + j.to_s
                    children.delete(position)
                end
            end
        end
    
        if playerValue =="X"
            children.each {|a|
                newcells = [cells[0].dup,cells[1].dup,cells[2].dup]
                newcells[a[0].to_i][a[-1].to_i] = 'X'
                score = minimax(level - 1, opponent, newcells,alpha,beta)[0]
                if score > alpha
                    alpha = score
                    bestMove = a
                end	
                if alpha >= beta
                    break
                end
                }
             return [alpha,bestMove]
        else
            children.each {|a|
                newcells = [cells[0].dup,cells[1].dup,cells[2].dup]
                newcells[a[0].to_i][a[-1].to_i] = 'O'
                score = minimax(level - 1, opponent,newcells,alpha,beta)[0]
                if score < beta
                    beta = score
                    bestMove = a
                end
                if alpha >= beta
                    break
                end
                }
            return [beta,bestMove]
        end
    end
    
    def gameover(cells)
        for i in 0..2
            #one of the rows has a win
            if cells[i].count('X') ==3 || cells[i].count('O') ==3
                return true
            # a column has a win
            elsif cells[0][i].include?('X') && cells[1][i].include?('X') && cells[2][i].include?('X') || cells[0][i].include?('O') && cells[1][i].include?('O') && cells[2][i].include?('O') 
                return true
            end
        end
        # diagonal has a win
        if cells[0][0].include?('X') && cells[1][1].include?('X') && cells[2][2].include?('X') || cells[0][2].include?('X') && cells[1][1].include?('X') && cells[2][0].include?('X') || cells[0][0].include?('O') && cells[1][1].include?('O') && cells[2][2].include?('O') || cells[0][2].include?('O') && cells[1][1].include?('O') && cells[2][0].include?('O') 
            return true
        end
        #no more moves
        if !(cells[0].include?('_') || cells[1].include?('_') || cells[2].include?('_') )
            return true
        end
        return false
    end
    
    def generateScore(cells)
        
        playerValue = 'X'
        opponent = 'O'
        
        score = 0
        for i in 0..2
            #calculate score of row
            if cells[i].count(playerValue) == 3
                score +=100
            elsif cells[i].count(playerValue) ==2 && cells[i].include?('_')
                score+=10
            elsif cells[i].count('_') ==2 && cells[i].include?(playerValue)
                score+=1
            elsif cells[i].count(opponent) ==3
                score -=100
            elsif cells[i].count(opponent) ==2 && cells[i].include?('_')
                score-=10
            elsif cells[i].count('_') ==2 && cells[i].include?(opponent)
                score-=1
            else
                score+=0
            end
        
            #calculate score of column
            
            column = [cells[0][i],cells[1][i],cells[2][i]]
            if column.count(playerValue) ==3
                score +=100
            elsif column.count(playerValue) ==2 && column.include?('_')
                score+=10
            elsif column.count('_') ==2 && column.include?(playerValue)
                score+=1
            elsif column.count(opponent) ==3
                score -=100
            elsif column.count(opponent) ==2 && column.include?('_')
                score-=10
            elsif column.count('_') ==2 && column.include?(opponent)
                score-=1
            else
                score+=0
            end
    
        end
        
        diagonalone = [cells[0][0],cells[1][1],cells[2][2]]
        diagonaltwo = [cells[0][2],cells[1][1],cells[2][0]]
        
            if diagonalone.count(playerValue) ==3
                score +=100
            elsif diagonalone.count(playerValue) ==2 && diagonalone.include?('_')
                score+=10
            elsif diagonalone.count('_') ==2 && diagonalone.include?(playerValue)
                score+=1
            elsif diagonalone.count(opponent) ==3
                score -=100
            elsif diagonalone.count(opponent) ==2 && diagonalone.include?('_')
                score-=10
            elsif diagonalone.count('_') ==2 && diagonalone.include?(opponent)
                score-=1
            else
                score+=0
            end
    
            if diagonaltwo.count(playerValue) ==3
                score +=100
            elsif diagonaltwo.count(playerValue) ==2 && diagonaltwo.include?('_')
                score+=10
            elsif diagonaltwo.count('_') ==2 && diagonaltwo.include?(playerValue)
                score+=1
            elsif diagonaltwo.count(opponent) ==3
                score -=100
            elsif diagonaltwo.count(opponent) ==2 && diagonaltwo.include?('_')
                score-=10
            elsif diagonaltwo.count('_') ==2 && diagonaltwo.include?(opponent)
                score-=1
            else
                score+=0
            end
        return [score,""]
    end
  
    puts minimax(9,player,board,-10000,10000)[1]
end