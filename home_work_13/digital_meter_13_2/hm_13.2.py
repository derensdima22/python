def try_step(step_function):
    try:
        step_function()
    except ValueError as e:
        print(e)

class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        self.current = start

    def set_max(self, max):
        self.max_value = max

    def set_min(self, min):
        self.min_value = min

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Maximum achieved")

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Minimum achieved")

    def get_current(self):
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
print(f'Test 1: {counter.get_current()}')

try_step(counter.step_up)

print(f'Test 2: {counter.get_current()}')

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
print(f'Test 3: {counter.get_current()}')

try_step(counter.step_down)


print(f'Test 4: {counter.get_current()}')

