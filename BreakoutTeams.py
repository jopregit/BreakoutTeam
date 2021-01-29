import random

class BreakoutTeams:

    def __init__(self, overallMembers, demandedTeamSize):
        self.demandedTeamSize = demandedTeamSize
        self.overallMembers = overallMembers
        self.breakoutTeams = []
        self.currentTeam = []

    def rotateMembers(self, timesToRotate):
        i = 0
        while i < timesToRotate:
            first = self.overallMembers[0]
            self.overallMembers.remove(first)
            self.overallMembers.append(first)
            i += 1

    def randomizeMembers(self):
        i = 0
        randomlyOrderedMembers = []
        while i < len(self.overallMembers):
            n = random.randint(0, len(self.overallMembers) - 1)
            member = self.overallMembers[n]
            self.overallMembers.remove(member)
            randomlyOrderedMembers.append(member)
        self.overallMembers = randomlyOrderedMembers


    def addMemberToCurrentTeam(self, member):
        self.currentTeam.append(member)

    def anyTeamContains(self, candidate):
        if candidate in self.currentTeam:
            return True
        for team in self.breakoutTeams:
            if candidate in team:
                return True
        return False

    def getNumberOfTeams(self):
        return len(self.breakoutTeams)

    def getCurrentTeam(self):
        return self.currentTeam

    def getTeams(self):
        return self.breakoutTeams

    def closeCurrentTeam(self):
        self.breakoutTeams.append(self.currentTeam)
        self.currentTeam = []

    def allMembersAreAssigned(self):
        if len(self.getUnassignedMembers()) == 0:
            return True
        else:
            return False

    def getUnassignedMembers(self):
        unassignedMembers = []
        for candidate in self.overallMembers:
            if not self.anyTeamContains(candidate):
                unassignedMembers.append(candidate)
        return unassignedMembers


    def currentTeamIsComplete(self):
        if len(self.currentTeam) == int(self.demandedTeamSize):
            return True
        else:
            return False
