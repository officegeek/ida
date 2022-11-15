# Imports
import plotly.express as px

# Brug/Access datamodel
import datamodel

# Hent data
df_Employees = datamodel.get_employees()
df_Product_Sale = datamodel.get_product_sales()

# Vis data - print
print(df_Employees)
print(df_Product_Sale.head())

# Diagram - Employee Sales - Plotly
fig_product_sale = px.histogram(df_Product_Sale, 
    x='ProductName', y='Order_Total', barmode='group',
    color='Order_Month', title='Salg pr. produkt')

# Export til Excel
df_Employees.to_excel('./Employees.xlsx', index = False)
df_Product_Sale.to_excel('./ProductSale.xlsx', index = False)

# Eksport Diagram til html
fig_product_sale.write_html('./ProductSale.html')