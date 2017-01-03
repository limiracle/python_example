class Handler():
    def callback(self,prefix,name,*args):
        method=getattr(self,prefix+name,None)
        if callable(method):
            return method(*args)
    def start(self,name):
        self.callback('start_',name)
    def end(self,name):
        self.callback('end_', name)
    def sub(self,name):
        def substitution(match):
            result=self.callback("sub_",name,match)
            if result is None:match.group(0)
            return result
        return substitution

class HTMLRenderer(Handler):
    def start_document(self):
        print '<html><head><title>...</title></head><body>'
    def end_document(self):
        print '</body></html>'
    def start_paragraph(self):
        print '<p>'
    def end_paragraph(self):
        print '</p>'
    def start_heading(self):
        print '<h2>'
    def end_heading(self):
        print '</h2>'
    def start_list(self):
        print '<ul>'
    def end_list(self):
        print '</ul>'

    def start_number_list(self):
        print '<ol>'
    def end_number_list(self):
        print '</ol>'

    def start_number_listitem(self):
        print '<li>'
    def end_number_listitem(self):
        print '</li>'

    def start_listitem(self):
        print '<li>'
    def end_listitem(self):
        print '</li>'
    def start_title(self):
        print '<h1>'
    def end_title(self):
        print '</h1>'
    def start_hr(self):
        print '<hr />'
    def start_h1(self):
        print '<h1>'
    def end_h1(self):
        print '</h1>'

    def start_h2(self):
        print '<h2>'
    def end_h2(self):
        print '</h2>'

    def start_h3(self):
        print '<h3>'
    def end_h3(self):
        print '</h3>'
    def sub_emphasis(self,match):
        return '<em>%s</em>' % match.group(1)
    def sub_url(self,match):
        mailName=match.group(1)
        mailPath=match.group(2)
        return '<a href="%s">%s</a>' % (mailPath[1:len(mailPath)-1],mailName[1:len(mailName)-1])
    def sub_mail(self,match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1),match.group(1))
    def sub_br(self,match):
        return '<br/>'
    def sub_strong(self,match):
        return '<strong>%s</strong>' % match.group(1)
    def sub_code(self,match):
        return '<code>%s</code>' % match.group(1)
    def feed(self,data):
        print data