from openerp.osv import osv,fields
import openerp
class exam_filliere(osv.osv):
    _name='exam.filliere'
    _columns={
        'name':fields.char('Nom',size=255),
        'module_id':fields.one2many('exam.module','filliere_id',string='Liste des Modules'),
			 }
exam_filliere()