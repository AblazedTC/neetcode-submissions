class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # #Remember I just have to return T/F
        # targetTriplets = []

        # #if theres already a valid triple from the jump
        # if triplets in target:
        #     return True

        # #I think we should store all the triples that have valid nums and we can run some simple algo that
        # #determins if they can be combined

        # for x,y,z in triplets:
        #     if x or y or z in target:
        #         targetTriplets.append([x,y,z])

        found = [False, False, False]

        for x, y, z in triplets:
            # skip anything that overshoots target
            if x > target[0] or y > target[1] or z > target[2]:
                continue

            if x == target[0]:
                found[0] = True
            if y == target[1]:
                found[1] = True
            if z == target[2]:
                found[2] = True

        return all(found)
        