import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class Firebase:
    def ultimo_jogo(self, documento, campo):
        db = firestore.client()
        collect = db.collection('brasileirao').document(documento)
        docs = collect.get()
        doc = docs.to_dict()
        field = doc[campo]
        value = field.split('-')
        dict = {'vitoria': value[0], 'empate': value[1] ,'derrota': value[2]}
        return dict