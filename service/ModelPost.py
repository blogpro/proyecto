# -*- encoding: utf-8 -*-
from post.models import Post,PostAdd
from comentarios.models import Comentario
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from categorias.models import Categoria
from etiquetas.models import Etiqueta

from menu.models import Menu