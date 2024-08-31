from flask import request, jsonify
from . import bp
from db.database import get_db

@bp.route('/pagamentos', methods=['POST', 'GET'])

def handle__pagamentos():
    if request.method == 'GET':
        return get_pagamentos()
    elif request.method == 'POST':
        return add_pagamento()


def get_pagamentos():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM pagamentos')
        dados = cursor.fetchall()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def add_pagamento():
    data = request.json.get('data')

    if not data:
        return jsonify({'error': 'data é obrigatório'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO pagamentos (data) VALUES (?)', (data,))
        db.commit()
        return jsonify({'message': 'Dados inseridos com sucesso'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

#========================================================================================================================================

@bp.route('/pagamento/<int:pagamento_id>', methods=['DELETE', 'GET', 'PUT'])

def handle_pagamento (pagamento_id):
    if request.method == 'GET':
        return get_pagamento(pagamento_id)
    elif request.method == 'DELETE':
        return delete_pagamento(pagamento_id)
    elif request.method == 'PUT':
        return update_pagamento(pagamento_id)

def get_pagamento(pagamento_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM pagamentos WHERE id = ?', (pagamento_id,))
        id = cursor.fetchone()
        if id: 
            return jsonify(dict(id))
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def delete_pagamento(pagamento_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM pagamentos WHERE id = ?', (pagamento_id,))
        dado = cursor.fetchone()
        if dado: 
            cursor.execute('DELETE FROM pagamentos WHERE id = ?', (pagamento_id,))
            db.commit()
            return jsonify({'message': 'Dado excluído com sucesso'})
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def update_pagamento(pagamento_id):
    data = request.json.get('data')

    if not data:
        return jsonify({'error': 'data é obrigatório'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM pagamentos WHERE id = ?', (pagamento_id,))
        id = cursor.fetchone()
        if id: 
            cursor.execute('UPDATE pagamentos set data = ? WHERE id = ?', (data, pagamento_id,))
            db.commit()
            return jsonify({'message': 'Dados alterados com sucesso!'}), 200
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()