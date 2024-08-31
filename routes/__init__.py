from flask import Blueprint

# Blueprint para as rotas
bp = Blueprint('routes', __name__)

# Importar rotas de outros arquivos
from .artistas import *
from .clientes import *
from .generos import *
from .gravadoras import *
from .musicas import *
from .pagamentos import *
from .planos import *
from .musicas_has_artistas import *
from .musicas_has_clientes import *
from .index import *
