def f(y):
	"""
	Time: O(log(n))
	"""
	ans = 0
	while y > 0:
		temp = y % 10
		ans += temp ** 2
		y /= 10
	return ans
		
def happyNumber(x: int):
    """
    x -> f(x) -> ff(x) -> fff(x) -> ...
    Time: O((a + b)*log(n)) -> a + b là thời gian để gặp nhau, log(n) thời gian tính tổng

    => Nếu tồn tại một vòng lặp mà gặp nhau ở điểm 1 -> True, ngược lại nếu gặp nhau nhưng không ở điểm một thì là False
    """
    if x == 1:
        return True
    used = set()
    while True:
        if x == 1:
            return True
        if x in used:
            return False
        used.add(x)
        x = f(x)
	
		
	