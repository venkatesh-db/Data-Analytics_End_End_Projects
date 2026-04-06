
# numpy array 
import numpy as np

#machine learning works with numpy array 
# machine learning lib works two numpy array 
# machine learning predict the future  data 


expeirnce = np.array([1, 2, 3, 4, 5])
salary= np.array([1000, 2000, 3000, 4000, 5000])

print("Experience:", expeirnce)
print("Salary:", salary)

from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(expeirnce.reshape(-1,1), salary)

predicted_salary = model.predict([[6]])
print("Predicted Salary for 6 years of experience:", predicted_salary)
