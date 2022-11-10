import lifelines
import pandas as pd
import numpy as np


# Loading the the survival patient data
patient_data = pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\survival analysis\Datasets_Survival Analytics\Patient.csv")

patient_data.head()

patient_data.describe()

patient_data.info()

# Lets check for null values
patient_data.isna().sum()

# No null values
# Check for duplicates
patient_data1 = patient_data.duplicated()
sum(patient_data1)
# NO duplicated values


# Label Encoder
from sklearn.preprocessing import LabelEncoder

# creating instance of labelencoder
lb = LabelEncoder()
patient_data['Scenario']= lb.fit_transform(patient_data['Scenario'])


# Followup is referring to time 
T = patient_data.Followup

# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitting model
kmf.fit(T, event_observed=patient_data.Eventtype)

# Time-line estimations plot 
kmf.plot()

# Over Multiple groups 
# For each group, here group is Scenario
patient_data.Scenario.value_counts()

# applying KaplanMeierFitter model on Time and Events for the group "1"
kmf.fit(T[patient_data.Followup==1], patient_data.Eventtype[patient_data.Followup==1], label='1')
ax = kmf.plot()

# Applying KaplanMeierFitter model on Time and Eventtypes for the group "0"
kmf.fit(T[patient_data.Scenario==0], patient_data.Eventtype[patient_data.Scenario==0], label='0')
kmf.plot(ax=ax)

patient_data.Followup 

patient_data.Eventtype
