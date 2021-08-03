import time

infinity = float('inf')

def return_value(ele):
    return ele.value
    
def AlphaBetaAlg(start_time,node,depth=infinity, alpha=-infinity, beta=infinity, isMaximizing=True,threshold=30):
    if depth == 0 or node.isterminal(isMaximizing):  # base condition
        return node.value, node.pos

    best_pos = None

    if isMaximizing:  # maxmizer player
        value = -infinity
        Choices = sorted(node.get_children(), key=return_value, reverse=True)
        for i in Choices:
            other = AlphaBetaAlg(start_time,i, depth - 1, alpha, beta, isMaximizing=i.is_repeated)
            if value < other[0]:
                value = other[0]
                best_pos = i.pos
            if value > alpha:
                alpha = value
            if alpha >= beta:  # cutoff
                break
            if time.time()-start_time>threshold+10:
                return value,best_pos
        return value, best_pos


    else:  # minimizer player
        value = infinity
        Choices = sorted(node.get_opponent_children(), key=return_value)
        for i in Choices:
            other = AlphaBetaAlg(start_time,i, depth - 1, alpha, beta, isMaximizing=not i.is_repeated)
            if value > other[0]:
                value = other[0]
                best_pos = i.pos
            if value < beta:
                beta = value
            if alpha >= beta:  # cutoff
                break
            
            if time.time()-start_time>threshold+10:
                return value,best_pos            
        return value, best_pos
