"""
Student information for this assignment:

On my honor, Palash, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: ppp625
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = None

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"



class LinkedList:
    def __init__(self):
        self.head = None

    def insert_term(self, coeff, exp):
        if coeff == 0:
            return
            
        new_node = Node(coeff, exp)
        
        if not self.head:
            self.head = new_node
            return
            
        if exp >= self.head.exp:
            if exp == self.head.exp:
                self.head.coeff += coeff
                if self.head.coeff == 0:
                    self.head = self.head.next
            else:
                new_node.next = self.head
                self.head = new_node
            return
            
        prev = self.head
        curr = self.head.next
        while curr and curr.exp > exp:
            prev = curr
            curr = curr.next
            
        if curr and curr.exp == exp:
            curr.coeff += coeff
            if curr.coeff == 0:
                prev.next = curr.next
        else:
            new_node.next = curr
            prev.next = new_node

    def add(self, p):
        result = LinkedList()
        curr1 = self.head
        curr2 = p.head
        
        if not curr1 and not curr2:
            return result
        if not curr1:
            while curr2:
                result.insert_term(curr2.coeff, curr2.exp)
                curr2 = curr2.next
            return result
        if not curr2:
            while curr1:
                result.insert_term(curr1.coeff, curr1.exp)
                curr1 = curr1.next
            return result
            
        while curr1 or curr2:
            if not curr2 or (curr1 and curr1.exp > curr2.exp):
                result.insert_term(curr1.coeff, curr1.exp)
                curr1 = curr1.next
            elif not curr1 or (curr2 and curr2.exp > curr1.exp):
                result.insert_term(curr2.coeff, curr2.exp)
                curr2 = curr2.next
            else:  
                coeff_sum = curr1.coeff + curr2.coeff
                if coeff_sum != 0:
                    result.insert_term(coeff_sum, curr1.exp)
                curr1 = curr1.next
                curr2 = curr2.next
        return result

    def mult(self, p):
        result = LinkedList()
        curr1 = self.head
        
        if not curr1 or not p.head:
            return result
            
        while curr1:
            curr2 = p.head
            while curr2:
                coeff_prod = curr1.coeff * curr2.coeff
                exp_sum = curr1.exp + curr2.exp
                result.insert_term(coeff_prod, exp_sum)
                curr2 = curr2.next
            curr1 = curr1.next
        return result

    def __str__(self):
        if not self.head:
            return ""
        terms = []
        curr = self.head
        while curr:
            terms.append(f"({curr.coeff}, {curr.exp})")
            curr = curr.next
        return " + ".join(terms)

def main():
    p = LinkedList()
    n = int(input())
    for _ in range(n):
        coeff, exp = map(int, input().split())
        p.insert_term(coeff, exp)
    
    input()  
    
    q = LinkedList()
    m = int(input())
    for _ in range(m):
        coeff, exp = map(int, input().split())
        q.insert_term(coeff, exp)
    
    print(p.add(q))
    print(p.mult(q))

if __name__ == "__main__":
    main()
