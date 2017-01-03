import re,sys

import util
from Rule import *
from handlers import *



class Parser:
    def __init__(self,handler):
        self.handler=handler
        self.rules=[]
        self.filters=[]
    def addRule(self,rule):
        self.rules.append(rule)
    def addFilter(self,pattern,name):
        def filter(block,handler):
            return re.sub(pattern,handler.sub(name),block)
        self.filters.append(filter)
    def parse(self,file):
        self.handler.start('document')
        for block in util.blocks(file):
            for filter in self.filters:
                block=filter(block,self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last=rule.action(block,self.handler)
                    if last: break
        self.handler.end('document')

class BasicTextParser(Parser):
    def __init__(self,handler):
        Parser.__init__(self,handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(NumberListRule())
        self.addRule(NumberListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())

        self.addRule(H3Rule())
        self.addRule(H2Rule())
        self.addRule(H1Rule())
        self.addRule(H1Rule())
        self.addRule(HrRule())

        self.addRule(ParagraphRule())
        self.addFilter(r'__(.+?)__', 'strong')
        self.addFilter(r'\*\*(.+?)\*\*', 'strong')
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'_(.+?)_', 'emphasis')
        self.addFilter(r'`(.+?)`', 'code')
        self.addFilter(r'(\[.+?\])(\(http://[\.a-zA-Z/]+\))', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')
        self.addFilter(r'(\n)', 'br')

handler=HTMLRenderer()
parser=BasicTextParser(handler)

parser.parse(open('D:/markdown.txt'))