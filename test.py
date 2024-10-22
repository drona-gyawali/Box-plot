import seaborn as sns
import matplotlib.pyplot as plt

# sorting the raw_data
raw_datasets=  [12, 15, 14, 10, 13, 25, 21, 24, 18, 19, 30, 28, 22, 35, 40]
raw_datasets.sort()


class outlier:
    def __init__(self,data):
        self.data=sorted(data)
    
    def get_len(self):
        return len(self.data)
    
    def calc_percentile(self,percentile_):
        n=self.get_len()
        R=(percentile_/100)*(n+1)
        return R
    
    def get_index_value(self,percent):
        R=self.calc_percentile(percent)
        lower_index=int(R)-1 # suppose R=4.0 then int(R)=4 : INT(R)-1 means 4-1 =3 why? Python use Zero based Index

        if R.is_integer():
            return self.data[lower_index]
        else:
            #conition is not exact so we need a mean value. 
            upper_index=lower_index+1  # lower_index = 3 : 3+1 which is upper_index[4]
            fraction = R-(lower_index+1) # R = 4: 4-(3+1) = 0.0 // get the fraction part of interpolation

            if upper_index<self.get_len():
                return (1-fraction)*self.data[lower_index]+fraction*self.data[upper_index] #linear interpolation -: percentile formula - y =Index , y^1=lower_index,y^2=upper_index: y=(1-fraction)*y^1+fraction*y^2
            else:
                result= self.data[lower_index]
            
                # Print the information inside the function
            print(f"Percentile Rank: {R}")
            print(f"Lower Index: {lower_index}, Upper Index: {upper_index}")
            print(f"Fraction: {fraction}")
            print(f"Interpolated Value: {result}")

            return result
        
    def calculate_IQR(self):
        q1=self.get_index_value(25)
        q3=self.get_index_value(75)
        IQR=q3-q1
        return q1,q3,IQR
        
    def calculated_fence(self):
        q1,q3,IQR=self.calculate_IQR()
        lower_fence=q1-1.5*(IQR)
        higher_fence=q3+1.5*(IQR)
        print(f'Lower_fence: {lower_fence}')
        print(f'Higher Fence:{higher_fence}')
        print('-'*20)    
    
    def create_boxplot(self):
        data=raw_datasets
        sns.boxplot(data)
        plt.title('Box plot')
        plt.show()
        


l=outlier(raw_datasets)
percentile_index1=l.calc_percentile(25)
percentile_index2=l.calc_percentile(75)
value_at_percentile=l.get_index_value(25)
value_at_percentile1=l.get_index_value(75)
l.calculate_IQR()
l.calculated_fence()
print(f'Percentile Index(q1): {percentile_index1}\nPercentile Index(q3): {percentile_index2}\n------------------\nQ1 Value in that Index: {value_at_percentile}\nQ3 Value in that Index: {value_at_percentile1}\n---------------------------------\nIQR: {value_at_percentile1-value_at_percentile}')
l.create_boxplot()

