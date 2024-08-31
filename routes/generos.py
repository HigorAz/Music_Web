from flask import request, jsonify
from . import bp
from db.database import get_db

@bp.route('/generos', methods=['POST', 'GET'])

def handle__generos():
    if request.method == 'GET':
        return get_generos()
    elif request.method == 'POST':
        return add_genero()


def get_generos():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM generos')
        dados = cursor.fetchall()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def add_genero():
    descricao = request.json.get('descricao')

    if not descricao:
        return jsonify({'error': 'descricao é obrigatório'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO generos (descricao) VALUES (?)', (descricao))
        db.commit()
        return jsonify({'message': 'Dados inseridos com sucesso'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

#========================================================================================================================================

@bp.route('/genero/<int:genero_id>', methods=['DELETE', 'GET', 'PUT'])

def handle_genero (genero_id):
    if request.method == 'GET':
        return get_genero(genero_id)
    elif request.method == 'DELETE':
        return delete_genero(genero_id)
    elif request.method == 'PUT':
        return update_genero(genero_id)

def get_genero(genero_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM generos WHERE id = ?', (genero_id,))
        id = cursor.fetchone()
        if id: 
            return jsonify(dict(id))
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def delete_genero(genero_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM generos WHERE id = ?', (genero_id,))
        dado = cursor.fetchone()
        if dado: 
            cursor.execute('DELETE FROM generos WHERE id = ?', (genero_id,))
            db.commit()
            return jsonify({'message': 'Dado excluído com sucesso'})
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def update_genero(genero_id):
    descricao = request.json.get('descricao')

    if not descricao:
        return jsonify({'error': 'descricao é obrigatório'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM generos WHERE id = ?', (genero_id,))
        id = cursor.fetchone()
        if id: 
            cursor.execute('UPDATE generos set descricao = ? WHERE id = ?', (descricao, genero_id,))
            db.commit()
            return jsonify({'message': 'Dados alterados com sucesso!'}), 200
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()