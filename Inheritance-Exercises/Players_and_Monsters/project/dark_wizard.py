from Players_and_Monsters.project.wizard import Wizard


class DarkWizard(Wizard):

    def __init__(self, username, level):
        Wizard.__init__(self, username, level)