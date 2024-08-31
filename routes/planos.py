from flask import request, jsonify
from . import bp
from db.database import get_db

@bp.route('/planos', methods=['POST', 'GET'])

def handle__planos():
    if request.method == 'GET':
        return get_planos()
    elif request.method == 'POST':
        return add_plano()


def get_planos():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM planos')
        dados = cursor.fetchall()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def add_plano():
    descricao = request.json.get('descricao')
    valor = request.json.get('valor')
    limite = request.json.get('limite')


    if not descricao:
        return jsonify({'error': 'descricao é obrigatório'})
    if not valor:
        return jsonify({'error': 'valor é obrigatória'})
    if not limite:
        return jsonify({'error': 'limite é obrigatório'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO planos (descricao, valor, limite) VALUES (?, ?, ?)', (descricao, valor, limite,))
        db.commit()
        return jsonify({'message': 'Dados inseridos com sucesso'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

#========================================================================================================================================

@bp.route('/plano/<int:plano_id>', methods=['DELETE', 'GET', 'PUT'])

def handle_plano (plano_id):
    if request.method == 'GET':
        return get_plano(plano_id)
    elif request.method == 'DELETE':
        return delete_plano(plano_id)
    elif request.method == 'PUT':
        return update_plano(plano_id)

def get_plano(plano_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM planos WHERE id = ?', (plano_id,))
        id = cursor.fetchone()
        if id: 
            return jsonify(dict(id))
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def delete_plano(plano_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM planos WHERE id = ?', (plano_id,))
        dado = cursor.fetchone()
        if dado: 
            cursor.execute('DELETE FROM planos WHERE id = ?', (plano_id,))
            db.commit()
            return jsonify({'message': 'Dado excluído com sucesso'})
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def update_plano(plano_id):
    descricao = request.json.get('descricao')
    valor = request.json.get('valor')
    limite = request.json.get('limite')


    if not descricao:
        return jsonify({'error': 'descricao é obrigatório'})
    if not valor:
        return jsonify({'error': 'valor é obrigatória'})
    if not limite:
        return jsonify({'error': 'limite é obrigatório'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM planos WHERE id = ?', (plano_id,))
        id = cursor.fetchone()
        if id: 
            cursor.execute('UPDATE planos set descricao = ?, valor = ?, limite = ? WHERE id = ?', (descricao, valor, limite, plano_id,))
            db.commit()
            return jsonify({'message': 'Dados alterados com sucesso!'}), 200
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()