from openerp.osv import osv,fields
import openerp
class exam_salle(osv.osv):
    _name='exam.salle'
    _columns={
		'name': fields.char('Local', size=64),
        #'type_id': fields.many2one('exam.type','Type de Local',ondelete='cascade'),
        'surveillant_id': fields.one2many('exam.surveillant','salle',string='Surveillant'),
			 }
exam_salle()

