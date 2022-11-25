from flaskr import create_app
from .models import db, Cancion, Usuario, Album, Medio, AlbumSchema, CancionSchema, UsuarioSchema
from .views import VistaAlbum, VistaAlbumsUsuario, VistaCancion, VistaCanciones, VistaSignIn, VistaCancionesAlbum, VistaLogIn

from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/canciones/<int:id_cancion>')
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/logIn')
api.add_resource(VistaAlbumsUsuario, '/usuarios/<int:id_usuario>/albumes')
api.add_resource(VistaAlbum, '/albumes/<int:id_album>')
api.add_resource(VistaCancionesAlbum, '/albumes/<int:id_album>/canciones')

jwt = JWTManager(app)

# Test

with app.app_context():
    u = Usuario(nombre='usuarioUno',contrasena='1234')
    a_1 = Album(titulo='prueba_uno',anio=2000,descripcion='texto',medio=Medio.CD)
    a_2 = Album(titulo='prueba_dos',anio=2000,descripcion='texto',medio=Medio.CD)
    c = Cancion(titulo='TituloUno',minutos=2,segundos=25,interprete='InterpreteUno')
    album_schema = AlbumSchema()
    usuario_schema = UsuarioSchema()
    cancion_schema = CancionSchema()
    u.albumes.append(a_1)
    u.albumes.append(a_2)
    a_1.canciones.append(c)
    a_2.canciones.append(c)
    db.session.add(u)
    db.session.add(a_1)
    db.session.add(c)
    db.session.commit()
    print("How to pass from database to json ---> ", [album_schema.dump(album) for album in Album.query.all()])
    print("How to pass from database to json ---> ", [type(album_schema.dump(album)) for album in Album.query.all()])
    print(Cancion.query.all())
    print(Usuario.query.all())
    print(Usuario.query.all()[0].albumes)
    db.session.delete(u)
    print(Usuario.query.all())
    print(Album.query.all())
    