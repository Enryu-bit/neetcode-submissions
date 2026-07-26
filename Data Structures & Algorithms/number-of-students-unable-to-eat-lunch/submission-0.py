class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        no=0
        students=deque(students)
        sandwiches=deque(sandwiches)
        while no<len(students):
            if len(sandwiches)==0:
                return len(students)
            if sandwiches[0]==students[0]:
                sandwiches.popleft()
                students.popleft()
                no=0
            else:
                students.append(students.popleft())
                no+=1
        return len(students)
            
        