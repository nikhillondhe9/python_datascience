import pandas as pd


class Salaries(object):

    def __init__(self):
        self.sal = pd.read_csv('Salaries.csv')

    def process_salaries(self):
        # head of the data frame
        print(self.sal.head())

        # info of the df
        print(self.sal.info())

        # average base pay
        print("Average Basepay: " + str(self.sal['BasePay'].mean()))

        # highest overtime pay
        print("Highest Overtimepay" + str(self.sal['OvertimePay'].max()))

        # job title of JOSEPH DRISCOLL
        print("Job title of JOSEPH DRISCOLL: \n" + str(self.sal[self.sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']))  # noqa

        # Total pay benefits of JOSEPH DRISCOLL
        print("Total Pay Benefits of JOSEPH DRISCOLL: \n" + str(self.sal[self.sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']))  # noqa

        # Name of the highest paid person including the benefits
        print(self.sal[self.sal['TotalPayBenefits'] == self.sal['TotalPayBenefits'].max()])

        # Name of lowest paid person (including benefits)
        print(self.sal[self.sal['TotalPayBenefits'] == self.sal['TotalPayBenefits'].min()])

        # average (mean) BasePay of all employees per year (2011-2014)
        print(self.sal.groupby('Year').mean()['BasePay'])

        # unique job titles
        print("Unique Job titles: " + str(self.sal['JobTitle'].nunique()))

        #  The top 5 most common jobs
        print("Top 5 most common job title: " + str(self.sal['JobTitle'].value_counts().head(5)))

        # Job Titles represented by only one person in 2013
        print("Job titles represented by only on person in 2013" + str(sum(self.sal[self.sal['Year'] == 2013]['JobTitle'].value_counts() == 1)))  # noqa

        # How many people have the word Chief in their job title
        def chief_string(title):
            if 'chief' in title.lower().split():
                return True
            else:
                return False
        print(sum(self.sal['JobTitle'].apply(lambda x: chief_string(x))))

        # correlation between length of the Job Title string and Salary
        self.sal['title_len'] = self.sal['JobTitle'].apply(len)
        print(self.sal[['title_len', 'TotalPayBenefits']].corr())


if __name__ == '__main__':
    salaries = Salaries()
    salaries.process_salaries()
