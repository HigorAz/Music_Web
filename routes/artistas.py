import sqlite3
from flask import render_template, request, jsonify
from . import bp
from db.database import get_db

@bp.route('/artistas', methods=['POST', 'GET'])

def handle__artistas():
    if request.method == 'GET':
        return get_artistas()
    elif request.method == 'POST':
        return add_artista()


def get_artistas():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM artistas')
        dados = cursor.fetchall()
        return render_template("artistas.html", dados = dados)
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def add_artista():
    nome = request.json.get('nome')
    gravadoras_id = request.json.get('gravadoras_id')

    if not nome:
        return jsonify({'error': 'nome é obrigatório'})
    if not gravadoras_id:
        return jsonify({'error': 'gravadoras_id é obrigatória'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO artistas (NOME, gravadoras_id) VALUES (?, ?)', (nome, gravadoras_id))
        db.commit()
        return jsonify({'message': 'Dados inseridos com sucesso'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

#========================================================================================================================================

@bp.route('/artista/<int:artista_id>', methods=['DELETE', 'GET', 'PUT'])

def handle_artista (artista_id):
    if request.method == 'GET':
        return get_artista(artista_id)
    elif request.method == 'DELETE':
        return delete_artista(artista_id)
    elif request.method == 'PUT':
        return update_artista(artista_id)

def get_artista(artista_id):
    try:
        db = get_db()
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute('SELECT * FROM artistas WHERE id = ?', (artista_id,))
        id = cursor.fetchone()
        if id: 
            return render_template("artista.html", id = id)
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def delete_artista(artista_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM artistas WHERE id = ?', (artista_id,))
        dado = cursor.fetchone()
        if dado: 
            cursor.execute('DELETE FROM artistas WHERE id = ?', (artista_id,))
            db.commit()
            return jsonify({'message': 'Dado excluído com sucesso'})
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def update_artista(artista_id):
    nome = request.json.get('nome')
    gravadoras_id = request.json.get('gravadoras_id')

    if not nome:
        return jsonify({'error': 'nome é obrigatório'})
    if not gravadoras_id:
        return jsonify({'error': 'gravadoras_id é obrigatória'})
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM artistas WHERE id = ?', (artista_id,))
        id = cursor.fetchone()
        if id: 
            cursor.execute('UPDATE artistas set nome = ?, gravadoras_id = ? WHERE id = ?', (nome, gravadoras_id, artista_id,))
            db.commit()
            return jsonify({'message': 'Dados alterados com sucesso!'}), 200
        else:
            return jsonify({'error': 'ID não encontrado'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()