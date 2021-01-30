from BreakoutTeams import BreakoutTeams
from Visavis import Visavis
import copy


class SmartTeam:

    def __init__(self, name, team):
        self.debug = True
        self.name = name
        self.members = self.clean_list(team)
        self.breakout_teams = None
        self.breakout_teams_trial = None
        self.visavis = Visavis(self.members)
        self.visavis_trial = Visavis
        self.breakout_teams_trial = None
        self.current_number_of_trials = 0
        self.max_trials = 10000
        self.html_result = "<h2>Your breakout teams:</h2>"

    # heuristic: hope that after enough trials (with randomized order in list of members) ideal groups are found
    def create_next_breakout_teams(self, demanded_team_size):
        self.breakout_teams = BreakoutTeams(self.members, demanded_team_size)
        self.current_number_of_trials = 0
        while self.current_number_of_trials < self.max_trials:
            self.current_number_of_trials += 1
            self.initiate_next_trial()
            self.try_next_breakout_teams(demanded_team_size)
            if self.visavis_trial.is_ideal():
                self.breakout_teams = self.breakout_teams_trial
                self.visavis = self.visavis_trial
                print("Ideal team found after " + self.current_number_of_trials.__str__() + " trials")
                return
        print("Unfortunately no ideal solution has been found after " + self.max_trials.__str__() + " trials")
        self.breakout_teams = self.breakout_teams_trial
        self.visavis = self.visavis_trial

    def initiate_next_trial(self):
        self.breakout_teams_trial = copy.deepcopy(self.breakout_teams)
        self.visavis_trial = copy.deepcopy(self.visavis)
        self.breakout_teams_trial.randomize_members()

    def try_next_breakout_teams(self, demanded_team_size):
        while not self.breakout_teams_trial.all_members_are_assigned():
            while not self.breakout_teams_trial.current_team_is_complete():
                new_member = self.find_best_partner()
                self.visavis_trial.increase_visits(new_member, self.breakout_teams_trial.get_current_team())
                self.breakout_teams_trial.add_member_to_current_team(new_member)
            self.breakout_teams_trial.close_current_team()
            if len(self.breakout_teams_trial.get_unassigned_members()) < demanded_team_size * 2:
                self.build_last_team()

    def build_last_team(self):
        for candidate in self.members:
            if not self.breakout_teams_trial.any_team_contains(candidate):
                self.visavis_trial.increase_visits(candidate, self.breakout_teams_trial.get_current_team())
                self.breakout_teams_trial.add_member_to_current_team(candidate)
        self.breakout_teams_trial.close_current_team()

    def get_current_breakout_teams(self):
        return self.breakout_teams.get_teams()

    def get_current_visavis(self):
        return self.visavis.visavis_matrix

    def get_name(self):
        return self.name

    # best partner is someone who has rarely seen the others who are already in the current team
    #              and who is not yet in any other breakout team
    def find_best_partner(self):
        for candidate in self.breakout_teams_trial.overall_members:
            if not self.breakout_teams_trial.any_team_contains(candidate):
                if self.is_best_partner(candidate, self.breakout_teams_trial.get_current_team()):
                    return candidate
        # no good candidate found, so we just return first one that is not already assigned
        for candidate in self.breakout_teams_trial.overall_members:
            if not self.breakout_teams_trial.any_team_contains(candidate):
                return candidate

    # 'selten gesehen' heisst: nicht mehr als einmal oefters als die anderen
    def is_best_partner(self, candidate, team):
        minimal_visits = self.visavis_trial.get_minimum_of_current_visits()
        for member in team:
            if self.visavis_trial.get_visits(candidate, member) > (minimal_visits + 1):
                return False
        return True

    def create_sequence_of_breakout_teams(self, demanded_team_sizes):
        demanded_team_sizes = self.remove_empty_items(demanded_team_sizes)
        session_number = 0
        for team_size in demanded_team_sizes:
            if (int(team_size) > 0) and (int(team_size) < 5):
                self.create_next_breakout_teams(int(team_size))
                session_number += 1
                self.add_teams_to_html_result(session_number)

    def add_teams_to_html_result(self, session_number):
        self.html_result += "<br><h3>Breakout Session "
        self.html_result += str(session_number)
        self.html_result += ": "
        for team in self.breakout_teams.get_teams():
            self.html_result += "( "
            for member in team:
                self.html_result += member
                self.html_result += " "
            self.html_result += ")  "
        self.html_result += "</h3>"

    def get_formatted_result(self):
        return self.html_result

    def clean_list(self, my_list):
        return self.remove_duplicate_items(self.remove_empty_items(my_list))

    def remove_empty_items(self, my_list):
        clean_list = []
        for item in my_list:
            if item is not "":
                clean_list.append(item)
        return clean_list

    def remove_duplicate_items(self, my_list):
        return list(dict.fromkeys(my_list))

