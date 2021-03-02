from flask import Flask,jsonify,request
app = Flask(__name__)
from products import products

@app.route('/ping')
def ping():
    return jsonify({"message":"Pong!"})

@app.route('/products', methods=['GET'])   #por defecto la ruta sin añadirle el tio de método usan el método get,  
# por lo caual en le ruta anterior no necesitamos aclarar el tipo de petición,esto sirve sólo cuando hagas una petición 
# diferente a la GET
def getProducts():
    return jsonify({"product" :products, "message":"products list"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    # print(product_name)
    # return "received"
    productFound = [product for product in products if product['name'] == product_name]
    if len(productFound) == 0:
       return jsonify ({"message":"No se encontró este producto"})
    return jsonify({"product":productFound[0]})

# hasta ahora estamos obteniendo datos,  pero también podemos crear datos
# con una aplicación, pero  aquí sólo estamos  viendo cómo hacer la  api,
# por eso usamos otra llamada insomnia
@app.route('/products', methods = ['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantyty": request.json['quantyty']
    }
    products.append(new_product)
    return jsonify({"message": "producto agregado satisfactoriamente", "products":products})


                                                                   #  OPERACION PUT
@app.route('/products/<string:product_name>', methods = ['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) >0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantyty'] = request.json['quantyty']
        return jsonify({"message" : "producto actualizado", "product" : productFound[0]})
    return jsonify({"message": "Producto no encontrado"})



                                                                     # OPERACION DELETE
@app.route('/products/<string:product_name>',methods = ['DELETE'])

def deleteProduct(product_name):
        productsFound = [product for product in products if product['name'] == product_name]
        if len(productsFound)>0:
            products.remove(productsFound[0])
            return jsonify({"message": "producto eliminado", "products": products})
        return jsonify({"message": "producto no encontrado"})




if __name__ == '__main__':
    app.run(debug=True,port = 4000)