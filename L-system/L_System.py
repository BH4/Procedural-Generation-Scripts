from random import seed, uniform


class L_System():
    def __init__(self, start, rules):
        # Start is a combination of variables and constants in a single string
        self.start = start
        # Rules should be a dictionary with variable keys and values that are
        # combinations of variables and constants
        self.rules = rules

        # Variables and constants are single characters
        self.variables, self.constants = self.get_alphabet()

        self.reset()

    def get_alphabet(self):
        v_list = []
        c_list = []

        # Consistency checks to make sure there were no obvious typos.
        for x in self.rules.keys():
            if self.rules[x] != x:
                v_list.append(x)
            else:
                c_list.append(x)

        for v in self.rules.values():
            for x in v:
                if x not in v_list and x not in c_list:
                    c_list.append(x)

        return v_list, c_list

    def reset(self):
        self.curr = self.start
        self.gen = 0

    def advance(self):
        new = ''

        for c in self.curr:
            if c in self.rules:
                new += self.rules[c]
            else:
                new += c

        self.curr = new

    def advance_n(self, n):
        for i in range(n):
            self.advance()

    def get_step(self, n):
        self.reset()
        self.advance_n(n)
        return self.curr
