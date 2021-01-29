import random


class BreakoutTeams:

    def __init__(self, overall_members, demanded_team_size):
        self.demanded_team_size = demanded_team_size
        self.overall_members = overall_members
        self.breakout_teams = []
        self.current_team = []

    def randomize_members(self):
        i = 0
        randomly_ordered_members = []
        while i < len(self.overall_members):
            n = random.randint(0, len(self.overall_members) - 1)
            member = self.overall_members[n]
            self.overall_members.remove(member)
            randomly_ordered_members.append(member)
        self.overall_members = randomly_ordered_members

    def add_member_to_current_team(self, member):
        self.current_team.append(member)

    def any_team_contains(self, candidate):
        if candidate in self.current_team:
            return True
        for team in self.breakout_teams:
            if candidate in team:
                return True
        return False

    def get_number_of_teams(self):
        return len(self.breakout_teams)

    def get_current_team(self):
        return self.current_team

    def get_teams(self):
        return self.breakout_teams

    def close_current_team(self):
        self.breakout_teams.append(self.current_team)
        self.current_team = []

    def all_members_are_assigned(self):
        if len(self.get_unassigned_members()) == 0:
            return True
        else:
            return False

    def get_unassigned_members(self):
        unassigned_members = []
        for candidate in self.overall_members:
            if not self.any_team_contains(candidate):
                unassigned_members.append(candidate)
        return unassigned_members

    def current_team_is_complete(self):
        if len(self.current_team) == int(self.demanded_team_size):
            return True
        else:
            return False
