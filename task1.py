# Ініціалізуємо вузол
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Ініціалізуємо зв'язаний список
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        self.length += 1

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            self.length -= 1
            return

        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next

        if cur:
            prev.next = cur.next
            self.length -= 1

    def search_element(self, data: int):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            end = " -> " if current.next else ""
            print(current.data, end=end)
            current = current.next

    # Реверсування списку
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування списку злиттям
    def sort_list(self):
        if self.length <= 1 or not self.head:
            return  # список вже відсортований або порожній

        # Виклик рекурсії для підсписків
        self.head = self._merge_sort(self.head, self.length)

    def _merge_sort(self, head, length):
        if length <= 1 or not head:
            return head

        # Пошук середини через довжину
        mid_index = length // 2
        prev = None
        cur = head
        for _ in range(mid_index):
            prev = cur
            cur = cur.next

        # Поділ списку навпіл
        prev.next = None
        left = head
        right = cur

        # Рекурсивне сортування лівого та правого підсписків
        left_sorted = self._merge_sort(left, mid_index)
        right_sorted = self._merge_sort(right, length - mid_index)

        # Злиття двох відсортованих списків
        return self._sorted_merge(left_sorted, right_sorted)

    # Об'єднання двох відсортованих однозв'язних списки в один відсортований список
    @staticmethod
    def merge_sorted_lists(l1, l2):
        result = LinkedList()
        result.head = LinkedList._sorted_merge(l1.head, l2.head)
        result.length = l1.length + l2.length
        return result

    # Сортування та злиття двох списків
    @staticmethod
    def _sorted_merge(a, b):
        pre_head = Node()
        tail = pre_head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b

        # Повертає нову голову відсортованого списку
        return pre_head.next


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.insert_at_end(1)
    ll1.insert_at_end(8)
    ll1.insert_at_end(2)
    ll1.insert_at_end(10)
    ll1.insert_at_end(5)

    ll2 = LinkedList()
    ll2.insert_at_end(2)
    ll2.insert_at_end(4)
    ll2.insert_at_end(6)
    ll2.insert_at_end(1)
    ll2.insert_at_end(12)

    print("\n--------- ПЕРШИЙ СПИСОК ---------")
    print("Початковий список:")
    ll1.print_list()

    print("\nРеверс:")
    ll1.reverse_list()
    ll1.print_list()

    print("\nСортування злиттям:")
    ll1.sort_list()
    ll1.print_list()

    print("\n\n--------- ДРУГИЙ СПИСОК ---------")
    print("Початковий список:")
    ll2.print_list()

    print("\nРеверс:")
    ll2.reverse_list()
    ll2.print_list()

    print("\nСортування злиттям:")
    ll2.sort_list()
    ll2.print_list()

    print("\n\n--- СПИСОК З 2 СОРТОВАНИХ СПИСКІВ ---")
    merged = LinkedList.merge_sorted_lists(ll1, ll2)
    merged.print_list()
