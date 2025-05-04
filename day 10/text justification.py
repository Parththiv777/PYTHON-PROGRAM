class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        lines = []
        curr_line = []
        curr_total = 0
        
        i = 0
        while i < len(words):
            if curr_total + len(words[i]) + len(curr_line) > maxWidth:
                lines.append((curr_line, maxWidth-curr_total))
                curr_line = []
                curr_total = 0

            curr_line.append(words[i])
            curr_total += len(words[i])
            i += 1

        if curr_line:
            lines.append((curr_line, maxWidth-curr_total))

        def calculate_space(n, k):
            if k == 0:
                return [n]

            base = n // k
            remain = n % k

            res = [base] * k
            for i in range(remain):
                res[i] += 1

            return res

        res = []
        curr_res = ''
        for ls in range(len(lines)):
            line, space = lines[ls]

            sp = calculate_space(space, len(line)-1)

            if ls == len(lines) - 1:
                for i in range(len(line)):
                    curr_res += line[i]

                    if i < len(line) - 1:
                        curr_res += " "
                        space -= 1
                    else:
                        curr_res += space * " "
            else:
                for i in range(len(line)):
                    curr_res += line[i]

                    if i < len(sp):
                        curr_res += " " * sp[i]

            res.append(curr_res)
            curr_res = ''

        return res

