numbers= list(range(1,10001))
equivalence_classes ={0:[],1:[],2:[],3:[],4:[]}
for num in  numbers:
    remainder = num % 5
    equivalence_classes[remainder].append(num)
union_of_classes = set()
for key in equivalence_classes:
    union_of_classes.update(equivalence_classes[key])
is_valid = (set(numbers)==union_of_classes)
print(f"Validity of equivalence classes :{is_valid}")