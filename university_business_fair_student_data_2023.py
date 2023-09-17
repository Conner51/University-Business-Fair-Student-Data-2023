#import and df
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = r'C:\Users\Preston Conner\Documents\LMU_CPD_Projects\LMUCPD_busfair_student_2023_clean.csv'
df = pd.read_csv(data)

df.isnull().sum()
#missing values in username (1), college (7), majors (3), school year (3)

#find where null values are
null_mask = df.isnull()
rows_with_null = null_mask.any(axis=1) #check by row to see if any true values
rows_with_null_df = df[rows_with_null] #df with only null value rows
print(rows_with_null_df)
#18, 126, 306, 307, 311, 353, 354; go into excel to see and come to conclusion about each
#18, missing college, know from Major
#126, same case as #18
#306, missing college and major, able to look up student in handshake
#307, missing college and major, null values in handshake
#311, missing college and class, able to fix college by major, class is null
#353, missing college and class, able to fill both
#354, missing username, college, major, class, dont care about username, able to retrieve the rest

###
#created copy of excel file with cleaned data, now ready to analyze
###

#creating visuals for summary report 

#count num observations for each school year
class_counts = df['School Year'].value_counts()

#bar chart for school year
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
ax = sns.barplot(x=class_counts.index, y=class_counts.values, palette="viridis")
ax.set_title('Class Breakdown',fontsize=20)
ax.set_xlabel('Class',fontsize=16)
ax.set_ylabel('Count',fontsize=16)
plt.xticks(rotation=45,fontsize=13)
plt.yticks(fontsize=13)
plt.savefig('C:\\Users\\Preston Conner\\Documents\\LMU_CPD_Projects\\class_breakdown_bar.png', bbox_inches='tight')
plt.show()

#pie chart for school year 
sns.set(style="whitegrid")
plt.figure(figsize=(8, 8))
plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%', colors=sns.color_palette("Set3"))
plt.title('Class Breakdown',fontsize=16)
plt.savefig('C:\\Users\\Preston Conner\\Documents\\LMU_CPD_Projects\\class_breakdown_pie.png', bbox_inches='tight')
plt.show()

#count num observations for each college
college_counts = df['College'].value_counts()

#bar chart for each college
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
ax = sns.barplot(x=college_counts.index, y=college_counts.values, palette="viridis")
ax.set_title('College Breakdown',fontsize=20)
ax.set_xlabel('College',fontsize=16)
ax.set_ylabel('Count',fontsize=16)
plt.xticks(rotation=90,fontsize=13)
plt.yticks(fontsize=13)
plt.savefig('C:\\Users\\Preston Conner\\Documents\\LMU_CPD_Projects\\college_breakdown_bar.png', bbox_inches='tight')
plt.show()

#pie chart for school year 
sns.set(style="whitegrid")
plt.figure(figsize=(8, 8))
plt.pie(college_counts, labels=college_counts.index, autopct='%1.1f%%', colors=sns.color_palette("Set3"))
plt.title('College Breakdown',fontsize=16)
plt.savefig('C:\\Users\\Preston Conner\\Documents\\LMU_CPD_Projects\\college_breakdown_pie.png', bbox_inches='tight')
plt.show()

#count num observations for each major
major_counts = df['Majors'].value_counts().head(12)

#bar chart for major
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
ax = sns.barplot(x=major_counts.index, y=major_counts.values, palette="viridis")
ax.set_title('12 Most Attended Majors Breakdown',fontsize=20)
ax.set_xlabel('Majors',fontsize=16)
ax.set_ylabel('Count',fontsize=16)
plt.xticks(rotation=90,fontsize=13)
plt.yticks(fontsize=13)
plt.savefig('C:\\Users\\Preston Conner\\Documents\\LMU_CPD_Projects\\major_breakdown_bar.png', bbox_inches='tight')
plt.show()

#not creating pie chart for top 12 majors because it will not equal to 100%, misleading

##################
#business fair mostly catered to business majors, so visuals dedicated to just Business school
df_business = df[df['College'] == 'Business Administration']
print(df_business)

#count num observations for each school year for business school
class_counts_business = df_business['School Year'].value_counts()

#bar chart for school year for business school
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
ax = sns.barplot(x=class_counts_business.index, y=class_counts_business.values, palette="viridis")
ax.set_title('Class Breakdown for Business School',fontsize=20)
ax.set_xlabel('Class',fontsize=16)
ax.set_ylabel('Count',fontsize=16)
plt.xticks(rotation=45,fontsize=13)
plt.yticks(fontsize=13)
plt.savefig('C:\\Users\\Preston Conner\\Documents\\LMU_CPD_Projects\\class_breakdown_business_school_bar.png', bbox_inches='tight')
plt.show()

#pie chart for school year for business school
sns.set(style="whitegrid")
plt.figure(figsize=(8, 8))
plt.pie(class_counts_business, labels=class_counts_business.index, autopct='%1.1f%%', colors=sns.color_palette("Set3"))
plt.title('Class Breakdown for Business School',fontsize=16)
plt.savefig('C:\\Users\\Preston Conner\\Documents\\LMU_CPD_Projects\\class_breakdown_business_school_pie.png', bbox_inches='tight')
plt.show()

#count num observations for each major for business school
major_counts_business = df_business['Majors'].value_counts().head(12)

