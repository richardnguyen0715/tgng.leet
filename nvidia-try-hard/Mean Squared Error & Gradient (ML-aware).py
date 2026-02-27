def solution(y_true, y_pred):
    
    # Time: O(N + N) = O(N)
    # Space: O(1)
    
    # Note:
    # Brute Force? -> one loop? O(N)? -> Maybe ( < 10^3)
    
    # Test: no need
    
    n = len(y_true)
    mse = 0.0
    grad = 0.0
    
    for i in range(n): # O(N)
        diff = y_pred[i] - y_true[i]
        mse += diff * diff
        grad[i] = diff
    
    mse /= n
    factor = 2.0 / n
    for i in range(n): # O(N)
        grad[i] *= factor
    
    return mse, grad