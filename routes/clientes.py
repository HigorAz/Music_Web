from flask import render_template, request, jsonify
from . import bp
from db.database import get_db

@bp.route('/clientes', methods=['POST', 'GET'])

def handle__clientes():
    if request.method == 'GET':
        return get_clientes()
    elif request.method == 'POST':
        return add_cliente()


def get_clientes():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM clientes')
        dados = cursor.fetchall()
        return render_template("clientes.html", dados = dados)
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def add_cliente():
    login = request.json.get('login')
    senha = request.json.get('senha')
    planos_id = request.json.get('planos_id')
    email = request.json.get('email')


    if not login:
        return jsonify({'error': 'login é obrigatório'})
    if not senha:
        return jsonify({'error': 'senha é obrigatória'})
    if not planos_id:
        return jsonify({'error': 'planos_id é obrigatório'})
    if not email:
        return jsonify({'error': 'email é obrigatório'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO clientes (login, senha, planos_id, email) VALUES (?, ?, ?, ?)', (login, senha, planos_id, email))
        db.commit()
        return jsonify({'message': 'Dados inseridos com sucesso'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

#========================================================================================================================================

@bp.route('/cliente/<int:cliente_id>', methods=['DELETE', 'GET', 'PUT'])

def handle_cliente (cliente_id):
    if request.method == 'GET':
        return get_cliente(cliente_id)
    elif request.method == 'DELETE':
        return delete_cliente(cliente_id)
    elif request.method == 'PUT':
        return update_cliente(cliente_id)

def get_cliente(cliente_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM clientes WHERE id = ?', (cliente_id,))
        id = cursor.fetchone()
        if id: 
            return jsonify(dict(id))
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def delete_cliente(cliente_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM clientes WHERE id = ?', (cliente_id,))
        dado = cursor.fetchone()
        if dado: 
            cursor.execute('DELETE FROM clientes WHERE id = ?', (cliente_id,))
            db.commit()
            return jsonify({'message': 'Dado excluído com sucesso'})
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def update_cliente(cliente_id):
    login = request.json.get('login')
    senha = request.json.get('senha')
    planos_id = request.json.get('planos_id')
    email = request.json.get('email')


    if not login:
        return jsonify({'error': 'login é obrigatório'})
    if not senha:
        return jsonify({'error': 'senha é obrigatória'})
    if not planos_id:
        return jsonify({'error': 'planos_id é obrigatório'})
    if not email:
        return jsonify({'error': 'email é obrigatório'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM clientes WHERE id = ?', (cliente_id,))
        id = cursor.fetchone()
        if id: 
            cursor.execute('UPDATE clientes set login = ?, senha = ?, planos_id = ?, email = ? WHERE id = ?', (login, senha, planos_id, email, cliente_id,))
            db.commit()
            return jsonify({'message': 'Dados alterados com sucesso!'}), 200
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()