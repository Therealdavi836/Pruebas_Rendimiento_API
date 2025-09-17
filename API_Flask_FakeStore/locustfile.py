#Tarea #1 creacion de la api y separación de responsabilidades para prueba de rendimiento
#Importamos a locust
from locust import HttpUser, task

# --------------- Locust Test ----------------- #
class SimpleProduct(HttpUser):

    #Prueba de metodo get de todos los productos de la API flask
    @task
    def get_product(self):
        self.client.get('/products')
    
    #Prueba de metodo get devolviendo un solo producto
    @task
    def get_single_product(self):
        self.client.get('/products/1')
    
    #Prueba de metodo post enviando un producto
    @task
    def create_product(self):
        data = {
            "title": "string",
            "price": 0.1,
            "description": "string",
            "category": "string",
            "image": "http://example.com"
        }
        self.client.post('/products', json=data)
    
    #Prueba de metodo put actualizando un producto
    @task
    def update_product(self):
        data = {
            "id": 1,
            "title": "string",
            "price": 0.1,
            "description": "string",
            "category": "string",
            "image": "http://example.com"
        }
        self.client.put('/products/1', json=data)
    
    #Prueba de metodo delete borrando un producto
    @task
    def delete_product(self):
        self.client.delete('/products/1')
    