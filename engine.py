import pandas as pd
import numpy as np

df = pd.read_csv('FeaturesData.csv')
df.index += 1

def recommended_cars(features_vectos, features_priorities):
    # user desired features input
    user_desired_features = features_vectos
    # user features priority input
    user_features_priorities = features_priorities

    # list to hold the similarity score of cars matching users choice
    similarity_score = []

    df2 = df.drop('Car names', axis = 1)

    # function to calculate similarity scores
    def similar_cars(user_DV):
        user_vector = np.array(user_desired_features)

        for i in range(1,len(df2)+1):
            v = list(df2.loc[i])
            vector = np.array(v)
            dist = np.linalg.norm(vector - user_vector) 
            similarity_score.append(round(dist, 2))

        return similarity_score

    # function to make seprate dataframe for user for further comptations and to find similar cars ids
    def seprate_df():
        df["E_distance"] = similar_cars(features_vectos)
        
        # sorting cars score-wise and making a new df
        new_df = df.nsmallest(6,'E_distance')
        
        # for repeatation purpose
        similarity_score.clear()

        similar_cars_id = list(new_df.index)
        return similar_cars_id

    id_score_dict = {}
    def make_dict(user_features_priorities):
        similar_cars_ids = seprate_df()
        
        # rolling back df to its original form for computation of final similar car score
        df.drop('E_distance', axis = 1, inplace = True)

        for i in similar_cars_ids[1:]:
            score = np.dot(user_features_priorities, list(df2.loc[i]))
            id_score_dict[i] = score

        return id_score_dict

    # final list that will be containing similar cars ids
    car_id_recommendations = []

    score_dict = make_dict(user_features_priorities)
    score_dict_temp = score_dict
    sorted_scores = sorted(score_dict.values(), reverse = True)

    def get_key(id):
        for key, value in score_dict_temp.items():
            if id == value:
                return key

    for i in sorted_scores:
        car_id = get_key(i)
        car_id_recommendations.append(car_id)
        del score_dict_temp[car_id]

    return car_id_recommendations
