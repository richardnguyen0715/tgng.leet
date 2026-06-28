class Solution:
    def maskPII(self, s: str) -> str:
        
        # EMAIL
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')
            
            return name[0] + "*****" + name[-1] + "@" + domain
        
        # PHONE
        digits = [c for c in s if c.isdigit()]
        
        local = "***-***-" + "".join(digits[-4:])
        
        if len(digits) == 10:
            return local
        
        country = "+" + "*" * (len(digits) - 10) + "-"
        
        return country + local