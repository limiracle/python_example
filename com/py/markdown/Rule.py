class Rule:
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True

class HeadingRule(Rule):
    type='heading'
    def condition(self,block):
        return not '\n' in block and len(block)<3 and not block[-1]==':'

class TitleRule(HeadingRule):
    type='title'
    first=True
    def condition(self,block):
        if not self.first: return False
        self.first = False
        return HeadingRule.condition(self,block)
class ListItemRule(Rule):
    type='listitem'
    def condition(self,block):
        return block[0]=='*'
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True

class NumberListItemRule(Rule):
    type='number_listitem'
    def condition(self,block):
        block=block.strip();
        return block[0].isdigit() and block[1:2]=='.'
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block[2:].strip())
        handler.end(self.type)
        return True


class NumberListRule(NumberListItemRule):
    type='number_list'
    inside=False
    def condition(self,block):
        return True
    def action(self,block,handler):
        if not self.inside and NumberListItemRule.condition(self,block):
            handler.start(self.type)
            self.inside=True
        elif self.inside and not NumberListItemRule.condition(self,block):
            handler.end(self.type)
            self.inside=False
        return False



class ListRule(ListItemRule):
    type='list'
    inside=False
    def condition(self,block):
        return True
    def action(self,block,handler):
        if not self.inside and ListItemRule.condition(self,block):
            handler.start(self.type)
            self.inside=True
        elif self.inside and not ListItemRule.condition(self,block):
            handler.end(self.type)
            self.inside=False
        return False
class ParagraphRule(Rule):
    type='paragraph'
    def condition(self,block):
        return True


class H1Rule(Rule):
    type='h1'
    def condition(self,block):
        return block[0]=='#'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True
class H2Rule(Rule):
    type='h2'
    def condition(self,block):
        return block[0:2]=='##'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[2:].strip())
        handler.end(self.type)
        return True
class H3Rule(Rule):
    type='h3'
    def condition(self,block):
        return block[0:3]=='###'
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[3:].strip())
        handler.end(self.type)
        return True
class HrRule(Rule):
    type='hr'
    def condition(self,block):
        return block[:3]=='---'
    def action(self, block, handler):
       handler.start(self.type)
       return True