import SmartTeam


def run():
    team = ["Peter", "Luci", "Anna", "Flo", "Yussef", "Rahel", "Paul", "Orwid", "Zachery", "Steve", "Cindy", "Manu"]

    smart_team = SmartTeam.SmartTeam("Test Team", team)

    smart_team.create_next_breakout_teams(4)
    print(smart_team.get_current_breakout_teams())
    print(smart_team.get_current_visavis())
    smart_team.create_next_breakout_teams(3)
    print(smart_team.get_current_breakout_teams())
    print(smart_team.get_current_visavis())
    smart_team.create_next_breakout_teams(3)
    print(smart_team.get_current_breakout_teams())
    print(smart_team.get_current_visavis())
    smart_team.create_next_breakout_teams(3)
    print(smart_team.get_current_breakout_teams())
    print(smart_team.get_current_visavis())
    smart_team.create_next_breakout_teams(2)
    print(smart_team.get_current_breakout_teams())
    print(smart_team.get_current_visavis())
    smart_team.create_next_breakout_teams(2)
    print(smart_team.get_current_breakout_teams())
    print(smart_team.get_current_visavis())


if __name__ == '__main__':
    run()
