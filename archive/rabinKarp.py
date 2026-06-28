def rabinKarp(t: str = "", p: str = ""):
    # T vs P
    # T: AAABBABAAA (m)
    # P: AAABB (n)
    
    m = len(t)
    n = len(p)
    
    if m < n:
        return []
    
    result = []
    power = 1
    tHash = 0
    pHash = 0
    k = 2
    
    # N kí tự đầu của P
    for i in range(n):
        power = 0 if i == 0 else power * k
        tHash = k * tHash + ord(t[i])
        pHash = k * pHash + ord(p[i])
        
    # N kí tự sau kể từ P
    for i in range(n, m):
        if pHash == tHash and t[i - n:i + 1] == p:
            result.append(i - n)
        
        # Dịch chuyển lên một kí tự
        tHash = tHash - ord(t[i-n]) * power
        tHash = k * tHash + ord(t[i])
    
    
    # So sánh substring cuối cùng
    if tHash == pHash and t[m - n: m] == p:
        result.append(m - n)
    
    return result




def rabinKarp(t: str, p: str):
    
    m = len(t)
    n = len(p)
    
    # P khong phai substring cua T
    if n > m:
        return []
    
    power = 1
    tHash = 0
    pHash = 0
    k = 2
    results = []
    q = 1000000007
    
    # Tinh cho N ki tu dau tien
    for i in range(n):
        power = 1 if i == 0 else (power * k) % q
        tHash = (k * tHash + ord(t[i])) % q
        pHash = (k * pHash + ord(p[i])) % q
        
    
    # Xet M - N ki tu tiep theo
    for i in range(n, m):
        if tHash == pHash and t[i - n: i + 1] == p:
            results.append(i)
        
        tHash -= (ord(t[i - n]) * power) % q
        if tHash < 0:
            tHash += q
        tHash = (tHash * k + ord(t[i])) % q
        
    if tHash == pHash and t[m-n:m] == p:
        results.append(m - n)
    
    return results
    
    