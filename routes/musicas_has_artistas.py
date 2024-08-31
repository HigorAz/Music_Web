from flask import request, jsonify
from . import bp
from db.database import get_db

@bp.route('/musicas_has_artistas', methods=['POST', 'GET'])

def handle__musicas_has_artistas():
    if request.method == 'GET':
        return get_musicas_has_artistas()
    elif request.method == 'POST':
        return add_artista()


def get_musicas_has_artistas():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM musicas_has_artistas')
        dados = cursor.fetchall()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def add_artista():
    musicas_id = request.json.get('musicas_id')
    artistas_id = request.json.get('artistas_id')

    if not musicas_id:
        return jsonify({'error': 'musicas_id é obrigatório'})
    if not artistas_id:
        return jsonify({'error': 'artistas_id é obrigatória'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO musicas_has_artistas (musicas_id, artistas_id) VALUES (?, ?)', (musicas_id, artistas_id))
        db.commit()
        return jsonify({'message': 'Dados inseridos com sucesso'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

#========================================================================================================================================

@bp.route('/musicas_has_artista/<int:musicas_has_artista_id>', methods=['DELETE', 'GET', 'PUT'])

def handle_musicas_has_artista (musicas_has_artista_id):
    if request.method == 'GET':
        return get_musicas_has_artista(musicas_has_artista_id)
    elif request.method == 'DELETE':
        return delete_musicas_has_artista(musicas_has_artista_id)
    elif request.method == 'PUT':
        return update_musicas_has_artista(musicas_has_artista_id)

def get_musicas_has_artista(musicas_has_artista_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM musicas_has_artistas WHERE id = ?', (musicas_has_artista_id,))
        id = cursor.fetchone()
        if id: 
            return jsonify(dict(id))
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def delete_musicas_has_artista(musicas_has_artista_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM musicas_has_artistas WHERE id = ?', (musicas_has_artista_id,))
        dado = cursor.fetchone()
        if dado: 
            cursor.execute('DELETE FROM musicas_has_artistas WHERE id = ?', (musicas_has_artista_id,))
            db.commit()
            return jsonify({'message': 'Dado excluído com sucesso'})
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def update_musicas_has_artista(musicas_has_artista_id):
    musicas_id = request.json.get('musicas_id')
    artistas_id = request.json.get('artistas_id')

    if not musicas_id:
        return jsonify({'error': 'musicas_id é obrigatório'})
    if not artistas_id:
        return jsonify({'error': 'artistas_id é obrigatória'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM musicas_has_artistas WHERE id = ?', (musicas_has_artista_id,))
        id = cursor.fetchone()
        if id: 
            cursor.execute('UPDATE musicas_has_artistas set musicas_id = ?, artistas_id = ? WHERE id = ?', (musicas_id, artistas_id, musicas_has_artista_id,))
            db.commit()
            return jsonify({'message': 'Dados alterados com sucesso!'}), 200
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()