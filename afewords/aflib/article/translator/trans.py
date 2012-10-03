from translator import *
from replaceutils import *
from replacepattern import *

_ref_line_repls = [ih4, ih3, ih2, ibold, idel, iins, iitalic,
                    isup, isub, ibr, ihr, iindent3, iindent2, iindent1]
_ref_pro_repls = [ilink, imath, iequation, icode, iesc]
_ref_line_trans = LineTranslator(*_ref_line_repls)
_ref_pro_trans = ProtectTranslator(*_ref_pro_repls)
reference_translator = Translator(_ref_pro_trans, _ref_line_trans)
normal_translator = reference_translator

class ArticleTranslator(Translator):

    line_repls = [ih4, ih3, ih2, ibold, idel, iins, iitalic, 
                    isup, isub, ibr, ihr, iindent3, iindent2, iindent1]
    protect_trans = None
    line_trans = LineTranslator(*line_repls)

    def __init__(self, refinder):
        iref = RefPattern(refinder)
        self.pro_repls = [ilink, imath, iequation, icode, iesc]
        self.pro_repls.append(iref)
        self.protect_trans = ProtectTranslator(*self.pro_repls)
