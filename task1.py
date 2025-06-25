class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def insertion_sort(self):
        if not self.head or not self.head.next:
            return
        
        sorted_list = None
        current = self.head
        
        while current:
            next_node = current.next
            if not sorted_list or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                temp = sorted_list
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node
        
        self.head = sorted_list
    
    def merge_sorted_lists(list1, list2):
        #Об'єднання двох відсортованих списків в один відсортований
        result = LinkedList()
        a = list1.head if list1 else None
        b = list2.head if list2 else None
        
        while a and b:
            if a.data <= b.data:
                result.append(a.data)
                a = a.next
            else:
                result.append(b.data)
                b = b.next
        
        while a:
            result.append(a.data)
            a = a.next
        
        while b:
            result.append(b.data)
            b = b.next
        
        return result

# Приклади використання
if __name__ == "__main__":
    print("1. Тестування реверсування списку:")
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print("Початковий список:")
    ll.print_list()
    ll.reverse()
    print("Реверсований список:")
    ll.print_list()
    
    print("\n2. Тестування сортування списку:")
    ll2 = LinkedList()
    ll2.append(4)
    ll2.append(2)
    ll2.append(1)
    ll2.append(3)
    print("Початковий список:")
    ll2.print_list()
    ll2.insertion_sort()
    print("Відсортований список:")
    ll2.print_list()
    
    print("\n3. Тестування об'єднання двох відсортованих списків:")
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)
    
    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)
    
    print("Перший відсортований список:")
    list1.print_list()
    print("Другий відсортований список:")
    list2.print_list()
    
    merged = LinkedList.merge_sorted_lists(list1, list2)
    print("Об'єднаний відсортований список:")
    merged.print_list()