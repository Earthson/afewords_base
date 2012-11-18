#coding=utf-8
from basehandler import *
from pages.postjson import ObjRemoveJson

from authority import *

from generator import generator, cls_gen
from article import *

class ObjRemovePara(BaseHandlerPara):
    paradoc = {
        'obj_id': None,
        'obj_type': 'blog',
    }


class ObjRemoveHandler(BaseHandler):
    
    @with_login_post
    def post(self):
        handler_para = ObjRemovePara(self)
        handler_json = ObjRemoveJson(self)
        usr = self.current_user
        obj_toremove = generator(handler_para['obj_id'], 
                                handler_para['obj_type'])
        if obj_toremove is None:
            handler_json.by_status(2)
            handler_json.write()
            return #Obj Not Exist
        env = obj_toremove.env
        auth_ans = obj_toremove.authority_verify(usr, env)
        if test_auth(auth_ans, A_DEL) is False:
            handler_json.by_status(3)
            handler_json.write()
            return #Delete Permission Denied
        obj_toremove.remove()
        handler_json.by_status(0)
        handler_json.write()
        return #0
