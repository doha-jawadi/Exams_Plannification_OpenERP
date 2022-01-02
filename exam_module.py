from openerp.osv import osv,fields
import openerp
class exam_module(osv.osv):
    _name='exam.module'
    _columns={
		'name': fields.char('Module',size=64),
        'filliere_id':fields.many2one('exam.filliere','Filliere',ondelete='cascade'),
			 }
exam_module()