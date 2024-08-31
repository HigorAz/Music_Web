from flask import request, jsonify
from . import bp
from db.database import get_db

@bp.route('/musicas_has_clientes', methods=['POST', 'GET'])

def handle__musicas_has_clientes():
    if request.method == 'GET':
        return get_musicas_has_clientes()
    elif request.method == 'POST':
        return add_cliente()


def get_musicas_has_clientes():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM musicas_has_clientes')
        dados = cursor.fetchall()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def add_cliente():
    musicas_id = request.json.get('musicas_id')
    clientes_id = request.json.get('clientes_id')

    if not musicas_id:
        return jsonify({'error': 'musicas_id é obrigatório'})
    if not clientes_id:
        return jsonify({'error': 'clientes_id é obrigatória'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO musicas_has_clientes (musicas_id, clientes_id) VALUES (?, ?)', (musicas_id, clientes_id))
        db.commit()
        return jsonify({'message': 'Dados inseridos com sucesso'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

#========================================================================================================================================

@bp.route('/musicas_has_cliente/<int:musicas_has_cliente_id>', methods=['DELETE', 'GET', 'PUT'])

def handle_musicas_has_cliente (musicas_has_cliente_id):
    if request.method == 'GET':
        return get_musicas_has_cliente(musicas_has_cliente_id)
    elif request.method == 'DELETE':
        return delete_musicas_has_cliente(musicas_has_cliente_id)
    elif request.method == 'PUT':
        return update_musicas_has_cliente(musicas_has_cliente_id)

def get_musicas_has_cliente(musicas_has_cliente_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM musicas_has_clientes WHERE id = ?', (musicas_has_cliente_id,))
        id = cursor.fetchone()
        if id: 
            return jsonify(dict(id))
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def delete_musicas_has_cliente(musicas_has_cliente_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM musicas_has_clientes WHERE id = ?', (musicas_has_cliente_id,))
        dado = cursor.fetchone()
        if dado: 
            cursor.execute('DELETE FROM musicas_has_clientes WHERE id = ?', (musicas_has_cliente_id,))
            db.commit()
            return jsonify({'message': 'Dado excluído com sucesso'})
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def update_musicas_has_cliente(musicas_has_cliente_id):
    musicas_id = request.json.get('musicas_id')
    clientes_id = request.json.get('clientes_id')

    if not musicas_id:
        return jsonify({'error': 'musicas_id é obrigatório'})
    if not clientes_id:
        return jsonify({'error': 'clientes_id é obrigatória'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM musicas_has_clientes WHERE id = ?', (musicas_has_cliente_id,))
        id = cursor.fetchone()
        if id: 
            cursor.execute('UPDATE musicas_has_clientes set musicas_id = ?, clientes_id = ? WHERE id = ?', (musicas_id, clientes_id, musicas_has_cliente_id,))
            db.commit()
            return jsonify({'message': 'Dados alterados com sucesso!'}), 200
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()