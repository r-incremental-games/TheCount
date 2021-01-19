class Stats(object):

    def __init__(self):
        self.dict = {}

    def increment_user(self, name):
        """Increment a users stats or create a new entry if they didn't exist yet"""
        if name in self.dict:
            self.dict[name] += 1
        else:
            self.dict[name] = 1

    def get_user_count_count(self, name):
        """:returns the amount of numbers this name has counted"""
        return self.dict[name] if name in self.dict else 0

    def get_high_scores(self, limit=10):
        """:returns a sorted (DESC) list of the users who """
        counts = [(k, v) for k, v in self.dict.items()]
        sorted_by_count = sorted(counts, key=lambda tup: tup[1], reverse=True)
        return sorted_by_count[:limit]
