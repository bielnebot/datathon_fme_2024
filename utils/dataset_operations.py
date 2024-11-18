import pandas as pd


def append_attribute_columns():
    """
    A function that generates a dataset with 11 columns with the corresponding values
    for each individual. 
    """
    # Load data
    product_df = pd.read_csv("data/product_data.csv")
    attribute_df = pd.read_csv("data/attribute_data.csv")

    unique_products_id = product_df["cod_modelo_color"].unique()
    unique_attributes = attribute_df["attribute_name"].unique()
    print("unique_products_id",unique_products_id)

    # Create a row for each element
    list_of_rows = []
    count = 0
    for product_i in unique_products_id:
        # Percentage counter
        count += 1
        print(count/len(unique_products_id))
        
        # Original data from product_df (they have duplicates)
        original_info_row = product_df[product_df["cod_modelo_color"]==product_i].iloc[0]
        
        # Attributes:
        # Create an empty (with INVALID) row
        empty_attributes = pd.Series(["INVALID" for _ in range(len(unique_attributes))], index=unique_attributes)
        # And replace the available attributes
        attribute_info = attribute_df[attribute_df["cod_modelo_color"]==product_i]
        attribute_row = attribute_info.set_index("attribute_name").T.loc["des_value"]
        empty_attributes.update(attribute_row)
        # Combine the features and the attributes in a single row
        product_row = pd.concat([original_info_row, empty_attributes])

        list_of_rows.append(product_row)
    
    df = pd.concat(list_of_rows, axis=1).T
    df.to_csv('unique_products_with_attributes.csv', index=False)


# def image_and_y():
#     # Load data
#     product_df = pd.read_csv("data/product_data.csv")
#     attribute_df = pd.read_csv("data/attribute_data.csv")

#     unique_images = product_df["des_filename"].unique()
#     unique_attributes = attribute_df["attribute_name"].unique()

#     # Create a row for each element
#     list_of_rows = []
#     count = 0
#     for image_i in unique_images:
#         # print("New iteration:",product_i)
#         count += 1
#         print(count/len(unique_images))
        
#         # Original data from product_df (they have duplicates)
#         original_info_row = product_df[product_df["des_filename"]==image_i].iloc[0]
        
#         # Attributes:
#         product_i = original_info_row["cod_modelo_color"]
#         # Create an empty (with INVALID) row
#         empty_attributes = pd.Series(["INVALID" for _ in range(len(unique_attributes))], index=unique_attributes)
#         # And replace the available attributes
#         attribute_info = attribute_df[attribute_df["cod_modelo_color"]==product_i]
#         attribute_row = attribute_info.set_index("attribute_name").T.loc["des_value"]
#         empty_attributes.update(attribute_row)
#         # print("empty_attributes=",empty_attributes)
#         product_row = pd.concat([original_info_row, empty_attributes])
#         # print("product_row=",product_row)
#         # print(product_row.columns)
#         list_of_rows.append(product_row)
    
#     df = pd.concat(list_of_rows, axis=1).T
#     df.to_csv('images_with_attributes.csv', index=False)


if __name__ == "__main__":
    append_attribute_columns()