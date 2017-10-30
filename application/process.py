class ClashBot:
    def __init__(self, name, options):
        self.name = name
        self.options = options

def process(fileLocation, array = False):
    bots = []
    tree = ET.parse(fileLocation)
    root = tree.getroot()
    for child in root:
        new_capitol = ClashBot(child.attrib, child.find('config').text)
        bots.append(new_capitol)
    return bots