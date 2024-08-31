from flask import request, jsonify
from . import bp
from db.database import get_db

@bp.route('/musicas', methods=['POST', 'GET'])

def handle__musicas():
    if request.method == 'GET':
        return get_musicas()
    elif request.method == 'POST':
        return add_musica()


def get_musicas():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM musicas')
        dados = cursor.fetchall()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def add_musica():
    nome = request.json.get('nome')
    duracao = request.json.get('duracao')
    generos_id = request.json.get('generos_id')
    lancamento = request.json.get('lancamento')


    if not nome:
        return jsonify({'error': 'nome é obrigatório'})
    if not duracao:
        return jsonify({'error': 'duracao é obrigatória'})
    if not generos_id:
        return jsonify({'error': 'generos_id é obrigatório'})
    if not lancamento:
        return jsonify({'error': 'lancamento é obrigatório'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO musicas (nome, duracao, generos_id, lancamento) VALUES (?, ?, ?, ?)', (nome, duracao, generos_id, lancamento))
        db.commit()
        return jsonify({'message': 'Dados inseridos com sucesso'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

#========================================================================================================================================

@bp.route('/musica/<int:musica_id>', methods=['DELETE', 'GET', 'PUT'])

def handle_musica (musica_id):
    if request.method == 'GET':
        return get_musica(musica_id)
    elif request.method == 'DELETE':
        return delete_musica(musica_id)
    elif request.method == 'PUT':
        return update_musica(musica_id)

def get_musica(musica_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM musicas WHERE id = ?', (musica_id,))
        id = cursor.fetchone()
        if id: 
            return jsonify(dict(id))
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def delete_musica(musica_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM musicas WHERE id = ?', (musica_id,))
        dado = cursor.fetchone()
        if dado: 
            cursor.execute('DELETE FROM musicas WHERE id = ?', (musica_id,))
            db.commit()
            return jsonify({'message': 'Dado excluído com sucesso'})
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def update_musica(musica_id):
    nome = request.json.get('nome')
    duracao = request.json.get('duracao')
    generos_id = request.json.get('generos_id')
    lancamento = request.json.get('lancamento')


    if not nome:
        return jsonify({'error': 'nome é obrigatório'})
    if not duracao:
        return jsonify({'error': 'duracao é obrigatória'})
    if not generos_id:
        return jsonify({'error': 'generos_id é obrigatório'})
    if not lancamento:
        return jsonify({'error': 'lancamento é obrigatório'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM musicas WHERE id = ?', (musica_id,))
        id = cursor.fetchone()
        if id: 
            cursor.execute('UPDATE musicas set nome = ?, duracao = ?, generos_id = ?, lancamento = ? WHERE id = ?', (nome, duracao, generos_id, lancamento, musica_id,))
            db.commit()
            return jsonify({'message': 'Dados alterados com sucesso!'}), 200
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()