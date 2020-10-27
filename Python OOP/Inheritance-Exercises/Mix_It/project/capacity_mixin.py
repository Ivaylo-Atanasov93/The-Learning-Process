class CapacityMixin:

    def get_capacity(self, capacity, amount):
        if amount > capacity:
            return 'Capacity reached!'
        return capacity - amount