class Visavis:

    def __init__(self, team):
        self.team = team
        self.visavisMatrix = {}
        self.initializeVisavisMatrix()


    def initializeVisavisMatrix(self):
        for member_1 in self.team:
            for member_2 in self.team:
                if member_1 < member_2:
                    self.visavisMatrix[self.joinToKey(member_1, member_2)] = 0

    def joinToKey(self, member_1, member_2):
        if member_1 < member_2:
            return (member_1 + "---" + member_2)
        else:
            return (member_2 + "---" + member_1)

    def getMinimumOfCurrentVisits(self):
        #nasty! find proper initial value
        currentMinimumValue = 1000
        for key in self.visavisMatrix:
            value = self.visavisMatrix[key]
            if value < currentMinimumValue:
                currentMinimumValue = value
        return currentMinimumValue

    def getVisits(self, member_1, member_2):
        return self.visavisMatrix[self.joinToKey(member_1, member_2)]

    def increaseVisits(self, newMember, breakoutTeam):
        for member in breakoutTeam:
            self.visavisMatrix[self.joinToKey(newMember, member)] += 1

    # ideal heisst: kein Paar hat sich mehr als einmal oefters gesehen als die anderen Paare
    def isIdeal(self):
        minimalVisits = self.getMinimumOfCurrentVisits()
        for key in self.visavisMatrix:
            if self.visavisMatrix[key] > (minimalVisits + 1):
                return False
        return True

