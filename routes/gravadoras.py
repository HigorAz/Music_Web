from flask import request, jsonify
from . import bp
from db.database import get_db

@bp.route('/gravadoras', methods=['POST', 'GET'])

def handle__gravadoras():
    if request.method == 'GET':
        return get_gravadoras()
    elif request.method == 'POST':
        return add_gravadora()


def get_gravadoras():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM gravadoras')
        dados = cursor.fetchall()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def add_gravadora():
    nome = request.json.get('nome')
    valor_contrato = request.json.get('valor_contrato')
    vencimento_contrato = request.json.get('vencimento_contrato')


    if not nome:
        return jsonify({'error': 'nome é obrigatório'})
    if not valor_contrato:
        return jsonify({'error': 'valor_contrato é obrigatória'})
    if not vencimento_contrato:
        return jsonify({'error': 'vencimento_contrato é obrigatório'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO gravadoras (nome, valor_contrato, vencimento_contrato) VALUES (?, ?, ?)', (nome, valor_contrato, vencimento_contrato,))
        db.commit()
        return jsonify({'message': 'Dados inseridos com sucesso'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

#========================================================================================================================================

@bp.route('/gravadora/<int:gravadora_id>', methods=['DELETE', 'GET', 'PUT'])

def handle_gravadora (gravadora_id):
    if request.method == 'GET':
        return get_gravadora(gravadora_id)
    elif request.method == 'DELETE':
        return delete_gravadora(gravadora_id)
    elif request.method == 'PUT':
        return update_gravadora(gravadora_id)

def get_gravadora(gravadora_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM gravadoras WHERE id = ?', (gravadora_id,))
        id = cursor.fetchone()
        if id: 
            return jsonify(dict(id))
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def delete_gravadora(gravadora_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM gravadoras WHERE id = ?', (gravadora_id,))
        dado = cursor.fetchone()
        if dado: 
            cursor.execute('DELETE FROM gravadoras WHERE id = ?', (gravadora_id,))
            db.commit()
            return jsonify({'message': 'Dado excluído com sucesso'})
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def update_gravadora(gravadora_id):
    nome = request.json.get('nome')
    valor_contrato = request.json.get('valor_contrato')
    vencimento_contrato = request.json.get('vencimento_contrato')


    if not nome:
        return jsonify({'error': 'nome é obrigatório'})
    if not valor_contrato:
        return jsonify({'error': 'valor_contrato é obrigatória'})
    if not vencimento_contrato:
        return jsonify({'error': 'vencimento_contrato é obrigatório'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM gravadoras WHERE id = ?', (gravadora_id,))
        id = cursor.fetchone()
        if id: 
            cursor.execute('UPDATE gravadoras set nome = ?, valor_contrato = ?, vencimento_contrato = ? WHERE id = ?', (nome, valor_contrato, vencimento_contrato, gravadora_id,))
            db.commit()
            return jsonify({'message': 'Dados alterados com sucesso!'}), 200
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()