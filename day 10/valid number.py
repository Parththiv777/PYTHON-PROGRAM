class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        invalids = {
            'inf', '+inf', '-inf',
            'infinity', '+infinity', '-infinity',
            'Infinity', '+Infinity', '-Infinity',
            'INF', '+INF', '-INF',
            'INFINITY', '+INFINITY', '-INFINITY',
            'nan', 'Nan', 'NAN'
        }

        try:
            if s in invalids:
                return False
            float(s)
            return True
        except ValueError:
            return False
