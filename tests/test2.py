# import pandas as pd
# from dto import TrackDataDTO
# from loaders import TCXLoader
# # Sample list of objects (you'll replace this with your data)
# class Object:
#     def __init__(self, speed):
#         self.speed = speed

# dto = TCXLoader()._loadTCXFile('E:/IOT/Projects/Python/GPSTrackEditor/Sergiu_Toporjinschi_2023-09-22_18-28-23.TCX')


# # Convert the list of objects to a pandas DataFrame
# df = pd.DataFrame([(obj.speed, obj.distance) for obj in dto.trackPoints], columns=['speed', 'distance'])

# # Apply the logical expression
# # filtered_df = df[(df['distance'] > 110) & (df['distance'] < 150)]
# # filtered_dfs = df[pd.eval(expr='distance > 110 & distance < 150',local_dict={'df' : df})]
# filtered_dfs = df.query('distance > 110 & distance < 150')
# # Get the positions of the objects that match the expression
# # positions = filtered_df.index.tolist()
# positions = filtered_dfs.index.tolist()
# print(positions)


from UtilFunctions import buildAttributeExpression

buildAttributeExpression("test", ">220&<110|>220&<110|>220&<110&>220&<110")
