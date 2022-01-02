{
    'name':'Exam Planning',
    'version':'1.0',
    'author':'Doha&Samia',
    'category':'BI ENSAH ERP',
    'sequence':1,
    'description': """
	
          gestion de planification des examens de l'ecole ENSAH/Option BI
		  
        
        *Gestion des Horaires
		*Gestion des Salles
        *Gestion des personnels
        *Gestion des modules
    
    """,
    'website':'http://www.Doha&Samia.ma',
    'images':['C:\\Users\\lenevo\\Pictures\\planning.PNG'],
    'depends':['base'],
    #insertion des views
    'data':['exam_etudiant_view.xml',
            'exam_semestre_view.xml',
            'exam_session_view.xml',
            'exam_salle_view.xml',
            'exam_annee_view.xml',
            'exam_element_view.xml',
            'exam_module_view.xml',
            'exam_surveillant_view.xml',
            'exam_examen_view.xml',
            'exam_filliere_view.xml',
            'exam_examen_wkf_view.xml'],
    'init_xml' : [],
    'update_xml' : [],
    'js':[],
    'qweb':[],
    'css':[],
    'demo':[],
    'test':[],
    "installable": True,
    "auto_install": False
}