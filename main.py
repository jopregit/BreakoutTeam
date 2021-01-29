import SmartTeam

def run():

    team = []
    team.append("Peter")
    team.append("Luci")
    team.append("Anna")
    team.append("Flo")
    team.append("Yussef")
    team.append("Rahel")
    team.append("Paul")
    team.append("Orwid")
    team.append("Zachery")
    team.append("Steve")
    team.append("Cindy")
    team.append("Manu")

    smartTeam = SmartTeam.SmartTeam("Test Team", team)

    smartTeam.createNextBreakoutTeams(3)
    print(smartTeam.getCurrentBreakoutTeams())
    print(smartTeam.getCurrentVisavis())
    smartTeam.createNextBreakoutTeams(3)
    print(smartTeam.getCurrentBreakoutTeams())
    print(smartTeam.getCurrentVisavis())
    smartTeam.createNextBreakoutTeams(3)
    print(smartTeam.getCurrentBreakoutTeams())
    print(smartTeam.getCurrentVisavis())
    smartTeam.createNextBreakoutTeams(2)
    print(smartTeam.getCurrentBreakoutTeams())
    print(smartTeam.getCurrentVisavis())
    smartTeam.createNextBreakoutTeams(2)
    print(smartTeam.getCurrentBreakoutTeams())
    print(smartTeam.getCurrentVisavis())
    smartTeam.createNextBreakoutTeams(2)
    print(smartTeam.getCurrentBreakoutTeams())
    print(smartTeam.getCurrentVisavis())
    smartTeam.createNextBreakoutTeams(2)
    print(smartTeam.getCurrentBreakoutTeams())
    print(smartTeam.getCurrentVisavis())
    smartTeam.createNextBreakoutTeams(2)
    print(smartTeam.getCurrentBreakoutTeams())
    print(smartTeam.getCurrentVisavis())


if __name__ == '__main__':
    run()



