def solution(y_true, y_pred):
    
    # time:
    # space:
    
    
    n = len(y_true)
    
    squared_error = 0
    grad = [0.0] * n
    
    for i in range(n):
        cur_error = y_pred[i] - y_true[i]
        squared_error += cur_error * cur_error
        grad[i] = cur_error
        
    mse = squared_error / n
    factor = 2.0 / n
    for i in range(n):
        grad[i] *= factor
    
    return mse, grad