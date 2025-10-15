class RecentCounter(object):
    def __init__(self):
        self.calling_list = []

    def ping(self, t):
        self.calling_list.append(t)
        start = t - 3000
        while self.calling_list[0] < start:
            self.calling_list.pop(0)

        return len(self.calling_list)
    
class RecentCounter(object):
    def __init__(self):
        self.calling_list = []
        self.MAX_TIME_SPAN = 3000

    def ping(self, t):
        self.calling_list.append(t)
        start = t - self.MAX_TIME_SPAN
        while self.calling_list[0] < start:
            self.calling_list.pop(0)

        return len(self.calling_list)
    
class RecentCounter(object):
    def __init__(self):
			  """
				  Time: O(a) : a là số phần tử bị loại bỏ
				  Space: O(1) -> tuy nhiên thì tùy thuộc vào số lượng ping
			  """
        self.queue = collections.deque()
        self.MAX_TIME_SPAN = 3000

    def ping(self, t):
        self.calling_list.append(t)
        start = t - self.MAX_TIME_SPAN
        while self.queue and self.queue[0] < start:
	        self.queue.popleft()
        return len(self.queue)