class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        if ':' in queryIP and '.' not in queryIP:
            ipList = queryIP.split(":")
            print(ipList)

            if len(ipList) != 8:
                return "Neither"

            for ipID in ipList:
                if len(ipID) < 1 or len(ipID) > 4:
                    return "Neither"
                
                try:
                    decimalID = int(ipID, 16)
                except:
                    return "Neither"

            return "IPv6"

        elif '.' in queryIP and ':' not in queryIP:
            ipList = queryIP.split('.')
            print(ipList)

            if len(ipList) != 4:
                return "Neither"

            for ipID in ipList:

                print(ipID)

                if ipID == '' or (ipID[0] == '0' and len(ipID) >= 2):
                    return "Neither"
                
                try:
                    intID = int(ipID)
                except:
                    return "Neither"

                if 0 > intID or intID > 255:
                    return "Neither"

            return "IPv4"

        else:
            return "Neither"