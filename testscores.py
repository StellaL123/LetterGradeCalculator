# Create a classroom grades simulation:
  # 0. Don't import any Python math libraries, we'll create custom functions for each of these tasks
  # 1. Create 5 students. Each student has 5 test grades from 0-100, unsorted.
  # 2. Write a function average_score to find each student's average score. This is their overall grade in the class.
  # 3. Write a function assign_letter_grade to determine the student's letter grade given their score.
  # 4. At the end of the semester, each test score is bumped up 10 points: use any list iteration method (map, for loop, etc) to add 10 points to each student's scores.
  # 5. At the end of the semester, we remove the lowest test score. Use any solution to filter out the lowest score.
  # Bonus: calculate standard deviation and variance for each student, and for the overall class

emma = [92, 90, 84, 93, 97]
bob = [74, 79, 84, 86, 73]
anita = [91, 89, 92, 92, 90]
john = [98, 99, 97, 96, 98]
sam = [68, 57, 62, 73, 76]

# .remove() always returns None
print("Original:", emma)

emma.remove(min(emma))
print(".remove():", emma, type(emma))  # This permanently alters the emma list, changing it "in-place"

emma = [92, 90, 84, 93, 97]
emma.remove(min(emma)) # None
print("list:", list(emma), type(emma)) # already a list, so casting to a list does nothing

# some functions do return the list back. Therefore we should store it back into the list variable
# emma = sorted(emma)


# Wrapper function for min()
# add our own custom code to the min() function
def lowest_score(scores):
    low_score = min(scores)
    return low_score

def average_score(scores):
    # global: accessible anywhere
    # avoid naming variables to reserved or global keywords/functions
    # sum = sum(scores) # replace the global variable sum with this variable
    average = sum(scores) / len(scores)
    return average

def add_points(x):
    return x + 10

def standard_deviation_and_variance(scores, x):
    # dif_from_average = [(x - average_score(scores)) ** 2 for x in scores]
    # map
    dif_from_average = list(map(lambda x: x - average_score(scores) ** 2, scores))
    # for x in scores:
    #     x = (x - average_score(scores)) ** 2
    #     dif_from_average.append(x)
    standard_deviation = (sum(dif_from_average)/len(dif_from_average)) ** 0.5
    variance = standard_deviation ** 2
    print("Your standard deviation is " + str(standard_deviation) + " and your variance is " + str(variance))

def letter_grade(scores, x):
    if x >= 93:
        letter_grade = "A"
    elif x >= 90:
        letter_grade = "A-"
    elif x >= 87:
        letter_grade = "B+"
    elif x >= 83:
        letter_grade = "B"
    elif x >= 80:
        letter_grade = "B-"
    elif x >= 77:
        letter_grade = "C+"
    elif x >= 73:
        letter_grade = "C"
    elif x >= 70:
        letter_grade = "C-"
    elif x >= 67:
        letter_grade = "D+"
    elif x >= 63:
        letter_grade = "D"
    elif x >= 60:
        letter_grade = "D-"
    else:
        letter_grade = "Fail"
    scores = str(scores)
    print("Your 5 tests scores are " + scores + " and you will receive a(n) " + letter_grade + " for this course this year!")


emma = list(map(add_points, emma))
bob = list(map(add_points, bob))
anita = list(map(add_points, anita))
john = list(map(add_points, john))
sam = list(map(add_points, sam))

emma.remove(lowest_score(emma))
bob.remove(lowest_score(bob))
anita.remove(lowest_score(anita))
john.remove(lowest_score(john))
sam.remove(lowest_score(sam))

def main():

    letter_grade(emma, average_score(emma))
    standard_deviation_and_variance(emma, average_score(emma))

    letter_grade(bob, average_score(bob))
    standard_deviation_and_variance(bob, average_score(bob))

    letter_grade(anita, average_score(anita))
    standard_deviation_and_variance(anita, average_score(anita))

    letter_grade(john, average_score(john))
    standard_deviation_and_variance(john, average_score(john))

    letter_grade(sam, average_score(sam))
    standard_deviation_and_variance(sam, average_score(sam))


main()


# emma = emma.remove(min(emma)) #This makes my list a nonetype :( very sad so I won't be using it... ughh my code broke so many times due to this
# bob = bob.remove(min(bob))
# anita = anita.remove(min(anita))
# john = john.remove(min(john))
# sam = sam.remove(min(sam))


# cathys_score = average_score(cathy) # gets this student's average test score
# assign_letter_grade(cathys_score) # Returns 'A'
# map(cathy) # add 10 to each score

# 5: Option 1, use .filter()
# lowest_score = min(cathy) # returns lowest score
# filter(list(lambda x: x > lowest_score, cathy))

# Option 2:
# cathy.remove(lowest_score)
#
# # each students have 30 assignments over the year
# # To remove 5 assignments
# cathy.remove(first_lowest)
# cathy.remove(second_lowest)
# cathy.remove(third_lowest)
# cathy.remove(fourth_lowest)
# cathy.remove(five_lowest)

# Option 3:
#sorted() # Sorts a list
# Then we can remove the first element (if sorted from least to greatest)
