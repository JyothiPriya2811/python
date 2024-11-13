import pandas  as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C://Users/RK/Downloads/matches.csv")
matches_per_season =data.groupby("Venue").size().reset_index(name='Match_Count')
print(matches_per_season)
plt.scatter(matches_per_season['Venue'],matches_per_season['Match_Count'])
plt.xlabel('Venue')
plt.ylabel('Number of Matches')
plt.title('Number of Matches in Each Venue')
plt.show()