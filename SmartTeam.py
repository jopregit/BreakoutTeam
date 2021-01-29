from BreakoutTeams import BreakoutTeams
from Visavis import Visavis
import copy


class SmartTeam:

    def __init__(self, name, team):
        self.debug = True
        self.name = name
        self.members = team
        self.breakoutTeams = None
        self.breakoutTeamsTrial = None
        self.visavis = Visavis(self.members)
        self.visavisTrial = Visavis
        self.breakoutTeamsTrial = None
        self.currentNumberOfTrials = 0
        self.maxTrials = 100000

    # heuristic: hope that after enough tries (with randomized order in list of members) ideal groups are found
    def createNextBreakoutTeams(self, demandedTeamSize):
        self.breakoutTeams = BreakoutTeams(self.members, demandedTeamSize)
        self.currentNumberOfTrials = 0
        while self.currentNumberOfTrials < self.maxTrials:
            self.currentNumberOfTrials += 1
            self.initiateNextTrial()
            self.tryNextBreakoutTeams(demandedTeamSize)
            if self.visavisTrial.isIdeal():
                self.breakoutTeams = self.breakoutTeamsTrial
                self.visavis = self.visavisTrial
                print("Ideal team found after " + self.currentNumberOfTrials.__str__() + " trials")
                return
        print("Unfortunately no ideal solution has been found.")
        self.breakoutTeams = self.breakoutTeamsTrial
        self.visavis = self.visavisTrial

    def initiateNextTrial(self):
        self.breakoutTeamsTrial = copy.deepcopy(self.breakoutTeams)
        self.visavisTrial = copy.deepcopy(self.visavis)
        self.breakoutTeamsTrial.randomizeMembers()

    def tryNextBreakoutTeams(self, demandedTeamSize):
        while not self.breakoutTeamsTrial.allMembersAreAssigned():
            while not self.breakoutTeamsTrial.currentTeamIsComplete():
                newMember = self.findBestPartner()
                self.visavisTrial.increaseVisits(newMember, self.breakoutTeamsTrial.getCurrentTeam())
                self.breakoutTeamsTrial.addMemberToCurrentTeam(newMember)
            self.breakoutTeamsTrial.closeCurrentTeam()
            if len(self.breakoutTeamsTrial.getUnassignedMembers()) < demandedTeamSize * 2:
                self.buildLastTeam()

    def buildLastTeam(self):
        for candidate in self.members:
            if not self.breakoutTeamsTrial.anyTeamContains(candidate):
                self.visavisTrial.increaseVisits(candidate, self.breakoutTeamsTrial.getCurrentTeam())
                self.breakoutTeamsTrial.addMemberToCurrentTeam(candidate)
        self.breakoutTeamsTrial.closeCurrentTeam()

    def getCurrentBreakoutTeams(self):
        return self.breakoutTeams.getTeams()

    def getCurrentVisavis(self):
        return self.visavis.visavisMatrix

    def getName(self):
        return self.name


    # best partner is someone who has rarely seen the others who are already in the current team
    #              and who is not yet in any other breakout team
    def findBestPartner(self):
        for candidate in self.breakoutTeamsTrial.overallMembers:
            if not self.breakoutTeamsTrial.anyTeamContains(candidate):
                if self.isBestPartner(candidate, self.breakoutTeamsTrial.getCurrentTeam()):
                     return candidate
        # no good candidate found, so we just return last one
        return candidate

    # 'selten gesehen' heisst: nicht mehr als einmal oefters als die anderen
    def isBestPartner(self, candidate, team):
        minimalVisits = self.visavisTrial.getMinimumOfCurrentVisits()
        for member in team:
            if self.visavisTrial.getVisits(candidate, member) > (minimalVisits + 1):
                return False
        return True

