from Players_and_Monsters.project.hero import Hero


class DarkWizard(Hero):

    def __init__(self, name, level):
        Hero.__init__(self, name, level)