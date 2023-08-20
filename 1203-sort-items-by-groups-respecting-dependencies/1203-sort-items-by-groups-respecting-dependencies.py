class Solution:
    def __init__(self):
        self.ret = []
        self.group = []
        self.beforeItems = []
        self.cnt = 0
        self.groups = []
        self.checked = []
        self.preparing = []
        self.cycle = False

    def sortItems(self, n, m, group, beforeItems):
        # Initialize variables
        self.groups = [[] for _ in range(m)]
        self.ret = [0] * n
        self.checked = [False] * n
        self.preparing = [False] * n
        self.group = group
        self.beforeItems = beforeItems

        # Group items by their group[i]
        for i in range(n):
            if group[i] != -1:
                self.groups[group[i]].append(i)

        # Iterate and prepare all items
        for i in range(n):
            if not self.checked[i]:
                self.prepare(i, True)

        return [] if self.cycle else self.ret

    def prepare(self, i, pass_on):
        if self.preparing[i] or self.cycle:
            self.cycle = True
            return

        self.preparing[i] = True

        if self.group[i] == -1:
            for item in self.beforeItems[i]:
                if not self.checked[item]:
                    self.prepare(item, True)
            self.checked[i] = True
            self.ret[self.cnt] = i
            self.cnt += 1
        else:
            for item in self.groups[self.group[i]]:
                if item == i:
                    continue
                for beforeItem in self.beforeItems[item]:
                    if self.group[beforeItem] != self.group[item] and not self.checked[beforeItem]:
                        self.prepare(beforeItem, True)

            for item in self.beforeItems[i]:
                if not self.checked[item]:
                    self.prepare(item, self.group[item] != self.group[i])
            self.checked[i] = True
            self.ret[self.cnt] = i
            self.cnt += 1

            if pass_on:
                for item in self.groups[self.group[i]]:
                    if not self.preparing[item]:
                        self.prepare(item, False)
