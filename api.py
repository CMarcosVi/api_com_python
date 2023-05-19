#!/usr/bin/env python
# coding: utf-8

# In[12]:


get_ipython().system('pip install flask')
get_ipython().system('pip install gunicorn')


# In[ ]:


from flask import Flask, jsonify, request


# In[ ]:


from flask import Flask, jsonify

app = Flask(__name__)

# Rota para retornar uma mensagem de boas-vindas
@app.route('/')
def hello():
    return 'Bem-vindo à API Python!'

# Rota para retornar uma lista de itens
@app.route('/items', methods=['GET'])
def get_items():
    items = ['armas', 'comidas', 'magias']
    return jsonify(items)

# Rota para retornar uma lista de armas
@app.route('/items/armas', methods=['GET'])
def get_armas():
    armas = {
        'espadas': {'diamantina': {'dano':'100'}, 'sanguis': {'dano':'100'}},
        'foices': {'cristalina': {'dano':'100'}, 'sanguinaria': {'dano':'100'}},
        'lanças': {'salorium': {'dano':'100'}, 'donocil': {'dano':'100'}},
        'adagas': {'darrde': {'dano':'100'}, 'rovc': {'dano':'100'}},
        'espadasgrandes': {'reverberium': {'dano':'100'}, 'donorium': {'dano':'100'}}
    }
    return jsonify(armas)

# Rota para retornar uma lista de comidas
@app.route('/items/pocao', methods=['GET'])
def get_pocao():
    pocao = {
        'pocaoDeCura': {'cura': '100'},
        'pocaoDeForca': {'forca': '50'},
        'pocaoDeResistencia': {'resistencia': ''}
    }
    return jsonify(pocao)

# Rota para retornar uma lista de magias
@app.route('/items/magias', methods=['GET'])
def get_magias():
    magias = {
        'bolasElementares': {'bolaDeFogo': {'dano':'100'}, 'bolaDeGelo': {'dano':'100'}},
        'raio': {'raioDeJogo': {'dano':'100'}, 'raioDeFogo': {'dano':'100'}},
        'tornato': {'tornadoDeFogo': {'dano':'100'}, 'tornadoDeGelo': {'dano':'100'}}
    }
    return jsonify(magias)

if __name__ == '__main__':
    app.run()


# In[1]:





# In[ ]:




