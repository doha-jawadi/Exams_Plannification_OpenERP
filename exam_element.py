from openerp.osv import osv,fields
import openerp
class exam_element(osv.osv):
    _name='exam.element'
    _columns={
		'name': fields.char('Element',size=255),
        'module_id':fields.many2one('exam.module','Module',ondelete='cascade'),
			 }
exam_element()