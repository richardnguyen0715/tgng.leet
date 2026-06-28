from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        n = len(emails)
        uniqueEmails = set()
        for email in emails:
            cleanedEmail = []
            catchPlusSign = False
            for idx, c in enumerate(email):

                if c == '@':
                    cleanedEmail.append(email[idx:])
                    break

                if c == '.' or catchPlusSign:
                    continue

                if c == '+':
                    catchPlusSign = True
                    continue
                
                cleanedEmail.append(c)
            
            uniqueEmails.add("".join(cleanedEmail))
        
        print(uniqueEmails)
        return len(uniqueEmails)
                

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            local, domain = email.split('@')

            if '+' in local:
                local = local[:local.index('+')]
            
            local = local.replace('.', '')

            normalized = local + '@' + domain
            uniqueEmails.add(normalized)

        return len(uniqueEmails)