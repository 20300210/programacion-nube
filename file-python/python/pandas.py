import pandas as pd
# ventas=pd.Series([15,12,21],index=["Ene","Feb","Mar"])
# print(ventas)
# print(ventas.dtype)
# print(ventas.index)
# print(ventas.values)
# ventas.name="ventas 2020"
# print(ventas)
# ventas.index.name="Meses"
# print(ventas)
# ventas.axes
# print(ventas)
# ventas.shape
# print(ventas)

# datos={'manzanas':[3,2,0,1],'naranjas':[0,3,7,2]}
# print(datos)

# compras=pd.DataFrame(datos,index=['juno','robert','lily','david'])
# print(compras)
# compras.index
# print(compras)
# compras.columns
# print(compras)
# compras.axes
# print(compras)
# compras.index.name="clientes"
# print(compras)
# compras.columns.name="frutas"
# print(compras)
# compras.values
# print(compras)
# s=pd.Series([7,5,3])
# print(s)
# s=pd.Series([7,5,3], index=["Ene","Feb","Mar"])
# print(s)
# d={"Ene":7,"Feb":5,"Mar":3}
# s=pd.Series(d)
# print(s)
# s=pd.Series(d,index=["Abr","Mar","Feb","Ene"],dtype=int)
# print(s)

# año_inicial=int(input("intoduce el año inicial "))
# año_final=int(input("intoduce el año final "))
# ventas={}
# for i in range (año_inicial,año_final+1):
#   ventas[i]=float(input("introduce las ventas del año "+str(i)+': '))
# ventas=pd.Series(ventas)
# print('ventas\n',ventas)
# print('ventas con descuento\n',ventas*0.9)

# datos={'mes':['enero','febrero','marzo','abril'],'ventas':[30500,35600,28300,33900],'gastos':[22000,23400,18100,20700]}
# contabilidad=pd.DataFrame(datos)
# print(contabilidad)

# elementos={
#     "numero atomico":[1,6,47,88],
#     "masa atomica":[1.008,12.011,107.87,226],
#     "familia":["no metal","no metal","metal","metal"]
# }
# elementos
# tabla_periodica=pd.DataFrame(elementos)
# tabla_periodica

# unidades_datos=[
#     {"ag":2,"au":5,"cu":3,"pt":2},
#     {"ag":4,"au":6,"cu":7,"pt":2},
#     {"ag":3,"au":2,"cu":4,"pt":1}]
# unidades=pd.DataFrame(unidades_datos,index=[2015,2016,2017],columns=["ag","au","cu","pt"])
# unidades.head()
# print(unidades)

# unidades_2015={"ag":2,"au":5,"cu":3,"pt":2}
# unidades_2016={"ag":4,"au":6,"cu":7,"pt":2}
# unidades_2017={"ag":3,"au":2,"cu":4,"pt":1}
# unidades=pd.DataFrame([unidades_2015,unidades_2016,unidades_2017],index=[2015,2016,2017])
# print(unidades)