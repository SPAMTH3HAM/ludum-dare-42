import pygame
class CreateText:
    def __init__(self, width, height, TEXT_START_X=0, TEXT_START_Y=0):
        self.screen_width = width
        self.screen_height = height
        self.startscreen = pygame.display.set_mode((self.screen_width, self.screen_height),pygame.NOFRAME)
        self.TEXT_START_X = TEXT_START_X
        self.TEXT_START_Y = TEXT_START_Y
        self.textstart = [TEXT_START_X, TEXT_START_Y]
        self.text = None
        self.color = (0, 0, 0)


        self.font = pygame.font.Font("assets/Phone Font.ttf", 50)
        self.lines = []
        self.xoffsets = []
        self.yoffsets = []

        self.phoneBackground = pygame.image.load("assets/phone zoom screens/phone zoom.png")
        self.textBox = pygame.image.load("assets/text box.png")

    def AddText(self, ulines, xoffs=0, yoffs=0):
        self.lines.append(ulines)
        self.xoffsets.append(xoffs)
        self.yoffsets.append(yoffs)

    def DrawRegionSelect(self, object):
        self.AddText(object.ps[6][0], 1000)
        self.AddText(object.ps[6][1], 1250)
        self.AddText(object.ps[6][2], 1500)
        self.AddText(object.ps[6][3], 1000, 64)
        self.AddText(object.ps[6][4], 1250, 64)
        self.AddText(object.ps[6][5], 1500, 64)

    # def MapUpdate():




    def SetColor(self, r=0, g=0, b=0):
        self.color = (r, g, b)

    def ClearDisplayText(self):
        self.lines = []
        self.xoffsets = []
        self.yoffsets = []


    def ShowDisplayText(self):
        self.startscreen.blit(self.phoneBackground, (0,0))
        self.startscreen.blit(self.textBox, (24,743))
        for line , xoffset, yoffset in zip(self.lines, self.xoffsets, self.yoffsets):
            self.text = self.font.render(line, True, self.color)
            self.startscreen.blit(self.text, [self.TEXT_START_X+xoffset,self.TEXT_START_Y+yoffset])
            pygame.display.flip()
