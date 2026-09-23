class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 
        pair = [(p,s) for p,s in zip(position, speed)]
        # position=[10,8,0,5,3], speed=[2,4,1,1,3] becomes [(10,2),(8,4),(0,1),(5,1),(3,3)]

        pair.sort(reverse=True)
        # the car closest to the target comes first
        stack = []
        for p,s in pair:
            stack.append((target-p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                # removes this car's time since it isn't a seperate fleet
        return len(stack)




        