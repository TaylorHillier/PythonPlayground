import numpy as np;

# Generate a 100 x 5 numpy array of random integers between 0 and 100
# rows represent students and columns represent exam scores
data = np.random.randint(0, 100, (100, 5))

# Shape of data
print("Shape of data:", data.shape)
# dtype of data
print("Data type of data:", data.dtype)
# min of data
print("Minimum value in data:", np.min(data))
# max of data
print("Maximum value in data:", np.max(data))
# mean of data
print("Mean value of data:", np.mean(data))

# slice out first 10 students' scores
first_10_students = data[:10]
print("First 10 students' scores:\n", first_10_students)

# slice out last exam column for all students
last_exam_scores = data[:, -1]
print("Last exam scores for all students:\n", last_exam_scores)

#slice out every other students' scores
every_other_student = data[::2]
print("Every other student's scores:\n", every_other_student)

# get all students who scored above 90 in the first exam and below 50 on exam 3
high_low_scorers = data[(data[:, 0] > 90) & (data[:, 2] < 50)]
print("Students who scored above 90 in the first exam and below 50 on exam 3:\n", high_low_scorers)

"""
Aggregations + Broadcasting

Aggregation is the process of summarizing data, often by computing a single value
that represents a larger set of values. Common aggregation functions include sum, mean, etc.

Broadcasting is a mechanism that allows numpy to perform operations on arrays of different shapes
"""

# Calculate the mean score per student(axis=1) and per exam(axis=0)
# axis 1 is rows (students), axis 0 is columns (exams)
mean_per_student = np.mean(data, axis=1)
mean_per_exam = np.mean(data, axis=0)
print("Mean score per student:\n", mean_per_student)
print("Mean score per exam:\n", mean_per_exam)

#Normalize scores to a 0-1 range using min-max normalization
min_scores = np.min(data,axis=0)
max_scores = np.max(data,axis=0)

# the formula for min-max normalization is: 
# (x - min) / (max - min)
# in this case, x is the data array and min and max are the min_scores and max_scores arrays, python automatically
# handles arrays for us, meaning we don't need to loop through each element, it uses broadcasting to do the operation
# again, broadcasting is a mechanism that allows numpy to perform operations on arrays of different shapes
# very simply explained - the array is treated as if it were a single value, and the operation is performed on each element of the array
normalized_data = (data - min_scores) / (max_scores - min_scores)

print("Normalized data:\n", normalized_data)

# Curve the grades of exam 2 for all students by adding 10 points, but cap at 100
# np.clip is the right tool here because it allows us to set a minimum and maximum value while performing the operation
data[:, 1] = np.clip(data[:,1] + 10, 0, 100)
print("Data after curving exam 2:\n", data)


"""
Reshaping + Stacking

Reshaping is the process of changing the shape of an array without changing its data.
Stacking is the process of combining multiple arrays into a single array along a specified axis.
"""

# reshape data into a (20, 25) shape, then back to (100, 5)
# the reshaped data will have 20 rows and 25 columns
# the (5, 100) data can be reshaped into (20, 25) because 5*100 = 20*25 = 500
# if we tried to reshape it into (30, 20), it would fail because 5*100 != 30*20
# the benefit of reshaping is that it allows us to change the way we view the data without changing the data itself
reshaped_data = data.reshape(20, 25)
print("Reshaped data (20, 25):\n", reshaped_data)

restored_data = reshaped_data.reshape(100, 5)
print("Restored data (100, 5):\n", restored_data)

# stack data into a 1d array of student ID's (1 to 100), then stack it alongside the exam scores into a (100, 6) array
student_ids = np.arange(1, 101)
student_data_with_ids = np.column_stack((student_ids, data))
print("Student data with IDs (100, 6):\n", student_data_with_ids)

"""
Linear Algebra
1. Matrix Ops
2. Correlation
"""

# Treat the (100,5) score matrix as x
# generate a (5, 1) weight vector
# multiply x @ weights to get a final grade for each student
# verify dimensions align

# the 5 in random weights corresponds to the 5 exams, creates a vector of weights for each exam
weights = 5 * np.random.random_sample((5,1))
weights = weights / np.sum(weights)  # normalize weights to sum to 1
final_grades = data @ weights
verify_shape = (final_grades.shape == data.shape)  # should be (100, 1)
print("Final grades shape (should be (100, 1)):", final_grades.shape)
print("Shape verification (should be True):", verify_shape)
print("Final grades:\n", final_grades)

# calculate the correlation matrix
correlation_matrix = np.corrcoef(data, rowvar=False)
print("Correlation matrix between exams:\n", correlation_matrix)

