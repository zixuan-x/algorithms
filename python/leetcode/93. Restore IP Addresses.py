# https://leetcode.com/problems/restore-ip-addresses/discuss/31140/Python-easy-to-understand-solution-with-comments-(backtracking).

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s or len(s) > 12:
            return []
        IPs = []
        self.search(s, 0, 0, '', IPs)
        return IPs
    
    def search(self, s, index, dots, ip, IPs):
        if index == len(s):
            if dots == 3 and self.isValidIp(ip):
                IPs.append(ip)
            return
        
        self.search(s, index + 1, dots, ip + s[index], IPs)
        
        self.search(s, index + 1, dots + 1, ip + s[index] + '.', IPs)

    def isValidIp(self, ip):
        nums = ip.split('.')
        for num in nums:
            if not num:
                return False
            if len(num) > 1 and num[0] == '0':
                return False
            if int(num) < 0 or int(num) > 255:
                return False
        return True
        