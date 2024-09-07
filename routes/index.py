from flask import render_template, request, jsonify
from . import bp
from db.database import get_db

@bp.route('/')
def home():
    return render_template ("base.html")

# """
#     <h1>Bem vindo à API FLASK </h1>
#     <p>Esta API permite que você execute operações na tabela 'Artistas'</p>
#     <p>Rotas disponíveis</p>
#     <ul>
#         <li>
#             POST /dados - Adiciona um novo dado. Envie um JSON com os campos 'nome' e 'idade'.
#         </li>
#         <li>
#             GET /dados - Retorna todos os dados da tabela.
#         </li>
#         <li>
#             GET /dados/{id} - Retorna um dado em específico.
#         </li>
#         <li>
#             PUT /dados/{id} - Atualiza um dado existente. Envie um JSON com os campos 'nome' e 'idade'.
#         </li>
#         <li>
#             DELETE /dados/{id} - Deleta um dado existente.
#         </li>
#     </ul>
#     """