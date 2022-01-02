from openerp.osv import osv,fields
import openerp
class exam_etudiant(osv.osv):
    _name='exam.etudiant'
    _columns={
        'name': fields.char('Nom', size=128),
        'prenom': fields.char('Prenom', size=128),
        'filliere_id':fields.many2one('exam.filliere','Filliere',ondelete='cascade'),
        'semestre_id':fields.many2one('exam.semestre','Semestre',ondelete='cascade'),
			 }
exam_etudiant()