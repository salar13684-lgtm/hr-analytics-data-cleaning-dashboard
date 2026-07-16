import pandas as pd
df = pd.read_excel(r"C:\Users\HP\Desktop\Excel  project CLEANING\new project\industry_employee_messy_dataset_10200_rows.xlsx")

#PART 1 DATA EXPLORATION
print (df.head())
print (df.tail())
print (df.shape)
print (df.info())
print (df.describe())
print (df.dtypes)

# Part 2 
# Missing Values
Chk_null = df.isnull().sum()
print (Chk_null)

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
df['Performance'] = df['Performance'].fillna(df['Performance'].mean())
df['City'] = df['City'].fillna("Unknown")


df['Age'] = df['Age'].round().astype(int)
df['Salary'] = df['Salary'].round().astype(int)
df['Performance'] = df['Performance'].round(2)
df["Joining Date"] = pd.to_datetime(df["Joining Date"],errors="coerce")


# Part 3  Text Cleaning
df['Name'] = df['Name'].str.strip().str.capitalize()
df['City'] = df['City'].str.strip().str.capitalize()
df['Department'] = df['Department'].str.strip().str.upper()
df['Email'] = df['Email'].str.strip().str.lower()

print (df)

# Part 4 – Duplicate Handling
# print (df.duplicated.sum())
print (df.duplicated(subset= ['Name', 'Age', 'Salary', 'Performance','City', 'Department','Joining Date', 'Email']).sum())
df.drop_duplicates(subset= ['Name', 'Age', 'Salary', 'Performance','City', 'Department','Joining Date', 'Email'], inplace=True)

print (df)
print (df.duplicated(subset= ['Name', 'Age', 'Salary', 'Performance','City', 'Department','Joining Date', 'Email']).sum())

df.reset_index(drop=True, inplace=True)

chk_null_2ndtime = df.isnull().sum()
print (chk_null_2ndtime)



df["Year"] = df["Joining Date"].dt.year
df["Month"] = df["Joining Date"].dt.month
df["Day"] = df["Joining Date"].dt.day
df["Month Name"] = df["Joining Date"].dt.month_name()
df["Day Name"] = df["Joining Date"].dt.day_name()

today = pd.Timestamp.today()
df["Days Since Joined"] = (today - df["Joining Date"]).dt.days


# Part 7 – Filtering
salary_above_80000 = df[df['Salary'] > 80000]
print (salary_above_80000)

performance_greaterorequal_90 = df[df['Performance'] >= 90]
print (performance_greaterorequal_90)

only_IT_employees = df[df['Department'] == "IT"]
print (only_IT_employees)

only_lahore_employees = df[df['City'] == "Lahore"]
print (only_lahore_employees)

joined_after2022 = df[df["Joining Date"] > "2022-01-01"]
print (joined_after2022)

# Part 8  Sorting
df.sort_values(by="Salary", ascending=True, inplace=True)
df.sort_values(by="Name", ascending=True , inplace=True)
df.sort_values(by=['City', 'Salary'], inplace = True)
df.sort_values(by="Joining Date", ascending=True , inplace=True)

# salary_sort = df.sort_values("Salary")

# name_sort = df.sort_values("Name")

# city_salary_sort = df.sort_values(["City","Salary"])

print (df)

# Part 9  New Columns

df['Bonus'] = df['Salary'] * 0.15
df['Tax'] = df['Salary'] * 0.05
df['Net Salary'] = df['Salary'] + df['Bonus'] - df['Tax']

df["Bonus"] = df["Bonus"].round().astype(int)
df["Tax"] = df["Tax"].round().astype(int)
df["Net Salary"] = df["Net Salary"].round().astype(int)

def salary_category(salary):
    if salary < 40000:
        return "Low"
    elif salary <= 80000:
        return "Medium"
    else:
        return "High"

df["Salary Category"] = df["Salary"].apply(salary_category)

def performance_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

df["Performance Grade"] = df["Performance"].apply(performance_grade)

# part 10  Aggregation
avg_salary = df['Salary'].mean()
max_salary = df['Salary'].max()
min_salary = df['Salary'].min()
avg_performance = df['Performance'].mean()
employee_namecount = df["Name"].count()  #for name count 
# df.shape[0]   #for counting  rows.
      

print (avg_salary)
print (max_salary)
print (min_salary)
print (avg_performance)
print (employee_namecount)

print ("\nGrouping Data")


Salaray_by_Department = df.groupby("Department")['Salary'].sum()
salary_by_city = df.groupby("City")['Salary'].sum()
performance_by_department = df.groupby("Department")['Performance'].mean()
employeecount_by_City = df.groupby("City")["Name"].count()

print (Salaray_by_Department)
print (salary_by_city)
print (performance_by_department)
print (employeecount_by_City)

#part 12 Pivot Table
print ("\nPivot table of avg salary department by city")
pivot = df.pivot_table(
    values="Salary",
    index="City",
    columns="Department",
    aggfunc="mean"
)
print(pivot)

print ("\nPivot table of Employe count City by department")
pivot = df.pivot_table(
    values= "Name",
    index = "Department",
    columns= "City",
    aggfunc= 'count',

)
print (pivot)

print ("\nPivot table of avg performance of each department")
pivot = df.pivot_table(
    values="Performance",
    columns="Department",
    aggfunc= "mean",
)

print (pivot)

def age_category (age):
    if age >18 and age <=22:
        return "Young"
    elif age >22 and age <= 30:
        return "Adult"
    else:
        return "Senior"
df['Age Category'] = df['Age'].apply(age_category)
print (df)


df.to_excel("Cleaned Data.xlsx", index=False)
print (df)







