class Node:
    def __init__(self, name, entropy, children, father, number, data_frame, answer, column):
        self.name = name
        self.entropy = entropy
        self.father = father
        self.children = children
        self.data_frame = data_frame
        self.number = number
        self.column = column
        self.answer = answer

    def set_entropy(self, ent):
        self.entropy = ent

    def set_children(self, c):
        self.children.append(c)

    def set_father(self, f):
        self.father = f

    def show_tree(self, spaces):
        if self.name != self.data_frame[0][-1]:
            print("  " * spaces + self.column + ": " +self.name)
        if self.answer:
            print ("  " * spaces + "  " +  "ANSWER: " + self.answer)
        for child in self.children:
            child.show_tree(spaces + 1)
