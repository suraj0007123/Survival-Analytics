import pandas as pd


#loading the ecgset
ecg_data = pd.read_excel(r"E:\DESKTOPFILES\suraj\assigments\survival analysis\Datasets_Survival Analytics\ECG_Surv.xlsx")

#2.	Work on each feature of the ecgset to create a ecg dictionary as displayed in the below image
#######feature of the ecgset to create a ecg dictionary

#######feature of the ecgset to create a ecg dictionary


ecg_details =pd.DataFrame({"column name":ecg_data.columns,
                            "ecg type(in Python)": ecg_data.dtypes})

            #3.	ecg Pre-ecgcessing
          #3.1 ecg Cleaning, Feature Engineering, etc
          

            

#details of ecg 
ecg_data.info()
ecg_data.describe()          


ecg_data.drop(columns=["name"],inplace = True) # dropind row num 1


#ecg types        
ecg_data.dtypes



#checking for na value
ecg_data.isna().sum()
ecg_data.isnull().sum()

ecg = ecg_data.fillna("None")
ecg.isna().sum()
#checking unique value for each columns
ecg.nunique()



"""	Exploratory ecg Analysis (EDA):
	Summary
	Univariate analysis
	Bivariate analysis """
    

ecg.columns
ecg.mean()
ecg.median()
ecg.mode()
ecg.std()
ecg.var()
ecg.skew()
ecg.kurt()



# covariance for ecg set 
covariance = ecg.cov()
covariance

# Correlation matrix 
co = ecg.corr()
co


import seaborn as sns
####### graphiecg repersentation



#boxplot for every continuous type data
ecg.columns
ecg.nunique()

ecg.boxplot(column=["survival_time_hr"])   #no outlier
 

sns.pairplot(ecg.iloc[:, :],hue="alive")
sns.pairplot(ecg.iloc[:, :],hue="group")

# Boxplot of independent variable distribution for each category of Result 
sns.boxplot(x = "alive", y = "survival_time_hr", data = ecg)
sns.boxplot(x = "group", y = "survival_time_hr", data = ecg)



# Scatter plot for each categorical Result of car
sns.stripplot(x = "alive", y = "survival_time_hr", jitter = True, data = ecg)
sns.stripplot(x = "group", y = "survival_time_hr", jitter = True, data = ecg)




"""	Model Building"""

T=ecg.survival_time_hr

# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and groups for death 
kmf.fit(T, event_observed=ecg.alive)

# Time-line estimations plot 
kmf.plot()


# Over Multiple groups 
# For each group, here group is group
ecg.group.value_counts()

# Applying KaplanMeierFitter model on Time and groups for the group "1"
kmf.fit(T[ecg.group==1], ecg.group[ecg.group==1], label='group-1')
ax = kmf.plot()

# Applying KaplanMeierFitter model on Time and groups for the group "2"
kmf.fit(T[ecg.group==2], ecg.group[ecg.group==2], label='group-2')
kmf.plot(ax=ax)

# Applying KaplanMeierFitter model on Time and groups for the group "3"
kmf.fit(T[ecg.group==3], ecg.group[ecg.group==3], label='group-3')
kmf.plot(ax=ax)
