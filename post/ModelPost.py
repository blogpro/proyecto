from post.models import Post,PostAdd
from comentarios.models import Comentario

class GetPostMixin(object):
	def GetPost(self,pk):
		ObjPost = Post.objects.get(pk=pk)
		PostMatriz = []
		p = ObjPost
		file_info = {}

		#----------------------------------------Lista Post---------------------------------------
		ListaPost = []
		ObjPostAdd = PostAdd.objects.filter(post__id= p.id).order_by('order')
		for s in ObjPostAdd:
			file_info_html = {}
			if s.subtitulopost != None:
				file_info_html['inicio_html']="<br><h5>"
				file_info_html['codigo_pos'] = s.subtitulopost
				file_info_html['fin_html']="</br>"
				file_info_html['id_post_add']=s.id
			if s.descripcionpost != None:	
				file_info_html['inicio_html']="<p>"
				file_info_html['codigo_pos'] = s.descripcionpost
				file_info_html['fin_html']="</p>"
				file_info_html['id_post_add']=s.id
			if s.codigospost != None:	
				file_info_html['inicio_html']="<pre class='brush: python'>"
				file_info_html['codigo_pos'] = s.codigospost
				file_info_html['fin_html']="</pre>"
				file_info_html['id_post_add']=s.id
			if s.imagenpost != None:
				file_info_html['inicio_html']="<img class='img-responsive' src='"	
				file_info_html['codigo_pos'] =s.imagenpost
				file_info_html['fin_html']=" ' alt=''> "
				file_info_html['id_post_add']=s.id
			ListaPost.append(file_info_html)
		file_info['postList']=ListaPost
		#----------------------------------------Lista Post---------------------------------------

		
		file_info['title']=p.title
		file_info['first_name']=p.user.first_name
		file_info['last_name']=p.user.last_name
		file_info['fecha']=p.fecha_registro
		file_info['categoria']=p.categoria
		ObjComentarioCount = Comentario.objects.filter(post__id=p.id).count()
		file_info['comentarios']=ObjComentarioCount

		PostMatriz.append(file_info)
		return PostMatriz	


class QueryPostMixin(object):
	def QueryPost(self):
		ObjPost = Post.objects.all()
		PostMatriz = []
		for p in ObjPost:
			file_info = {}

			#----------------------------------------Lista Post---------------------------------------
			ListaPost = []
			ObjPostAdd = PostAdd.objects.filter(post__id= p.id).order_by('order')
			for s in ObjPostAdd:
				file_info_html = {}
				if s.subtitulopost != None:
					file_info_html['inicio_html']="<br><h5>"
					file_info_html['codigo_pos'] = s.subtitulopost
					file_info_html['fin_html']="</br>"
					file_info_html['id_post_add']=s.id
				if s.descripcionpost != None:	
					file_info_html['inicio_html']="<p>"
					file_info_html['codigo_pos'] = s.descripcionpost
					file_info_html['fin_html']="</p>"
					file_info_html['id_post_add']=s.id
				if s.codigospost != None:	
					file_info_html['inicio_html']="<pre class='brush: python'>"
					file_info_html['codigo_pos'] = s.codigospost
					file_info_html['fin_html']="</pre>"
					file_info_html['id_post_add']=s.id
				if s.imagenpost != None:
					file_info_html['inicio_html']="<img class='img-responsive' src='"	
					file_info_html['codigo_pos'] =s.imagenpost
					file_info_html['fin_html']=" ' alt=''> "
					file_info_html['id_post_add']=s.id
				ListaPost.append(file_info_html)
			file_info['postList']=ListaPost
			#----------------------------------------Lista Post---------------------------------------

			
			file_info['title']=p.title
			file_info['id']=p.id
			file_info['first_name']=p.user.first_name
			file_info['last_name']=p.user.last_name
			file_info['fecha']=p.fecha_registro
			file_info['categoria']=p.categoria
			ObjComentarioCount = Comentario.objects.filter(post__id=p.id).count()
			file_info['comentarios']=ObjComentarioCount

			PostMatriz.append(file_info)
		return PostMatriz