#coding=utf-8
class Student(object):

    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print '%s: %s' %(self.name,self.score)

bart=Student('bart',200)
bart.print_score()

print bart

#和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
tom=Student('tom',100)
tom.age=300
tom.age

#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student1(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self,name):
        self.__name=name
    def set_score(self,score):
        self.__score=score

#改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了
#在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
# 不是private变量，所以，不能用__name__、__score__这样的变量名。
#按照约定俗成的规定，当你看到这样的变量时(__xxxx__)，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”

#双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量
bart = Student1('bart', 200)
bart._Student1__name
#但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名