#bar chart for major
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
ax = sns.barplot(x=major_counts_business.index, y=major_counts_business.values, palette="viridis")
ax.set_title('12 Most Attended Majors Breakdown for Business School',fontsize=20)
ax.set_xlabel('Majors',fontsize=16)
ax.set_ylabel('Count',fontsize=16)
plt.xticks(rotation=90,fontsize=13)
plt.yticks(fontsize=13)
plt.savefig('C:\\Users\\Preston Conner\\Documents\\LMU_CPD_Projects\\major_breakdown_business_school_bar.png', bbox_inches='tight')
plt.show()

####
#create a dummy boolean column for check ins into 1s and 0s
df['Checked In Boolean'] = (df['Checked In'] != 'No').astype(int)

#calculate the counts for boolean check in
check_boolean_counts = df['Checked In Boolean'].value_counts()
#pie chart of checked in or not
sns.set(style="whitegrid")
plt.figure(figsize=(8, 8))
labels = ['Checked In', 'Not Checked In']
label_fmt = lambda p: f'{check_boolean_counts[1]} ({p:.1f}%)' if p > 0 else f'{check_boolean_counts[0]} ({p:.1f}%)'
plt.pie(check_boolean_counts, labels=labels, autopct=label_fmt, startangle=140, colors=['green', 'red'])
plt.axis('equal')
plt.title('Check-In Status', fontsize=16)
plt.savefig('C:\\Users\\Preston Conner\\Documents\\LMU_CPD_Projects\\check_in_status_pie.png', bbox_inches='tight')
plt.show()

#convert check in column into date time to visualize later
df['Checked In'] = pd.to_datetime(df['Checked In'], errors='coerce')
import matplotlib.dates as mdates
#create a plot of distribution of check-in times
plt.figure(figsize=(10, 6))
sns.histplot(df['Checked In'], bins=10, kde=True, color='skyblue')
plt.xlabel('Check-In Time')
plt.ylabel('Frequency')
plt.title('Distribution of Check-In Times',fontsize=16)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%I:%M %p"))
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('C:\\Users\\Preston Conner\\Documents\\LMU_CPD_Projects\\distribution_check_in_times.png', bbox_inches='tight')
plt.show()

#two subplots combined; (violin plot and bar plot)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
#violin plot
sns.violinplot(x='Total Check-Ins', data=df, ax=ax1, color='skyblue')
ax1.set_xlabel('Total Check-Ins')
ax1.set_ylabel('Density')
ax1.set_title('Violin Plot of Total Table Check-Ins')
#bar plot
checkin_counts = df['Total Check-Ins'].value_counts().reset_index()
checkin_counts.columns = ['Total Check-Ins', 'Count']
checkin_counts = checkin_counts.sort_values(by='Total Check-Ins')
sns.barplot(x='Total Check-Ins', y='Count', data=checkin_counts, ax=ax2, color='skyblue')
ax2.set_xlabel('Total Check-Ins')
ax2.set_ylabel('Count')
ax2.set_title('Bar Plot of Total Table Check-Ins')
plt.tight_layout()
plt.savefig('C:\\Users\\Preston Conner\\Documents\\LMU_CPD_Projects\\Distribution_total_table_checkins_violin_and_bar.png', bbox_inches='tight')
plt.show()

###
#create dummy column for if registered or not
df['Registered Boolean'] = (df['Registered'] != 'No').astype(int)
#create new dataframe of just people who for sure attended/checkedin
df_checkedin = df[df['Checked In Boolean']==1]
#value count of atendees who for sure attended and if they registered
registered_boolean_counts = df_checkedin['Registered Boolean'].value_counts()

#pie chart of attendees who registered or not
sns.set(style="whitegrid")
plt.figure(figsize=(8, 8))
labels = ['Registered', 'Did not Register']
label_fmt = lambda p: f'{registered_boolean_counts[1]} ({p:.1f}%)' if p > 0 else f'{registered_boolean_counts[0]} ({p:.1f}%)'
plt.pie(registered_boolean_counts, labels=labels, autopct=label_fmt, startangle=140, colors=['green', 'red'])
plt.axis('equal')
plt.title('Attendees Who Registered or Not', fontsize=16)
plt.savefig('C:\\Users\\Preston Conner\\Documents\\LMU_CPD_Projects\\if_registered_attendees_breakdown_pie.png', bbox_inches='tight')
plt.show()

#create a wordcloud for majors
from wordcloud import WordCloud
df['Majors'] = df['Majors'].astype(str) #fix error that floats were found
majors_text = ' '.join(df['Majors'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(majors_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('C:\\Users\\Preston Conner\\Documents\\LMU_CPD_Projects\\wordcloud_majors.png', bbox_inches='tight')

#create stacked bar plot of registered vs nonregistered confirmed attendees per class
colors = ['#00FFFF', '#800000']
registration_counts = df_checkedin.groupby(['School Year', 'Registered Boolean'])['First Name'].count().unstack()
registration_counts[::-1].plot(kind='bar', stacked=True, figsize=(12, 6), color=colors)
plt.title('Breakdown of Registered and Non-Registered Attendees by Class Year', fontsize=16)
plt.xlabel('Class Year', fontsize=13)
plt.ylabel('Count', fontsize=13)
plt.xticks(rotation=0, fontsize=12)  # Rotate the x ticks to horizontal
plt.xticks(
    range(len(registration_counts)),
    ['Freshmen', 'Sophomore', 'Junior', 'Senior', 'Masters', 'Alumni'], fontsize=12
)
plt.legend(['Registered', 'Non-Registered'], fontsize=12)
plt.savefig('C:\\Users\\Preston Conner\\Documents\\LMU_CPD_Projects\\confirmed_attendees_registered_vs_not_per_class_stackbar.png', bbox_inches='tight')
plt.show()