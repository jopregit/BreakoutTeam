class Visavis:

    def __init__(self, team):
        self.team = team
        self.visavis_matrix = {}
        self.initialize_visavis_matrix()

    def initialize_visavis_matrix(self):
        for member_1 in self.team:
            for member_2 in self.team:
                if member_1 < member_2:
                    self.visavis_matrix[self.join_to_key(member_1, member_2)] = 0

    @staticmethod
    def join_to_key(member_1, member_2):
        if member_1 < member_2:
            return member_1 + "---" + member_2
        else:
            return member_2 + "---" + member_1

    def get_minimum_of_current_visits(self):
        # nasty! find proper initial value
        current_minimum_value = 1000
        for key in self.visavis_matrix:
            value = self.visavis_matrix[key]
            if value < current_minimum_value:
                current_minimum_value = value
        return current_minimum_value

    def get_visits(self, member_1, member_2):
        return self.visavis_matrix[self.join_to_key(member_1, member_2)]

    def increase_visits(self, new_member, breakout_team):
        for member in breakout_team:
            self.visavis_matrix[self.join_to_key(new_member, member)] += 1

    # ideal heisst: kein Paar hat sich mehr als einmal oefters gesehen als die anderen Paare
    def is_ideal(self):
        minimal_visits = self.get_minimum_of_current_visits()
        for key in self.visavis_matrix:
            if self.visavis_matrix[key] > (minimal_visits + 1):
                return False
        return True
